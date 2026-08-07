import sqlite3
import os
import logging

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_rates.db")

def create_table():
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            rate REAL NOT NULL,
            pulled_at TEXT NOT NULL,
            UNIQUE(date)
        )
    """)
  
  conn.commit()
  conn.close()

def insert_data(df):
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  row = df.iloc[0]

  date_str = row["date"].strftime("%Y-%m-%d")       
  pulled_at_str = str(row["pulled_at"])              
  rate_value = float(row["rate"])

  try:
    cursor.execute("""
                    INSERT INTO exchange_rates(date, rate, pulled_at)
                    VALUES(?, ?, ?)
      """, (date_str, rate_value, pulled_at_str))
    
    conn.commit()
    logging.info(f"Inserted row for {date_str}: rate = {rate_value}")

  except sqlite3.IntegrityError:
    print(f"Row for {row['date']} already exists — skipping duplicate insert.")

  finally:
    conn.close()

