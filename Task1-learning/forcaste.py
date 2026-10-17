import pandas as pd 
import matplotlib.pyplot as plt
#import forcasting model
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv("Nat_Gas.csv")

df["Dates"] = pd.to_datetime(
    df["Dates"],
    format="%m/%d/%y"
)
print(df.head())

#plot Data
plt.figure(figsize=(10, 5))
plt.plot(
    df["Dates"],
    df["Prices"]
)
#plt.show()
plt.savefig("Nat_Gas_Price_Trend.png")
plt.close()

#Train model
model = ExponentialSmoothing(
    df["Prices"],
    trend="add",
    seasonal="add",
    seasonal_periods=12 
)

#Fit model
fit_model = model.fit()

#Forecast next 12 months
future_prices = fit_model.forecast(12)
print(future_prices)

#create future dates
future_dates = pd.date_range(
    start=df["Dates"].max(),
    periods=13,
    freq="ME"
)[1:]
print(future_dates)

#combine both future dates and prices
forcaste_df = pd.DataFrame({
    "Dates": future_dates,
    "forcasted_price":future_prices.values
})
print(forcaste_df)

#plot both actual and forecasted prices
plt.figure(figsize=(10, 5))

plt.plot(
    df["Dates"],
    df["Prices"],
    label="Historical Prices"
)
plt.plot(
    forcaste_df["Dates"],
    forcaste_df["forcasted_price"],
    label="Forcast"
)
plt.legend()
plt.grid()
plt.show()



