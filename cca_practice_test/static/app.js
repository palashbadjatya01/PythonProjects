"use strict";

// ---------------------------------------------------------------------------
// State
// ---------------------------------------------------------------------------
const state = {
  quiz: null,          // { session, minutes, count, questions: [...] }
  answers: {},         // qid -> letter
  flagged: new Set(),  // qid
  current: 0,          // index into quiz.questions
  startTime: null,
  deadline: null,
  timerHandle: null,
  submitted: false,
};

const $ = (sel) => document.querySelector(sel);
const el = (tag, cls, html) => {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (html !== undefined) e.innerHTML = html;
  return e;
};
const esc = (s) =>
  String(s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
  );

function showScreen(id) {
  document.querySelectorAll(".screen").forEach((s) => s.classList.add("hidden"));
  $("#" + id).classList.remove("hidden");
  window.scrollTo(0, 0);
}

// ---------------------------------------------------------------------------
// Tab navigation
// ---------------------------------------------------------------------------
function switchTab(name) {
  // Don't allow leaving an in-progress test by mistake.
  if (name !== "practice" && state.quiz && !state.submitted) {
    const ok = confirm(
      "A test is in progress. Leaving this tab won't stop the timer. Switch anyway?"
    );
    if (!ok) return;
  }
  document.querySelectorAll(".tab").forEach((t) =>
    t.classList.toggle("active", t.dataset.tab === name)
  );
  document.querySelectorAll(".tab-panel").forEach((p) =>
    p.classList.toggle("hidden", p.id !== "tab-" + name)
  );
  window.scrollTo(0, 0);
}

document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => switchTab(tab.dataset.tab));
});
// "Go to practice" shortcuts on the resources tab.
["goto-practice", "goto-practice-btn"].forEach((id) => {
  const node = document.getElementById(id);
  if (node)
    node.addEventListener("click", (e) => {
      e.preventDefault();
      switchTab("practice");
    });
});

// ---------------------------------------------------------------------------
// Start screen
// ---------------------------------------------------------------------------
async function loadInfo() {
  try {
    const info = await (await fetch("/api/info")).json();
    $("#bank-size").textContent = info.total_questions;
    const resSize = document.getElementById("res-bank-size");
    if (resSize) resSize.textContent = info.total_questions;
    $("#opt-count").value = info.default_count;
    $("#opt-count").max = info.total_questions;
    $("#opt-minutes").value = info.default_minutes;
  } catch (e) {
    $("#bank-size").textContent = "470";
    const resSize = document.getElementById("res-bank-size");
    if (resSize) resSize.textContent = "470";
  }
}

document.querySelectorAll(".chip").forEach((chip) => {
  chip.addEventListener("click", () => {
    $("#opt-count").value = chip.dataset.count;
    $("#opt-minutes").value = chip.dataset.min;
  });
});

$("#btn-start").addEventListener("click", startTest);
$("#btn-restart").addEventListener("click", () => location.reload());

async function startTest() {
  const count = Math.max(1, parseInt($("#opt-count").value || "60", 10));
  const minutes = Math.max(1, parseInt($("#opt-minutes").value || "90", 10));
  $("#btn-start").disabled = true;
  $("#btn-start").textContent = "Building your test…";
  try {
    const res = await fetch(`/api/quiz?count=${count}&minutes=${minutes}`);
    state.quiz = await res.json();
  } catch (e) {
    alert("Could not load the test. Is the server running?");
    $("#btn-start").disabled = false;
    $("#btn-start").textContent = "Start Test";
    return;
  }
  state.answers = {};
  state.flagged = new Set();
  state.current = 0;
  state.submitted = false;
  state.startTime = Date.now();
  state.deadline = Date.now() + state.quiz.minutes * 60 * 1000;

  buildPalette();
  renderQuestion();
  startTimer();
  $("#timer").classList.remove("hidden");
  $("#main-tabs").classList.add("hidden"); // distraction-free during the test
  showScreen("screen-test");
}

// ---------------------------------------------------------------------------
// Timer
// ---------------------------------------------------------------------------
function startTimer() {
  updateTimer();
  state.timerHandle = setInterval(updateTimer, 1000);
}
function updateTimer() {
  const remaining = Math.max(0, state.deadline - Date.now());
  const totalSec = Math.floor(remaining / 1000);
  const m = String(Math.floor(totalSec / 60)).padStart(2, "0");
  const s = String(totalSec % 60).padStart(2, "0");
  const t = $("#timer");
  t.textContent = `${m}:${s}`;
  t.classList.toggle("warn", totalSec <= 300 && totalSec > 60);
  t.classList.toggle("danger", totalSec <= 60);
  if (remaining <= 0) {
    clearInterval(state.timerHandle);
    submitTest(true);
  }
}

// ---------------------------------------------------------------------------
// Question rendering
// ---------------------------------------------------------------------------
function renderQuestion() {
  const q = state.quiz.questions[state.current];
  const container = $("#question-container");
  container.innerHTML = "";

  const card = el("div", "qcard");
  const meta = el("div", "qmeta");
  meta.appendChild(
    el("div", null, `Question ${state.current + 1} of ${state.quiz.count}`)
  );
  const topics = el("div", "topics");
  q.topics.forEach((t) => topics.appendChild(el("span", "tag", esc(t))));
  meta.appendChild(topics);
  card.appendChild(meta);

  card.appendChild(el("div", "qtext", esc(q.question)));

  const opts = el("div", "options");
  q.options.forEach((o) => {
    const opt = el("div", "option");
    if (state.answers[q.qid] === o.letter) opt.classList.add("selected");
    opt.appendChild(el("span", "letter", esc(o.letter)));
    opt.appendChild(el("span", "otext", esc(o.text)));
    opt.addEventListener("click", () => {
      state.answers[q.qid] = o.letter;
      renderQuestion();
      updateProgress();
    });
    opts.appendChild(opt);
  });
  card.appendChild(opts);
  container.appendChild(card);

  $("#btn-prev").disabled = state.current === 0;
  $("#btn-next").disabled = state.current === state.quiz.count - 1;
  $("#btn-flag").textContent = state.flagged.has(q.qid)
    ? "⚑ Unflag"
    : "⚑ Flag for review";
  updatePalette();
}

$("#btn-prev").addEventListener("click", () => {
  if (state.current > 0) { state.current--; renderQuestion(); }
});
$("#btn-next").addEventListener("click", () => {
  if (state.current < state.quiz.count - 1) { state.current++; renderQuestion(); }
});
$("#btn-flag").addEventListener("click", () => {
  const qid = state.quiz.questions[state.current].qid;
  if (state.flagged.has(qid)) state.flagged.delete(qid);
  else state.flagged.add(qid);
  renderQuestion();
  updateProgress();
});
$("#btn-submit").addEventListener("click", () => submitTest(false));

// ---------------------------------------------------------------------------
// Palette / progress
// ---------------------------------------------------------------------------
function buildPalette() {
  const palette = $("#palette");
  palette.innerHTML = "";
  state.quiz.questions.forEach((q, i) => {
    const b = el("button", "pnum", String(i + 1));
    b.addEventListener("click", () => { state.current = i; renderQuestion(); });
    palette.appendChild(b);
  });
  updateProgress();
}
function updatePalette() {
  const nodes = $("#palette").children;
  state.quiz.questions.forEach((q, i) => {
    const n = nodes[i];
    n.classList.toggle("answered", state.answers[q.qid] !== undefined);
    n.classList.toggle("flagged", state.flagged.has(q.qid));
    n.classList.toggle("current", i === state.current);
  });
}
function updateProgress() {
  $("#answered-count").textContent = Object.keys(state.answers).length;
  $("#flagged-count").textContent = state.flagged.size;
  updatePalette();
}

// ---------------------------------------------------------------------------
// Submit + results
// ---------------------------------------------------------------------------
async function submitTest(auto) {
  if (state.submitted) return;
  const answeredCount = Object.keys(state.answers).length;
  const unanswered = state.quiz.count - answeredCount;
  if (!auto && unanswered > 0) {
    const ok = confirm(
      `You have ${unanswered} unanswered question(s). Submit anyway?`
    );
    if (!ok) return;
  }
  state.submitted = true;
  clearInterval(state.timerHandle);
  const elapsed = Math.floor((Date.now() - state.startTime) / 1000);

  let report;
  try {
    const res = await fetch("/api/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        session: state.quiz.session,
        answers: state.answers,
        elapsed_seconds: elapsed,
      }),
    });
    if (!res.ok) {
      const err = await res.json();
      alert(err.error || "Could not grade the test.");
      return;
    }
    report = await res.json();
  } catch (e) {
    alert("Network error grading the test.");
    return;
  }
  $("#timer").classList.add("hidden");
  $("#main-tabs").classList.remove("hidden"); // restore tabs after the test
  renderResults(report, auto);
  showScreen("screen-results");
}

function fmtDuration(sec) {
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${m}m ${String(s).padStart(2, "0")}s`;
}

function ringColor(pct) {
  if (pct >= 85) return "#16a34a";
  if (pct >= 70) return "#f59e0b";
  return "#dc2626";
}

function renderResults(report, auto) {
  // Summary card
  const summary = $("#results-summary");
  summary.innerHTML = "";
  if (auto) {
    summary.appendChild(el("div", "banner", "⏰ Time expired — your test was submitted automatically."));
  }
  const card = el("div", "summary-card");
  const ring = el("div", "score-ring");
  ring.style.setProperty("--pct", report.score_pct);
  ring.style.setProperty("--ring-color", ringColor(report.score_pct));
  ring.innerHTML = `<div class="inner"><div><div class="pct">${report.score_pct}%</div><div class="frac">${report.correct}/${report.total}</div></div></div>`;
  card.appendChild(ring);

  const meta = el("div", "summary-meta");
  const verdict = report.passed
    ? `<span class="verdict pass">PASS</span>`
    : `<span class="verdict fail">KEEP STUDYING</span>`;
  meta.innerHTML = `
    <h2>Your Result ${verdict}</h2>
    <p>You answered <strong>${report.correct}</strong> of <strong>${report.total}</strong> correct
       (pass mark ${report.pass_mark}%).</p>
    <p>Time taken: <strong>${fmtDuration(report.elapsed_seconds)}</strong></p>`;
  card.appendChild(meta);
  summary.appendChild(card);

  // Takeaways
  const tk = $("#results-takeaways");
  tk.innerHTML = "";
  const tkPanel = el("div", "panel");
  tkPanel.appendChild(el("h2", null, "Your takeaways &amp; how to prepare"));
  const ul = el("ul", "takeaways");
  report.takeaways.forEach((t) => ul.appendChild(el("li", null, esc(t))));
  tkPanel.appendChild(ul);
  tk.appendChild(tkPanel);

  // Topic breakdown
  const tp = $("#results-topics");
  tp.innerHTML = "";
  const tpPanel = el("div", "panel");
  tpPanel.appendChild(el("h2", null, "Where to focus — topic breakdown"));
  if (report.focus_areas.length) {
    const names = report.focus_areas.slice(0, 3).map((f) => f.topic).join(", ");
    tpPanel.appendChild(
      el("div", "focus-callout", `<strong>Spend your next study session here:</strong> ${esc(names)}. These scored below 70%.`)
    );
  }
  report.topic_breakdown.forEach((t) => {
    const row = el("div", "topic-row");
    row.appendChild(el("div", "topic-name", esc(t.topic)));
    const bar = el("div", "topic-bar");
    const fill = el("span");
    fill.style.width = t.accuracy + "%";
    fill.style.background = ringColor(t.accuracy);
    bar.appendChild(fill);
    row.appendChild(bar);
    row.appendChild(el("div", "topic-acc", `${t.accuracy}%`));
    const sub = el("div", "topic-name");
    sub.style.gridColumn = "1 / -1";
    sub.style.color = "var(--muted)";
    sub.style.fontSize = "12px";
    sub.style.marginTop = "-6px";
    sub.textContent = `${t.correct}/${t.total} correct`;
    row.appendChild(sub);
    tpPanel.appendChild(row);
  });
  tp.appendChild(tpPanel);

  // Review list
  renderReview(report);
  $("#only-wrong").checked = false;
  $("#only-wrong").onchange = () => renderReview(report);
}

function renderReview(report) {
  const onlyWrong = $("#only-wrong").checked;
  const wrap = $("#results-review");
  wrap.innerHTML = "";
  report.results.forEach((r) => {
    if (onlyWrong && r.is_correct) return;
    const item = el("div", "review-item " + (r.is_correct ? "correct" : "wrong"));
    let badge;
    if (r.is_correct) badge = `<span class="badge ok">Correct</span>`;
    else if (r.your_answer === null) badge = `<span class="badge skip">Skipped</span>`;
    else badge = `<span class="badge bad">Incorrect</span>`;

    item.appendChild(
      el("div", "rq", `<span class="num">Q${r.number}</span>${esc(r.question)}${badge}`)
    );

    r.options.forEach((o) => {
      let cls = "review-opt";
      let tail = "";
      if (o.letter === r.correct_answer) { cls += " correct"; tail = " ✓ correct answer"; }
      if (o.letter === r.your_answer && !r.is_correct) { cls += " your-wrong"; tail = " ✗ your answer"; }
      const optEl = el("div", cls,
        `<span class="ol">${esc(o.letter)}</span>${esc(o.text)}<em style="color:var(--muted)">${tail}</em>`);
      item.appendChild(optEl);
    });

    item.appendChild(
      el("div", "explanation", `<strong>Why:</strong> ${esc(r.explanation)}`)
    );
    item.appendChild(el("div", "review-source", `Source: ${esc(r.source)}`));
    wrap.appendChild(item);
  });
  if (!wrap.children.length) {
    wrap.appendChild(el("div", "panel center", "No mistakes to review — perfect score on the shown set! 🎉"));
  }
}

// Warn before accidental navigation away mid-test.
window.addEventListener("beforeunload", (e) => {
  if (state.quiz && !state.submitted) {
    e.preventDefault();
    e.returnValue = "";
  }
});

loadInfo();
