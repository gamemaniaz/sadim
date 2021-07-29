import pandas as pd
import requests

API_KEY = 'CECDTJ1CWNLB889K'
BASE_URL = 'https://www.alphavantage.co/query'

def get(function: str, symbol: str, interval: str):
  url = f'{BASE_URL}?function={function}&symbol={symbol}&interval={interval}&apikey={API_KEY}&outputsize=full'
  data = requests.get(url).json()[f'Time Series ({interval})']
  rows = []
  for datetime in data:
    date, time = datetime.split()
    row = [date, time]
    row.extend(data[datetime].values())
    rows.append(row)
  return pd.DataFrame(rows, columns=['DATE', 'TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']).sort_values(by=['DATE', 'TIME']).reset_index(drop=True)
  
