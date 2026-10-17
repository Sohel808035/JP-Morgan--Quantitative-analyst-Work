Natural Gas Price Forecasting Model

Objective:
Estimate natural gas prices for any historical date and forecast prices one year beyond the available dataset.

Methodology:

1. Data Loading
   - Load monthly natural gas prices.
   - Convert dates to datetime format.

2. Historical Price Estimation
   - Linear interpolation is used between monthly observations.

3. Future Forecasting
   - Holt-Winters Exponential Smoothing model.
   - Additive trend.
   - Additive seasonality.
   - Seasonal period = 12 months.

4. Output
   - Historical price estimates.
   - One-year future forecast.
   - Visualization of historical and forecast prices.

Libraries:
- pandas
- numpy
- scipy
- statsmodels
- matplotlib