import logging
import os
import datetime

from extract import extract_data
from transform import transform_data
from load import create_table, insert_data

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "pipeline.log")

logging.basicConfig(
  filename=LOG_PATH,
  level=logging.INFO,
  format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
  logging.info("Pipeline started...!")

  try:
    raw_data = extract_data()
    logging.info("Extract step succeeded.")

    clean_df = transform_data(raw_data)
    logging.info("Transform step succeeded.")

    create_table()
    insert_data(clean_df)
    logging.info("Load step succeeded.")

    logging.info("Pipeline finish successfully.")

  except Exception as e:
    logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
  run_pipeline()