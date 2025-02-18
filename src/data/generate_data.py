import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate 300 rows of data
n_samples = 300

# Generate loan IDs
loan_ids = range(1, n_samples + 1)

# Generate loan amounts (between $1000 and $40000)
loan_amounts = np.random.uniform(1000, 40000, n_samples).round(-2)  # Round to nearest 100

# Generate terms (36 or 60 months)
terms = np.random.choice(['36 months', '60 months'], n_samples, p=[0.7, 0.3])

# Generate interest rates (between 5% and 25%)
interest_rates = np.random.uniform(5, 25, n_samples).round(1)

# Generate grades (A to G with decreasing probability)
grades = np.random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 
                         n_samples, 
                         p=[0.3, 0.25, 0.2, 0.15, 0.05, 0.03, 0.02])

# Generate purposes
purposes = np.random.choice(
    ['debt_consolidation', 'credit_card', 'home_improvement', 'medical',
     'major_purchase', 'small_business', 'wedding', 'vacation', 'other'],
    n_samples,
    p=[0.4, 0.2, 0.1, 0.08, 0.07, 0.05, 0.05, 0.03, 0.02]
)

# Generate home ownership
home_ownership = np.random.choice(
    ['RENT', 'MORTGAGE', 'OWN'],
    n_samples,
    p=[0.4, 0.45, 0.15]
)

# Generate annual income (log-normal distribution)
annual_income = np.random.lognormal(11, 0.5, n_samples).round(-3)  # Round to nearest 1000
annual_income = np.clip(annual_income, 20000, 300000)

# Generate employment length (0-10+ years)
emp_length = np.random.choice(range(11), n_samples)  # 0-10 years
emp_length = [f"{x}+ years" if x == 10 else f"{x} years" for x in emp_length]

# Generate DTI (between 0 and 50)
dti = np.random.uniform(0, 50, n_samples).round(1)

# Generate FICO scores (normal distribution between 580 and 850)
fico_scores = np.random.normal(700, 50, n_samples).round().astype(int)
fico_scores = np.clip(fico_scores, 580, 850)

# Generate total credit lines (between 5 and 30)
total_credit_lines = np.random.randint(5, 31, n_samples)

# Generate revolving balance
revolving_balance = np.random.uniform(0, 50000, n_samples).round(-2)

# Generate revolving utilization (between 0 and 1)
revolving_utilization = np.random.uniform(0, 1, n_samples).round(2)

# Generate loan status (with higher default probability for lower grades and higher DTI)
def get_default_probability(grade, dti):
    base_prob = {
        'A': 0.02, 'B': 0.04, 'C': 0.08, 'D': 0.15,
        'E': 0.25, 'F': 0.35, 'G': 0.45
    }[grade]
    dti_factor = min(dti / 50, 1)  # Higher DTI increases default probability
    return base_prob * (1 + dti_factor)

loan_status = []
for grade, dti_val in zip(grades, dti):
    prob = get_default_probability(grade, dti_val)
    status = np.random.choice(['Default', 'Fully Paid'], p=[prob, 1-prob])
    loan_status.append(status)

# Create DataFrame
df = pd.DataFrame({
    'loan_id': loan_ids,
    'loan_amount': loan_amounts,
    'term': terms,
    'interest_rate': interest_rates,
    'grade': grades,
    'purpose': purposes,
    'home_ownership': home_ownership,
    'annual_income': annual_income,
    'emp_length': emp_length,
    'dti': dti,
    'fico_score': fico_scores,
    'total_credit_lines': total_credit_lines,
    'revolving_balance': revolving_balance,
    'revolving_utilization': revolving_utilization,
    'loan_status': loan_status
})

# Save raw data
df.to_csv('src/data/lending_club_raw_data.csv', index=False)

# Create golden dataset with some preprocessing
golden_df = df.copy()

# Apply preprocessing steps
golden_df['emp_length'] = golden_df['emp_length'].replace('10+ years', '10 years')
golden_df['emp_length'] = golden_df['emp_length'].str.replace(' years', '').astype(int)

# Create credit score categories
golden_df['fico_category'] = pd.cut(
    golden_df['fico_score'],
    bins=[0, 580, 670, 740, 800, 850],
    labels=['Very Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
)

# Create DTI categories
golden_df['dti_category'] = pd.cut(
    golden_df['dti'],
    bins=[0, 10, 20, 30, 40, float('inf')],
    labels=['Very Low', 'Low', 'Moderate', 'High', 'Very High']
)

# Log transform skewed features
golden_df['log_income'] = np.log1p(golden_df['annual_income'])
golden_df['log_loan_amount'] = np.log1p(golden_df['loan_amount'])

# Save golden data
golden_df.to_csv('src/data/lending_club_golden_data.csv', index=False)

print("Generated raw and golden datasets with 300 samples each.")
