import pandas as pd 
from scipy.interpolate import interp1d

df = pd.read_csv("Nat_Gas.csv  ")

df["Dates"] = pd.to_datetime(df["Dates"])

print(df.head())

#convert Dates to Numbers
df["Dates"] =(df["Dates"] - df["Dates"].min()).dt.days

print(df.head())

#create Interpolation model
model = interp1d(
    df["Dates"],
    df["Prices"],
    kind="linear"
)

#test it
#price = model(15)
#print(price)

#find for custome date prices the below 
query_date = pd.to_datetime("2021-02-18")
query_day = (query_date - df["Dates"].min()).days
price = model(query_day)
print("Estimated price",price)
#bcz of no start date mentioned so this will not work . if you want see things working see the file interpolation1.py
