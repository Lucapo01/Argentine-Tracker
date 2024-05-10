import requests
import pandas as pd

base_url = "https://fcitracker.online:8000"

r = requests.get(base_url+"/tickers/")
tickers = r.json()
tickers = {"1": tickers["1"]} # testing

for id, name in tickers.items():
    r = requests.get(base_url+f"/tickers/{id}")
    data = r.json()["funds"]["total"]
    df = pd.DataFrame(data)
    df['dates'] = pd.to_datetime(df['dates'], format='%d-%m-%Y')
    df.drop(columns=['prices'], inplace=True)
    df['delta'] = df['qty'].diff()
    df['delta_perc'] = (df['delta'] / df['qty'].shift(1)) * 100
    df['delta'] = df['delta'].abs()
    df['delta_perc'] = df['delta_perc'].abs()

    top_5_deltas = df.nlargest(5, 'delta')

    print(top_5_deltas)
