import pandas as pd

df = pd.read_csv("us-counties-5_20.csv")

df['date'] = pd.to_datetime(df['date'])
cobb_df = df[df['county'] == 'Cobb']
cobb_df.set_index("date" , inplace=True)
cobb_df['cases'].plot()