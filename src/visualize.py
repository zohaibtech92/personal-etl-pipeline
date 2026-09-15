import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_rates.db")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "static", "trend_chart.png")

def load_all_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        "SELECT date, rate FROM exchange_rates WHERE currency = 'INR' ORDER BY date ASC",
        conn
    )
    conn.close()
    return df

def plot_trend(df):
    df["date"] = pd.to_datetime(df["date"])

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["rate"], marker="o")
    plt.title("USD to INR Exchange Rate Trend")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(OUTPUT_PATH)
    print(f"Chart saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    df = load_all_data()
    plot_trend(df)