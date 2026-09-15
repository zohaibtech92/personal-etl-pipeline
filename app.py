from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "exchange_rates.db")

def get_all_rows():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT date, currency, rate, pulled_at FROM exchange_rates ORDER BY date DESC"
    ).fetchall()
    conn.close()
    return rows

@app.route("/")
def home():
    rows = get_all_rows()
    latest = rows[0] if rows else None
    return render_template("index.html", rows=rows, latest=latest)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))