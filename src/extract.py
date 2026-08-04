import requests

def extract_data():
    url = 'https://api.frankfurter.dev/v1/latest?base=USD'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Something went wrong: {response.status_code}")
        return None