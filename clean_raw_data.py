import pandas as pd

# Load the dataset
file_path = "../raw-data/certificates.csv"
df = pd.read_csv(file_path, low_memory=False)

# Select relevant columns for classification
columns_to_keep = [
    "CURRENT_ENERGY_RATING",
    "POTENTIAL_ENERGY_RATING",
    "CURRENT_ENERGY_EFFICIENCY",
    "POTENTIAL_ENERGY_EFFICIENCY",
    "PROPERTY_TYPE",
    "BUILT_FORM",
    "TOTAL_FLOOR_AREA",
    "ENERGY_CONSUMPTION_CURRENT",
    "ENERGY_CONSUMPTION_POTENTIAL",
    "CO2_EMISSIONS_CURRENT",
    "CO2_EMISSIONS_POTENTIAL",
    "NUMBER_HABITABLE_ROOMS",
    "NUMBER_HEATED_ROOMS",
    "LOW_ENERGY_LIGHTING",
    "MAIN_FUEL",
    "CONSTRUCTION_AGE_BAND"
]

# Keep only selected columns
df_clean = df[columns_to_keep]

# Drop rows missing the target variable (CURRENT_ENERGY_RATING)
df_clean = df_clean.dropna(subset=["CURRENT_ENERGY_RATING"])

# Fill remaining missing values
for col in df_clean.columns:
    if pd.api.types.is_numeric_dtype(df_clean[col]):
        df_clean[col] = df_clean[col].fillna(-1)  # Placeholder for numeric fields
    else:
        df_clean[col] = df_clean[col].fillna("Unknown")  # Placeholder for categorical fields

# Export the cleaned dataset as CSV
df_clean.to_csv("certificates_clean.csv", index=False)

print("Cleaned dataset saved as 'certificates_clean.csv'. Ready for WEKA!")
