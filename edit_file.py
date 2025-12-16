import pandas as pd

df = pd.read_csv("vehicles_us_small.csv")

df_small = df.sample(n=20000, random_state=42)

df_small.to_csv("vehicles_us.csv", index=False)