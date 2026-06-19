# CCA Foundations — Practice Hub

A self-contained, locally-hosted study hub for the **CCA (Claude Certified
Architect) Foundations** exam. It has two tabs:

- **📚 Resources** — what the exam covers, who it's for, official documentation,
  a curated learning path, and how to prepare.
- **📝 Practice Test** — a timed, randomized test that **hides every answer until
  you submit**, then gives you a full breakdown of how you did and where to focus.

Built with the Python **standard library only** — no `pip install`, no internet
needed to run it (the Resources tab links out to the web).

---

## Features

- **Two-tab layout.** A clean Resources study guide plus the practice test app.
  The tab bar hides automatically during a test for a distraction-free experience.
- **Fresh test every time.** Each attempt draws a random set of questions from a
  large question bank, and shuffles the order. Just start a new test
  (or refresh) for a different set.
- **Answers stay hidden.** The correct answers and explanations never reach your
  browser until you submit — grading happens server-side, so you can't peek.
- **Timed.** A live countdown (default 90 minutes) with warning colors. When time
  runs out the test auto-submits.
- **Take it like a real exam.** Jump between questions, flag ones for review, and
  see your answered/flagged progress at a glance.
- **Rich results on submit:**
  - Your score, pass/fail (70% pass mark), and time taken.
  - **Full answer key** with the correct option highlighted and an explanation
    for every question.
  - **"Where you went wrong"** — filter to show only your mistakes.
  - **Topic breakdown** — accuracy per topic, weakest first, so you know exactly
    where to focus.
  - **Takeaways** — concrete, generated study guidance based on your results.

---

## Running it

You need Python 3.7+ (already on most machines).

```bash
cd cca_practice_test
python app.py
```

Your browser opens automatically at <http://localhost:8000>. If it doesn't,
open that URL yourself.

### Options

```bash
python app.py --port 8000        # change the port
python app.py --host 0.0.0.0     # expose on your local network
python app.py --no-browser       # don't auto-open the browser
```

You can also change the question count and time limit right on the start screen
(or use the quick presets: full 60, half 30, or a quick 10).

### Using it on your phone or tablet

The app is fully mobile-friendly. To access it from another device on the same
Wi-Fi network, start the server bound to all interfaces:

```bash
python app.py --host 0.0.0.0
```

Then find your computer's local IP address:

```bash
# macOS / Linux
ipconfig getifaddr en0   # or: hostname -I
```

Open that IP in your phone's browser — e.g. `http://192.168.1.50:8000`.

> **Note:** `http://0.0.0.0:8000` is not a URL you visit — it's just what the
> server prints to show it's listening on all interfaces. Always use your
> machine's actual local IP when connecting from another device.

---

## How it works

```
cca_practice_test/
├── app.py                 # parser + zero-dependency web server + grading
├── questions/             # the 6 markdown question files (the bank)
│   └── cca_practice_exam-1.md … -6.md
├── static/
│   ├── index.html         # the single-page app
│   ├── style.css
│   └── app.js             # test flow, timer, results rendering
└── README.md
```

1. On startup, `app.py` parses all `questions/*.md` files. Each question's
   correct answer is taken from the **bolded option** in the markdown and
   cross-checked against the `Answer:` line.
2. Every question is auto-tagged with topics (MCP & Tool Design, Multi-Agent
   Systems, Prompting & Context, Safety & Guardrails, etc.) by keyword, which
   powers the focus breakdown.
3. `GET /api/quiz` builds a random test and returns it **without** answers,
   keeping the answer key in a short-lived server-side session.
4. `POST /api/submit` grades your answers, discards the session, and returns the
   full report.

## Updating the question bank

Drop new or edited markdown files into `questions/` following the same format
(a `## Question N` heading, options as `* A) …` with the correct one **bolded**,
and an `**Explanation:**` line). Restart the app and they're included
automatically.

Question content is from the
[devgotomarket/cca-prep](https://github.com/devgotomarket/cca-prep) repository.
