import pandas as pd
import numpy as np

# LOAD DATA

df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# CREATE 10 RATING BUCKETS

NUM_BUCKETS = 10

df["rating"] = pd.qcut(
    df["fico_score"],
    q=NUM_BUCKETS,
    labels=False,
    duplicates="drop"
)

# lower rating = better credit score

df["rating"] = (
    NUM_BUCKETS - 1 - df["rating"]
)

# BUILD RATING MAP

rating_map = df.groupby("rating").agg(
    min_fico=("fico_score", "min"),
    max_fico=("fico_score", "max"),
    borrowers=("fico_score", "count"),
    defaults=("default", "sum"),
    default_rate=("default", "mean")
).reset_index()

rating_map = rating_map.sort_values(
    by="rating"
)

print("\nRATING MAP")
print(rating_map)
# ASSIGN RATING FUNCTION

def assign_rating(fico_score):
    
    for _, row in rating_map.iterrows():
        
        if (
            fico_score >= row["min_fico"]
            and
            fico_score <= row["max_fico"]
        ):
            return int(row["rating"])

    return None

# TEST EXAMPLES

scores = [500, 580, 620, 680, 720, 800]

print("\nSample Ratings")

for score in scores:
    
    rating = assign_rating(score)
    
    print(
        f"FICO Score: {score} -> Rating: {rating}"
    )

# PD LOOKUP FUNCTION

def get_pd_from_fico(fico_score):
    
    for _, row in rating_map.iterrows():
        
        if (
            fico_score >= row["min_fico"]
            and
            fico_score <= row["max_fico"]
        ):
            return float(row["default_rate"])
    
    return None


# EXAMPLE.\.venv\Scripts\Activate.ps1
fico = 680

pd_estimate = get_pd_from_fico(fico)

print(
    f"\nFICO Score {fico}"
)
print(
    f"Estimated PD = {pd_estimate:.4f}"
)