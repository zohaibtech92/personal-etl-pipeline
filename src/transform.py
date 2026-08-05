import pandas as pd
from datetime import datetime

def transform_data(raw_data):
    date = raw_data["date"]
    rate = raw_data["rates"]["EUR"]
    pulled_at = datetime.now()

    row = {
        "date": pd.to_datetime(date),
        "rate": rate,
        "pulled_at": pulled_at
    }

    df = pd.DataFrame([row])
    return df