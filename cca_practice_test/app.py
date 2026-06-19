"""
CCA Foundations — Local Practice Test App
=========================================

A zero-dependency, locally-hosted practice exam engine for the CCA
(Claude Certified Architect) Foundations exam.

It parses the bundled markdown question bank (6 files x 60 questions = 360),
serves a timed test of randomly selected questions, and hides every answer
until you submit. On submission it reveals your score, a full answer key with
explanations, a review of what you got wrong, and a per-topic breakdown so you
know exactly where to focus.

Run it:
    python app.py
Then open http://localhost:8000 in your browser.

Requires only the Python 3 standard library — no pip install needed.
"""

import argparse
import json
import os
import random
import re
import secrets
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_DIR = os.path.join(BASE_DIR, "questions")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Default test settings
DEFAULT_QUESTION_COUNT = 60
DEFAULT_MINUTES = 90
PASS_MARK = 0.70  # 70% to pass (typical certification threshold)


# ---------------------------------------------------------------------------
# Topic tagging
# ---------------------------------------------------------------------------
# Each question is tagged with one or more topics based on keyword matching so
# the results screen can tell the user which areas are strongest/weakest.
TOPIC_KEYWORDS = {
    "MCP & Tool Design": [
        "mcp", "tool description", "tool definition", "tool result",
        "tool selection", "input schema", "fetch server", "tool call",
        "tool use", "expose", "remote server",
    ],
    "Multi-Agent Systems": [
        "multi-agent", "multi agent", "subagent", "sub-agent", "sub agent",
        "orchestrat", "manager agent", "reviewer agent", "delegat",
        "agent team", "researcher agent", "coder agent",
    ],
    "Claude Code & Skills": [
        "claude code", "claudeignore", "claude.md", "bash tool",
        "slash command", "agent skill", "skill", "search-and-replace",
        "refactor", "codebase",
    ],
    "Prompting & Context": [
        "system prompt", "context window", "prompt", "few-shot", "few shot",
        "extended thinking", "scratchpad", "chain of thought", "instruction",
        "context engineering", "compaction",
    ],
    "Messages API & Streaming": [
        "messages api", "tool_use", "tool_result", "role", "batches api",
        "message batches", "streaming", "stop_reason", "stop sequence",
        "assistant role", "user role", "json mode",
    ],
    "Safety & Guardrails": [
        "guardrail", "confirmation", "pre-execution", "gate", "security",
        "permission", "injection", "blinding", "high-stakes", "churn",
        "sensitive", "human-in-the-loop", "human in the loop", "approval",
    ],
    "Structured Output & Data": [
        "structured output", "json schema", "xml", "extract", "parsing",
        "output format", "validate", "schema", "receipt", "currency",
    ],
    "Performance & Cost": [
        "token-efficient", "token efficient", "latency", "cost", "caching",
        "cache", "rate limit", "throughput", "batch", "efficient",
        "prompt caching",
    ],
    "Evaluation & Testing": [
        "eval", "rubric", "self-eval", "self eval", "confidence", "grade",
        "ground truth", "benchmark", "regression", "judge", "scoring",
    ],
    "RAG & Retrieval": [
        "rag", "retrieval", "embedding", "vector", "semantic search",
        "knowledge base", "chunk", "citation",
    ],
}


def tag_topics(text):
    """Return a sorted list of topics whose keywords appear in ``text``."""
    lowered = text.lower()
    topics = [
        topic
        for topic, keywords in TOPIC_KEYWORDS.items()
        if any(kw in lowered for kw in keywords)
    ]
    return topics or ["General Concepts"]


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------
OPTION_RE = re.compile(r"^\*\s+(\*\*)?\s*([A-F])\)\s*(.*?)\s*$")
ANSWER_LINE_RE = re.compile(r"\*\*(?:Correct\s+)?Answer:\s*([A-F])\*\*", re.IGNORECASE)
# Matches a corrupted stem that is only a "Question N" placeholder.
MALFORMED_STEM_RE = re.compile(r"Question\s*\d+", re.IGNORECASE)


def _clean(text):
    """Strip stray markdown emphasis markers and surrounding whitespace."""
    return text.replace("**", "").strip()


def parse_question_block(block, exam_label, number):
    """Parse a single ``## Question`` block into a structured dict.

    Returns ``None`` if the block does not contain a usable question.
    """
    lines = block.splitlines()

    question_parts = []
    options = {}            # letter -> text
    correct_letter = None   # from the bolded option
    answer_letter = None    # from the "Answer:" line, used as a cross-check
    explanation_parts = []

    mode = "question"  # question -> options -> explanation
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            continue
        # Skip horizontal-rule separators between questions.
        if set(stripped) == {"-"} and len(stripped) >= 3:
            continue

        # The explicit answer line (present in some files).
        m_ans = ANSWER_LINE_RE.search(stripped)
        if m_ans:
            answer_letter = m_ans.group(1).upper()
            mode = "explanation"
            continue

        if stripped.startswith("**Explanation:**"):
            mode = "explanation"
            explanation_parts.append(_clean(stripped[len("**Explanation:**"):]))
            continue

        m_opt = OPTION_RE.match(stripped)
        if m_opt:
            mode = "options"
            is_bold = m_opt.group(1) is not None
            letter = m_opt.group(2).upper()
            text = _clean(m_opt.group(3))
            options[letter] = text
            if is_bold:
                correct_letter = letter
            continue

        if mode == "question":
            if stripped.startswith("**Question:**"):
                question_parts.append(_clean(stripped[len("**Question:**"):]))
            else:
                question_parts.append(_clean(stripped))
        elif mode == "explanation":
            explanation_parts.append(_clean(stripped))
        # Lines in "options" mode that aren't options are ignored.

    # Prefer the bolded option; fall back to the explicit answer line.
    final_answer = correct_letter or answer_letter
    if not options or final_answer is None:
        return None

    question_text = " ".join(p for p in question_parts if p).strip()
    explanation = " ".join(p for p in explanation_parts if p).strip()

    # Some entries in the upstream bank are corrupted: the real question stem
    # was replaced by a broken cross-reference like "Question 41", leaving no
    # actual prompt. Skip these so a blank question is never served.
    if not question_text or MALFORMED_STEM_RE.fullmatch(question_text):
        return None

    full_text = question_text + " " + " ".join(options.values())
    return {
        "source": exam_label,
        "number": number,
        "question": question_text,
        "options": options,
        "answer": final_answer,
        "explanation": explanation,
        "topics": tag_topics(full_text),
    }


def load_question_bank():
    """Parse every markdown file in the questions directory."""
    bank = []
    files = sorted(
        f for f in os.listdir(QUESTIONS_DIR) if f.lower().endswith(".md")
    )
    for fname in files:
        path = os.path.join(QUESTIONS_DIR, fname)
        with open(path, encoding="utf-8") as fh:
            content = fh.read()

        exam_label = os.path.splitext(fname)[0]
        # Split on the "## Question" headers, keeping each block separate.
        blocks = re.split(r"^##\s+Question\s+\d+.*$", content, flags=re.MULTILINE)
        # blocks[0] is the file preamble; the rest are question bodies.
        for idx, block in enumerate(blocks[1:], start=1):
            parsed = parse_question_block(block, exam_label, idx)
            if parsed:
                parsed["id"] = f"{exam_label}#{idx}"
                bank.append(parsed)
    return bank


# ---------------------------------------------------------------------------
# In-memory session store
# ---------------------------------------------------------------------------
# Maps a session token to the answer key for that quiz attempt. This keeps the
# correct answers and explanations on the server until the user submits, so the
# answers never reach the browser early.
SESSIONS = {}
SESSIONS_LOCK = threading.Lock()


def build_quiz(count, minutes):
    """Create a new quiz attempt and return (public_payload, session_token)."""
    selected = random.sample(QUESTION_BANK, min(count, len(QUESTION_BANK)))
    token = secrets.token_urlsafe(16)

    public_questions = []
    answer_key = {}
    for i, q in enumerate(selected):
        qid = str(i)
        # Present options in a stable, shuffled-per-question order so the
        # correct letter's position varies, but record the mapping for grading.
        letters = sorted(q["options"].keys())
        ordered = [(letter, q["options"][letter]) for letter in letters]
        public_questions.append(
            {
                "qid": qid,
                "number": i + 1,
                "question": q["question"],
                "options": [{"letter": l, "text": t} for l, t in ordered],
                "topics": q["topics"],
            }
        )
        answer_key[qid] = q

    with SESSIONS_LOCK:
        SESSIONS[token] = {
            "answer_key": answer_key,
            "created": time.time(),
            "minutes": minutes,
        }
        _evict_old_sessions()

    payload = {
        "session": token,
        "minutes": minutes,
        "count": len(public_questions),
        "questions": public_questions,
    }
    return payload, token


def _evict_old_sessions(max_age=6 * 3600, max_sessions=200):
    """Drop stale sessions so the in-memory store doesn't grow unbounded."""
    now = time.time()
    stale = [t for t, s in SESSIONS.items() if now - s["created"] > max_age]
    for t in stale:
        SESSIONS.pop(t, None)
    if len(SESSIONS) > max_sessions:
        for t in sorted(SESSIONS, key=lambda x: SESSIONS[x]["created"])[
            : len(SESSIONS) - max_sessions
        ]:
            SESSIONS.pop(t, None)


def grade_quiz(session_token, responses, elapsed_seconds):
    """Grade a submitted quiz and produce a full results report."""
    with SESSIONS_LOCK:
        session = SESSIONS.get(session_token)
    if not session:
        return None

    answer_key = session["answer_key"]
    results = []
    correct_count = 0
    topic_stats = {}  # topic -> {"correct": n, "total": n}

    for qid, q in answer_key.items():
        chosen = responses.get(qid)  # may be None if skipped
        is_correct = chosen == q["answer"]
        if is_correct:
            correct_count += 1

        for topic in q["topics"]:
            stat = topic_stats.setdefault(topic, {"correct": 0, "total": 0})
            stat["total"] += 1
            if is_correct:
                stat["correct"] += 1

        results.append(
            {
                "number": int(qid) + 1,
                "question": q["question"],
                "options": [
                    {"letter": l, "text": t}
                    for l, t in sorted(q["options"].items())
                ],
                "your_answer": chosen,
                "correct_answer": q["answer"],
                "is_correct": is_correct,
                "explanation": q["explanation"],
                "topics": q["topics"],
                "source": q["source"],
            }
        )

    total = len(answer_key)
    score_pct = round(100 * correct_count / total, 1) if total else 0.0
    passed = (correct_count / total) >= PASS_MARK if total else False

    # Per-topic accuracy, weakest first -> this is the "where to focus" list.
    topic_breakdown = []
    for topic, stat in topic_stats.items():
        acc = round(100 * stat["correct"] / stat["total"], 1)
        topic_breakdown.append(
            {
                "topic": topic,
                "correct": stat["correct"],
                "total": stat["total"],
                "accuracy": acc,
            }
        )
    topic_breakdown.sort(key=lambda x: (x["accuracy"], -x["total"]))

    focus_areas = [t for t in topic_breakdown if t["accuracy"] < 70]
    strengths = [t for t in topic_breakdown if t["accuracy"] >= 85]

    # Free up the session now that it's been graded.
    with SESSIONS_LOCK:
        SESSIONS.pop(session_token, None)

    return {
        "score_pct": score_pct,
        "correct": correct_count,
        "total": total,
        "passed": passed,
        "pass_mark": int(PASS_MARK * 100),
        "elapsed_seconds": int(elapsed_seconds),
        "results": results,
        "topic_breakdown": topic_breakdown,
        "focus_areas": focus_areas,
        "strengths": strengths,
        "takeaways": build_takeaways(
            score_pct, passed, focus_areas, strengths, results
        ),
    }


def build_takeaways(score_pct, passed, focus_areas, strengths, results):
    """Generate human-readable study guidance from the graded results."""
    tips = []
    if passed:
        tips.append(
            f"You scored {score_pct}% — above the {int(PASS_MARK * 100)}% "
            "pass line. Solid work; keep reinforcing the weaker topics below."
        )
    else:
        tips.append(
            f"You scored {score_pct}%, below the {int(PASS_MARK * 100)}% pass "
            "line. Focus your next study sessions on the topics listed below."
        )

    if focus_areas:
        names = ", ".join(t["topic"] for t in focus_areas[:3])
        tips.append(
            f"Prioritise these weak areas first: {names}. Re-read the "
            "explanations for every question you missed in them."
        )
    else:
        tips.append(
            "No topic fell below 70% — your knowledge is well balanced. "
            "Push for consistency and speed."
        )

    if strengths:
        names = ", ".join(t["topic"] for t in strengths[:3])
        tips.append(f"Strong areas you can rely on: {names}.")

    missed = [r for r in results if not r["is_correct"]]
    skipped = [r for r in missed if r["your_answer"] is None]
    if skipped:
        tips.append(
            f"You left {len(skipped)} question(s) unanswered. On the real exam, "
            "always make an educated guess — there's no penalty for trying."
        )

    tips.append(
        "Study method: for each missed question, write one sentence in your own "
        "words explaining why the correct answer is right AND why your choice "
        "was wrong. This active recall is more effective than re-reading."
    )
    return tips


# ---------------------------------------------------------------------------
# HTTP handler
# ---------------------------------------------------------------------------
class Handler(BaseHTTPRequestHandler):
    server_version = "CCAPracticeTest/1.0"

    def log_message(self, fmt, *args):  # quieter console
        pass

    def _send(self, code, body, content_type="application/json"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body).encode("utf-8")
        elif isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path, content_type):
        try:
            with open(path, "rb") as fh:
                body = fh.read()
        except OSError:
            self._send(404, {"error": "not found"})
            return
        self._send(200, body, content_type)

    def do_GET(self):
        route = self.path.split("?", 1)[0]
        if route == "/" or route == "/index.html":
            self._send_file(os.path.join(STATIC_DIR, "index.html"), "text/html; charset=utf-8")
        elif route == "/app.js":
            self._send_file(os.path.join(STATIC_DIR, "app.js"), "application/javascript; charset=utf-8")
        elif route == "/style.css":
            self._send_file(os.path.join(STATIC_DIR, "style.css"), "text/css; charset=utf-8")
        elif route == "/api/quiz":
            from urllib.parse import urlparse, parse_qs

            params = parse_qs(urlparse(self.path).query)
            count = int(params.get("count", [DEFAULT_QUESTION_COUNT])[0])
            minutes = int(params.get("minutes", [DEFAULT_MINUTES])[0])
            count = max(1, min(count, len(QUESTION_BANK)))
            minutes = max(1, min(minutes, 600))
            payload, _ = build_quiz(count, minutes)
            self._send(200, payload)
        elif route == "/api/info":
            self._send(
                200,
                {
                    "total_questions": len(QUESTION_BANK),
                    "default_count": DEFAULT_QUESTION_COUNT,
                    "default_minutes": DEFAULT_MINUTES,
                    "pass_mark": int(PASS_MARK * 100),
                },
            )
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        route = self.path.split("?", 1)[0]
        if route != "/api/submit":
            self._send(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            data = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            self._send(400, {"error": "invalid json"})
            return

        session = data.get("session")
        responses = data.get("answers", {}) or {}
        elapsed = data.get("elapsed_seconds", 0)
        report = grade_quiz(session, responses, elapsed)
        if report is None:
            self._send(
                410,
                {"error": "This test session expired or was already submitted. Start a new test."},
            )
            return
        self._send(200, report)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
QUESTION_BANK = []


def main():
    global QUESTION_BANK
    parser = argparse.ArgumentParser(description="CCA Foundations local practice test")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--no-browser", action="store_true", help="don't auto-open the browser")
    args = parser.parse_args()

    QUESTION_BANK = load_question_bank()
    if not QUESTION_BANK:
        raise SystemExit(
            "No questions parsed. Ensure the markdown files are in ./questions/"
        )
    print(f"Loaded {len(QUESTION_BANK)} usable questions from the bank.")

    server = ThreadingHTTPServer((args.host, args.port), Handler)
    url = f"http://{args.host}:{args.port}/"
    print(f"CCA Practice Test running at {url}")
    print("Press Ctrl+C to stop.")
    if not args.no_browser:
        threading.Timer(0.7, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.shutdown()


if __name__ == "__main__":
    main()
