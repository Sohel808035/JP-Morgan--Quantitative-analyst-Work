import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("Nat_Gas.csv")
df["Dates"] = pd.to_datetime(df["Dates"])

# Extract month number 
df["Month"] = df["Dates"].dt.month

# Avg price each month 
monthly_avg = df.groupby("Month")["Prices"].mean()

print(monthly_avg)

monthly_avg.plot(kind="bar")

plt.title("Average Natural Gas Price by Month")
plt.xlabel("Month")
plt.ylabel("Avg Price")
plt.show()
