import pandas as pd
# LOAD NATURAL GAS PRICE DATA
df = pd.read_csv("Nat_Gas.csv")
df['Dates'] = pd.to_datetime(df['Dates'])

print("Price Data Preview:")
print(df.head())
# PRICE LOOKUP FUNCTION
def get_price(date, price_data):
   
    date = pd.to_datetime(date)

    nearest_idx = (price_data['Dates'] - date).abs().idxmin()

    return price_data.loc[nearest_idx, 'Prices']

# STORAGE CONTRACT PRICING FUNCTION

def price_storage_contract(
    injection_dates,
    withdrawal_dates,
    injection_rate,
    withdrawal_rate,
    max_volume,
    storage_cost_per_month,
    price_data
):
    total_purchase_cost = 0
    total_sales_revenue = 0
    total_storage_cost = 0

    current_inventory = 0

    print("\nTransaction Details")
    print("-" * 60)

    for inj_date, wdr_date in zip(injection_dates, withdrawal_dates):

        # Lookup prices
        buy_price = get_price(inj_date, price_data)
        sell_price = get_price(wdr_date, price_data)

        # Respect storage capacity
        injected_volume = min(
            injection_rate,
            max_volume - current_inventory
        )
        current_inventory += injected_volume

        # Respect available inventory
        withdrawn_volume = min(
            withdrawal_rate,
            current_inventory
        )
        current_inventory -= withdrawn_volume

        purchase_cost = buy_price * injected_volume
        sales_revenue = sell_price * withdrawn_volume

        total_purchase_cost += purchase_cost
        total_sales_revenue += sales_revenue

        months_stored = (
            pd.to_datetime(wdr_date)
            - pd.to_datetime(inj_date)
        ).days / 30

        storage_cost = months_stored * storage_cost_per_month

        total_storage_cost += storage_cost

        print(f"Injection Date : {inj_date}")
        print(f"Withdrawal Date: {wdr_date}")
        print(f"Buy Price      : ${buy_price:.2f}")
        print(f"Sell Price     : ${sell_price:.2f}")
        print(f"Volume         : {withdrawn_volume:,.0f}")
        print(f"Storage Cost   : ${storage_cost:,.2f}")
        print("-" * 60)

    contract_value = (
        total_sales_revenue
        - total_purchase_cost
        - total_storage_cost
    )
    return (
        contract_value,
        total_purchase_cost,
        total_sales_revenue,
        total_storage_cost
    )
# TEST CASE

injection_dates = [
    "2022-05-31",
    "2022-06-30"
]

withdrawal_dates = [
    "2022-11-30",
    "2022-12-31"
]

contract_value, purchase_cost, sales_revenue, storage_cost = (
    price_storage_contract(
        injection_dates=injection_dates,
        withdrawal_dates=withdrawal_dates,
        injection_rate=500000,
        withdrawal_rate=500000,
        max_volume=500000,
        storage_cost_per_month=10000,
        price_data=df
    )
)
# FINAL SUMMARY
print("\n")
print("=" * 60)
print("GAS STORAGE CONTRACT VALUATION")
print("=" * 60)

print(f"Total Purchase Cost : ${purchase_cost:,.2f}")
print(f"Total Sales Revenue : ${sales_revenue:,.2f}")
print(f"Total Storage Cost  : ${storage_cost:,.2f}")
print("-" * 60)
print(f"Contract Value      : ${contract_value:,.2f}")
print("=" * 60)