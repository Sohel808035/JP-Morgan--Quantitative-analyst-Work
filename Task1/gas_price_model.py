import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib 
matplotlib.use("Agg")
import matplotlib.pyplot as plt


class GasPriceModel:

    def __init__(self, csv_file):

        self.df = pd.read_csv(csv_file)

        self.df["Dates"] = pd.to_datetime(
            self.df["Dates"],
            format="%m/%d/%y"
        )

        self.df = self.df.sort_values("Dates")

        self.start_date = self.df["Dates"].min()
        self.last_date = self.df["Dates"].max()

        self.df["Days"] = (
            self.df["Dates"] - self.start_date
        ).dt.days

        self.interpolation_model = interp1d(
            self.df["Days"],
            self.df["Prices"],
            kind="linear",
            fill_value="extrapolate"
        )

        self.forecast_model = ExponentialSmoothing(
            self.df["Prices"],
            trend="add",
            seasonal="add",
            seasonal_periods=12
        ).fit()

        self.forecast_dates = pd.date_range(
            start=self.last_date,
            periods=13,
            freq="ME"
        )[1:]

        self.forecast_prices = self.forecast_model.forecast(12)

        self.forecast_df = pd.DataFrame({
            "Date": self.forecast_dates,
            "Price": self.forecast_prices
        })

    def estimate_price(self, input_date):

        input_date = pd.to_datetime(input_date)

        if input_date <= self.last_date:

            query_day = (
                input_date - self.start_date
            ).days

            return float(
                self.interpolation_model(query_day)
            )

        else:

            future_match = self.forecast_df[
                self.forecast_df["Date"] >= input_date
            ]

            if len(future_match) > 0:
                return float(
                    future_match.iloc[0]["Price"]
                )

            return float(
                self.forecast_df.iloc[-1]["Price"]
            )

    def plot_results(self):

        plt.figure(figsize=(12, 6))

        plt.plot(
            self.df["Dates"],
            self.df["Prices"],
            label="Historical Prices"
        )

        plt.plot(
            self.forecast_df["Date"],
            self.forecast_df["Price"],
            label="Forecast Prices"
        )

        plt.title("Natural Gas Prices Forecast")

        plt.xlabel("Date")
        plt.ylabel("Price")

        plt.grid(True)
        plt.legend()

        plt.savefig("natural_gas_forecast.png")
        print("Graph saved successfully")


if __name__ == "__main__":

    model = GasPriceModel("Nat_Gas (1).csv")

    print(
        "Historical Estimate:",
        model.estimate_price("2022-06-15")
    )

    print(
        "Future Estimate:",
        model.estimate_price("2025-06-15")
    )

    model.plot_results()