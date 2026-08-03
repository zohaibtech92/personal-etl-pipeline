# Personal ETL Pipeline

A small data engineering project to practice the core ETL (Extract, Transform, Load) lifecycle — 
pulling data from a public API, cleaning it, storing it in a database, and eventually visualizing 
trends over time.

This is a learning project, built step by step as part of my self-study data engineering track.

## Goal

Build a simple daily pipeline that:
1. Extracts exchange rate data from a public API
2. Transforms/cleans it using Pandas
3. Loads it into a local SQLite database
4. Runs automatically on a schedule
5. Visualizes the trend over time

## Status

🚧 In progress — currently on Step 3 (Transform)

## Progress Log

### Step 0: Environment Setup ✅
- Created project folder and Python virtual environment (`venv`)
- Installed core libraries: `requests`, `pandas`, `matplotlib`
- Chose SQLite over Postgres for this first version, to keep focus on 
  learning the pipeline logic rather than database administration

### Step 1: API Research ✅
- Selected the [Frankfurter API](https://www.frankfurter.app/) for exchange rate data
  - No API key required, which keeps the first version simple
- Reviewed API documentation and saved a sample response (`sample_response.txt`)
- Manually tested the API via browser/curl to confirm the response structure
- Identified the fields I actually need: date, and the exchange rate for the currency pair I'm tracking

### Step 2: Extract ✅
- Built `src/extract.py`, which handles only one job: calling the Frankfurter API and returning the raw response
- Used the `requests` library to send a GET request to the exchange rate endpoint
- Added status code checking — if the API call succeeds (status 200), the raw JSON is returned/printed; 
  if not, a clear error message is shown instead of letting the script fail silently
- Verified the script works consistently across multiple runs
- Deliberately tested a broken URL to confirm error handling works correctly before reverting it back
- Kept this file focused purely on extraction — no cleaning or storage logic lives here, to keep each 
  pipeline stage isolated and easy to debug independently
### Step 3: Transform (coming next)
### Step 4: Load (coming next)
### Step 5: Combine into a pipeline (coming next)
### Step 6: Schedule with cron (coming next)
### Step 7: Visualize trend (coming next)

## Tech Stack

- Python 3
- Pandas
- SQLite
- Frankfurter API (exchange rates)
- Matplotlib (planned, for visualization)

## Why This Project

Built to practice the full data engineering lifecycle hands-on — generation, ingestion, 
transformation, and storage — rather than just reading about it. Each step is committed 
separately to show the build process, not just the final result.
