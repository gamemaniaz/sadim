import pandas as pd
from api.alphavantage import get


def main():
  data = get('TIME_SERIES_INTRADAY', 'TIGR', '1min')
  data.to_csv('TIGR.csv', index=False)


if __name__ == '__main__':
  main()