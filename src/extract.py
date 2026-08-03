import requests

url = 'https://api.frankfurter.dev/v1/latest?base=USD'

response = requests.get(url)

data = response.json()

if response.status_code == 200:
  print(data)
else:
  print(f"Something went wrong: {response.status_code}")