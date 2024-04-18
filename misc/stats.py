import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests
import json

DATE_FORMAT = "%d-%m-%Y --- %H:%M:%S"

r = requests.get("https://fcitracker.online:8000/users/g21jhv3223b1h")
users = r.json()
users = json.loads(users)

users.pop("lukpo.231", None)
users.pop("lukpo121.231", None)

users_qty = 0
connection_dates = []
for user in users.values():
    users_qty += 1
    connection_dates.append(
        datetime.strptime(user["last_login"], DATE_FORMAT).date()
    )

dates_df = pd.DataFrame(connection_dates, columns=["date"])
dates_df["date"] = pd.to_datetime(dates_df["date"]).dt.date
dates_df['count'] = dates_df.groupby('date')['date'].transform('count')
dates_df = dates_df.drop_duplicates(subset=['date', 'count'])

# order by date
dates_df.sort_values(by=["date"], inplace=True)
# set date as index
dates_df.set_index("date", inplace=True)
dates_df.plot(kind="bar", figsize=(15, 10))
plt.show()

# print(f"Users: {users_qty}")
# print(f"First connection: {min(connection_dates)}")
# print(f"Last connection: {max(connection_dates)}")
# print(f"All connections: {connection_dates}")
