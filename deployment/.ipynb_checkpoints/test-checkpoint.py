import requests
import pandas as pd

df = pd.read_csv('test.csv', index_col=0)
data = df.iloc[:1].to_dict(orient='records')

payload = {'features': data}

response = requests.post(
    'https://home-credit-1213.uc.r.appspot.com/predict',
    json=payload
)

try:
    response_data = response.json()
    print(response_data)
except requests.exceptions.JSONDecodeError as e:
    print(f"Failed to decode JSON response: {e}")
    print(f"Response text: {response.text}")
