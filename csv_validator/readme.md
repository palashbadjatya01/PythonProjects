# CSV Validation Pipeline

**DE-001 · Week 1 · Day 1–3 · Phase 1 — Python Muscle Rebuild**

Production-grade ingestion quality gate — written from scratch, independently.

---

## Meta

| Field        | Value                        |
|--------------|------------------------------|
| File         | `validator.py`               |
| Timer        | 45 minutes                   |
| AI allowed?  | No — first 45 min            |
| Docs allowed | Python official docs only    |

---

## Must Use

- OOP — at least one class
- `logging` module (no `print`)
- `argparse` for CLI
- Docstrings on all methods
- `try/except` for file errors

---

## Input Schema — `data/transactions.csv`

| # | Column             | Type   | Rules                                      |
|---|--------------------|--------|--------------------------------------------|
| 1 | `transaction_id`   | string | Non-null, **unique**                       |
| 2 | `customer_id`      | string | Non-null                                   |
| 3 | `amount`           | float  | Must be `> 0`                              |
| 4 | `transaction_date` | string | Valid `YYYY-MM-DD` format                  |
| 5 | `status`           | string | One of: `completed`, `pending`, `failed`  |

---

## What the Script Must Do

1. Accept file path as a CLI argument via `argparse`
2. Validate all 5 rules above on every row
3. Split output into `output/valid_records.csv` and `output/invalid_records.csv`
4. Invalid file gets an extra `failure_reason` column explaining why
5. Log summary to console **and** `logs/validator.log` — total, valid, invalid, breakdown by reason
6. Exit code `0` if > 90% valid · Exit code `1` if ≤ 90% valid
7. Handle file-not-found and malformed CSV without crashing

---

## Test Data Requirements

The `data/transactions.csv` file must include at least **20 rows** and cover all of these cases:

- Null `transaction_id`
- Duplicate `transaction_id`
- Negative `amount`
- Invalid date format
- Invalid status value
- Row with multiple failures

> Create the test data manually — thinking through edge cases is part of the exercise.

---

## Folder Structure

```
csv_validator/
├── data/
│   └── transactions.csv     # create this first
├── output/                  # script writes here
├── logs/                    # log files
├── validator.py             # ← your task
├── requirements.txt
└── README.md
```

---

## Rules

| | Rule |
|---|---|
| No | AI for the first 45 minutes — hard stop |
| No | Copilot or any AI extension in VS Code |
| No | `print()` for logging — use the `logging` module |
| OK | Python official docs for syntax lookup |
| OK | Your own past code as reference |
| Note | When 45 min is up — paste whatever you have, even if incomplete |

---

## Submission

When done, paste your code for a senior-engineer-style PR review — not just "does it run" but "would I approve this."
