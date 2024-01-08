import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

DATE_FORMAT = "%d-%m-%Y --- %H:%M:%S"

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'users.json')

with open(file_path) as f:
    users = json.load(f)

users_qty = 0
connection_dates = []
for user in users.values():
    users_qty += 1
    connection_dates.append(
        datetime.strptime(user["last_login"], DATE_FORMAT).date()
    )

dates_df = pd.DataFrame(connection_dates, columns=["date"])
dates_df["date"] = pd.to_datetime(dates_df["date"])
dates_df['count'] = dates_df.groupby('date')['date'].transform('count')
dates_df = dates_df.drop_duplicates(subset=['date', 'count'])

# order by date
dates_df.sort_values(by=["date"], inplace=True)
# set date as index
dates_df.set_index("date", inplace=True)
print(dates_df)
# show histogram
# dates_df.hist()

# print(f"Users: {users_qty}")
# print(f"First connection: {min(connection_dates)}")
# print(f"Last connection: {max(connection_dates)}")
# print(f"All connections: {connection_dates}")
