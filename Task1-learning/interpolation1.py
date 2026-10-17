import pandas as pd
from scipy.interpolate import interp1d

# Load data
df = pd.read_csv("Nat_Gas.csv")

# Convert dates
df["Dates"] = pd.to_datetime(df["Dates"])

# Create a separate numeric column
start_date = df["Dates"].min()

df["Days"] = (df["Dates"] - start_date).dt.days

print(df.head())

# Create interpolation model
model = interp1d(
    df["Days"],
    df["Prices"],
    kind="linear"
)

# Query date
query_date = pd.to_datetime("2021-02-18")

query_day = (query_date - start_date).days

price = model(query_day)

print("Estimated Price:", float(price))