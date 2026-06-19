# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository overview

This is a learning/practice repo containing two independent Python data-engineering projects. There is a shared `.venv` at the repo root (pandas, numpy).

```
json_2_csv_proj/   # JSON-to-CSV pipeline
csv_validator/     # CSV validation exercise (in-progress)
```

Activate the venv before running anything:
```bash
source .venv/bin/activate
```

---

## json_2_csv_proj

### Running

Must be run **from inside the project directory** — all paths are relative:

```bash
cd json_2_csv_proj
python main.py
```

Output CSVs land in `json_2_csv_proj/csv_output/<EventName>.csv` (append mode — re-running accumulates rows).

### Architecture

`main.py` → reads `raw_data/case.json` → `validate_json()` (checks for keys) → `DataProcessor.process_json()` → `save_to_csv()`

`DataProcessor` (in `data_process/processor.py`) expects each record to have three keys: `timestamp`, `event_name`, and `payload` (a dict). It spreads `payload` fields as individual CSV columns and writes to a file named after `event_name`.

### Known schema mismatch

The sample data in `raw_data/case.json` uses Azure Event Hub format with PascalCase keys (`EnqueuedTimeUtc`, `EventName`, `Payload` as a JSON string). The processing code expects snake_case (`timestamp`, `event_name`, `payload` as a dict). Any work involving the sample data must bridge this gap — either normalize keys in `main.py` or update the processor.

---

## csv_validator

### Running

```bash
# Current state (incomplete — hardcoded path, no argparse yet):
python csv_validator/validator.py

# Target interface per spec:
python csv_validator/validator.py --file csv_validator/data/transactions.csv
```

### Spec (from csv_validator/readme.md)

The validator must:
- Use OOP (at least one class), `logging` (no `print`), `argparse` for file path
- Validate a `transactions.csv` with columns: `transaction_id` (unique, non-null), `customer_id` (non-null), `amount` (>0 float), `transaction_date` (YYYY-MM-DD), `status` (completed/pending/failed)
- Split output into `output/valid_records.csv` and `output/invalid_records.csv` (invalid gets a `failure_reason` column)
- Log summary (totals, breakdown by reason) to console **and** `logs/validator.log`
- Exit code `0` if >90% valid, exit code `1` otherwise

The `data/transactions.csv` test file does not yet exist — it must be created manually with ≥20 rows covering all edge cases (null id, duplicate id, negative amount, bad date, invalid status, multi-failure row).
