import logging
from datetime import timedelta
import sys
from pathlib import Path

import pendulum
from airflow.sdk import dag, task, get_current_context

# Let the DAG import your existing code from the src/ folder
SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))


@dag(
    dag_id="exchange_rate_pipeline",
    schedule="0 21 * * 1-5",  # weekdays at 21:00 Pakistan time
    start_date=pendulum.datetime(2026, 10, 1, tz="Asia/Karachi"),
    catchup=False,
    default_args={"retries": 3, "retry_delay": timedelta(minutes=1)},
    tags=["etl", "exchange-rate"],
)
def exchange_rate_pipeline():

    @task
    def extract_rates():
        from extract import extract_data

        # Ask the API for the rate of the day this run is for
        logical_date = get_current_context().get("logical_date")
        date_str = logical_date.strftime("%Y-%m-%d") if logical_date else None
        logging.info(f"Fetching rate for {date_str or 'latest'}")
        return extract_data(date_str)

    @task
    def transform_rates(raw_data):
        from transform import transform_data
        df = transform_data(raw_data)
        row = df.iloc[0]
        # XCom needs plain values, so we convert the DataFrame row to a dict
        return {
            "date": row["date"].strftime("%Y-%m-%d"),
            "rate": float(row["rate"]),
            "pulled_at": str(row["pulled_at"]),
        }

    @task
    def load_rates(row):
        import pandas as pd
        from load import create_table, insert_data
        df = pd.DataFrame([{
            "date": pd.to_datetime(row["date"]),
            "rate": row["rate"],
            "pulled_at": row["pulled_at"],
        }])
        create_table()
        insert_data(df)

    raw = extract_rates()
    clean = transform_rates(raw)
    load_rates(clean)


exchange_rate_pipeline()
