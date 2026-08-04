# src/transform.py
import pandas as pd
from datetime import datetime
from extract import extract_data  

def transform_data(raw_data):
    # Pull out the date from Frankfurter API response
    date = raw_data.get("date")
    
    # Let's grab the rates dictionary
    rates_dict = raw_data.get("rates", {})
    
    # Pull out EUR (or check what is available if EUR returns None)
    rate = rates_dict.get("EUR")
    
    # Safety fallback: If EUR wasn't found, grab the first available currency just to test!
    if rate is None and rates_dict:
        first_currency = list(rates_dict.keys())[0]
        rate = rates_dict.get(first_currency)
        print(f"[Notice] 'EUR' key not found or returned None. Used '{first_currency}' instead: {rate}")

    timestamp = datetime.now()
    
    row_data = {
        "date": [date],
        "rate": [rate],
        "timestamp": [timestamp]
    }
    
    df = pd.DataFrame(row_data)
    
    # Type enforcement & conversion
    df["date"] = pd.to_datetime(df["date"])
    df["rate"] = pd.to_numeric(df["rate"])
    
    return df

# --- Pipeline Execution & Sanity Check ---
if __name__ == "__main__":
    print("1. Extracting fresh data using Frankfurter API...")
    live_raw_data = extract_data()
    
    if live_raw_data:
        print("2. Passing live data into transform_data()...\n")
        clean_df = transform_data(live_raw_data)
        
        print("--- Final Transformed DataFrame Row ---")
        print(clean_df)
        
        print("\n--- Column Data Types ---")
        print(clean_df.dtypes)
        
        # Sanity Check Output
        extracted_rate = clean_df["rate"].values[0]
        print(f"\n[Sanity Check] The extracted rate pulled is: {extracted_rate}")
        print("Compare this number with online currency rates to confirm it matches reality!")