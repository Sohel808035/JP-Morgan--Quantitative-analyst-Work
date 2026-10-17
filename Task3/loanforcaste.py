import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

# LOAD DATA
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

print("Dataset Shape:", df.shape)
print(df.head())
# FEATURES AND TARGET

features = [
    "credit_lines_outstanding",
    "loan_amt_outstanding",
    "total_debt_outstanding",
    "income",
    "years_employed",
    "fico_score"
]

target = "default"

X = df[features]
y = df[target]

# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
# RANDOM FOREST MODEL

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)

model.fit(X_train, y_train)

# MODEL EVALUATION

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, predictions)
auc = roc_auc_score(y_test, probabilities)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")
print("Accuracy :", round(accuracy, 4))
print("ROC AUC  :", round(auc, 4))

print("\nClassification Report")
print(classification_report(y_test, predictions))

# EXPECTED LOSS FUNCTION

RECOVERY_RATE = 0.10
LGD = 1 - RECOVERY_RATE


def calculate_expected_loss(
    credit_lines_outstanding,
    loan_amt_outstanding,
    total_debt_outstanding,
    income,
    years_employed,
    fico_score
):
    

    borrower = pd.DataFrame({
        "credit_lines_outstanding": [credit_lines_outstanding],
        "loan_amt_outstanding": [loan_amt_outstanding],
        "total_debt_outstanding": [total_debt_outstanding],
        "income": [income],
        "years_employed": [years_employed],
        "fico_score": [fico_score]
    })

    pd_estimate = model.predict_proba(borrower)[0][1]

    expected_loss = (
        pd_estimate
        * LGD
        * loan_amt_outstanding
    )

    return {
        "Probability_of_Default": round(pd_estimate, 4),
        "Expected_Loss": round(expected_loss, 2)
    }

# EXAMPLE

result = calculate_expected_loss(
    credit_lines_outstanding=2,
    loan_amt_outstanding=25000,
    total_debt_outstanding=40000,
    income=85000,
    years_employed=6,
    fico_score=720
)

print("\n==============================")
print("SAMPLE BORROWER")
print("==============================")
print(result)

# FEATURE IMPORTANCE
importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance")
print(importance_df)