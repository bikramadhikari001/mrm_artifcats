# Lending Club Data Sample Metadata

## Data Source
- Source: Lending Club Historical Loan Data
- Time Period: 2007-2018
- Sample Size: Representative sample of 10,000 loans
- Data Format: CSV
- Original Source URL: https://www.lendingclub.com/info/download-data.action

## Key Features

### Target Variable
- `loan_status`: Binary indicator (Default/Non-Default)
  - Default defined as: Charged Off, Default, or Late (>120 days)
  - Non-Default: Fully Paid or Current

### Primary Features
1. **Borrower Information**
   - Annual Income
   - Employment Length
   - Home Ownership
   - Debt-to-Income Ratio
   - FICO Score Range

2. **Loan Characteristics**
   - Loan Amount
   - Interest Rate
   - Term (36/60 months)
   - Grade and Sub-grade
   - Purpose

3. **Credit History**
   - Number of Credit Lines
   - Revolving Credit Balance
   - Credit Utilization
   - Recent Inquiries
   - Delinquency History

## Data Quality Considerations

### Missing Values
- Employment Length: ~3% missing
- Debt-to-Income: ~0.5% missing
- Revolving Credit Balance: ~0.1% missing

### Known Biases
1. **Selection Bias**
   - Data only includes approved loans
   - No information on rejected applications

2. **Temporal Bias**
   - Economic conditions vary across time period
   - COVID-19 period not represented

3. **Geographic Bias**
   - Over-representation of urban areas
   - State-level lending restrictions impact data availability

## Preprocessing Steps

1. **Data Cleaning**
   - Remove loans with missing FICO scores
   - Handle missing employment length with mode imputation
   - Remove loans with invalid debt-to-income ratios (>150%)

2. **Feature Engineering**
   - Credit score binning (50-point ranges)
   - Employment length categorization
   - Debt-to-income ratio bucketing
   - Purpose category consolidation

3. **Data Transformation**
   - Log transformation of income and loan amount
   - Standard scaling of numeric features
   - One-hot encoding of categorical variables

## Data Security & Privacy
- All PII (Personal Identifiable Information) removed
- ZIP codes aggregated to state level
- Income values rounded to nearest thousand
- Exact FICO scores converted to ranges

## Sampling Strategy
- Stratified sampling based on:
  1. Loan status (maintain default rate)
  2. Time period (ensure temporal representation)
  3. Loan grade (maintain risk distribution)
  4. Geographic distribution

## Data Update Frequency
- Historical data snapshot as of December 2018
- Quarterly updates for model monitoring
- Monthly performance tracking for active loans

## Usage Restrictions
- Not for commercial use
- Internal model development only
- No sharing with external parties
- Subject to Lending Club terms of service
