# Lending Club Credit Risk Model - Development Artifacts

This repository contains the development artifacts for the Lending Club credit risk model, prepared for MRM review.

## Repository Structure

```
.
├── src/
│   ├── notebooks/
│   │   └── lending_club_model_development.ipynb  # Main development notebook
│   ├── data/
│   │   ├── lending_club_raw_data.csv            # Original data (300 samples)
│   │   ├── lending_club_golden_data.csv         # Processed data with engineered features
│   │   └── data_sample_metadata.md              # Documentation of data transformations
```

## Development Artifacts

### 1. Model Development Notebook
`src/notebooks/lending_club_model_development.ipynb`
- Data exploration and analysis
- Feature engineering implementation
- Model training process
- Performance evaluation
- All code used in development

### 2. Data Files
- **Raw Data**: `src/data/lending_club_raw_data.csv`
  * Original Lending Club loan data
  * 300 samples for POC
  * Contains base features

- **Processed Data**: `src/data/lending_club_golden_data.csv`
  * Engineered features added
  * Ready for model training
  * Includes all transformations

### 3. Data Transformation Documentation
`src/data/data_sample_metadata.md`
- Detailed documentation of data processing steps
- Feature engineering explanations
- Data quality checks
- Transformation rationale

## Contact

For questions about the model development:
- Model Development Team
