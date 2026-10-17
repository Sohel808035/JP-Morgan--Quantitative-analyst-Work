# JPMorgan Chase & Co. - Quantitative Research Job Simulation

This repository contains completed project work, models, analysis, and solutions for the **JPMorgan Chase & Co. Quantitative Research Virtual Experience Program** (Forage).

---

## 📜 Certificate of Completion
The official completion certificate is available in the repository:
- [`Completion Certificate (PDF)`](bWqaecPDbYAwSDqJy_Sj7temL583QAYpHXD_mJqoKM64f3smeCErH_1781333360352_completion_certificate.pdf)

---

## 📁 Repository Structure & Tasks Overview

### [Task 1: Natural Gas Price Forecasting](Task1/)
- **Objective:** Estimate historical natural gas prices on arbitrary dates and forecast monthly commodity prices for one year into the future.
- **Methodology:**
  - **Historical Estimation:** Linear interpolation between monthly observed benchmark prices.
  - **Forecasting:** Holt-Winters Exponential Smoothing (`statsmodels`) capturing additive trend and 12-month annual seasonality.
- **Key Files:**
  - `gas_price_model.py`: Historical interpolation and predictive forecasting script.
  - `natural_gas_forecast.png`: Visualization of historical trends and projected future prices.
  - `Nat_Gas (1).csv`: Historical price dataset.

---

### [Task 2: Commodity Storage Contract Pricing](Task2/)
- **Objective:** Build a financial pricing model to estimate the net present value (NPV) / profit of a natural gas storage facility contract.
- **Methodology:**
  - Models injection costs, withdrawal revenues, operational injection/withdrawal rate limits, max storage capacity, and periodic storage fees.
  - Generates cash flows based on price lookup and transaction schedules to compute net profit.
- **Key Files:**
  - `seasonalgasprice.py`: Pricing contract engine and cash flow evaluation.
  - `Nat_Gas.csv`: Historical commodity pricing data.

---

### [Task 3: Credit Risk & Loan Default Prediction](Task3/)
- **Objective:** Build a predictive machine learning model to estimate the probability of default (PD) for retail borrowers and predict expected loss.
- **Methodology:**
  - Engineered borrower features: credit lines outstanding, total debt, income, years employed, and FICO scores.
  - Trained a `RandomForestClassifier` with stratified train-test splits and evaluated via ROC-AUC, Precision, Recall, and F1-score.
  - Formulated expected loss equation: $\text{Expected Loss} = \text{PD} \times \text{Exposure at Default (EAD)} \times (1 - \text{Recovery Rate})$.
- **Key Files:**
  - `loanforcaste.py`: ML pipeline, evaluation, and expected loss calculator.
  - `Task 3 and 4_Loan_Data.csv`: Borrower and loan repayment dataset.

---

### [Task 4: FICO Score Bucketing & Rating Map](Task4/)
- **Objective:** Segment borrowers into discrete credit rating buckets (1 to 10) based on FICO scores to optimize default predictability.
- **Methodology:**
  - Applied quantile-based bucketing (`pd.qcut`) to partition FICO scores into ordinal ratings.
  - Mapped rating brackets to borrower counts, empirical default rates, and minimum/maximum score boundaries.
  - Modeled rating transitions and default probability calibration.
- **Key Files:**
  - `FICO_scores.py`: Bucketing algorithm, rating table generator, and lookup functions.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+
- **Key Libraries:**
  - `pandas`, `numpy` (Data manipulation & numerical calculations)
  - `scipy`, `statsmodels` (Time series analysis & Holt-Winters smoothing)
  - `scikit-learn` (Predictive modeling & classification metrics)
  - `matplotlib` (Data visualization & forecasting plots)

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Sohel808035/JP-Morgan--Quantitative-analyst-Work.git
   cd JP-Morgan--Quantitative-analyst-Work
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux / macOS:
   source .venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install numpy pandas scipy statsmodels scikit-learn matplotlib
   ```

4. Run any of the task scripts:
   ```bash
   # Task 1
   python Task1/gas_price_model.py

   # Task 2
   python Task2/seasonalgasprice.py

   # Task 3
   python Task3/loanforcaste.py

   # Task 4
   python Task4/FICO_scores.py
   ```
