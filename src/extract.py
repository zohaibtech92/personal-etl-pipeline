import requests


def extract_data(date=None):
    """Fetch USD exchange rates from the Frankfurter API.

    date: "YYYY-MM-DD" for a specific day, or None for the latest rates.
    """
    when = date if date else "latest"
    url = f"https://api.frankfurter.dev/v1/{when}?base=USD"
    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        return response.json()
    raise Exception(f"Something went wrong: {response.status_code}")
