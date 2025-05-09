import pandas as pd
import os

# Path to the folder where all 7 files are stored
data_folder = "../raw-data-ratings/"

# Expected filenames (modify if needed)
files = [
    "certificates_A.csv",
    "certificates_B.csv",
    "certificates_C.csv",
    "certificates_D.csv",
    "certificates_E.csv",
    "certificates_F.csv",
    "certificates_G.csv"
]

# Columns to keep
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
    "CONSTRUCTION_AGE_BAND",
    "POSTCODE"
]

# Load and combine datasets
dfs = []
for file in files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path, low_memory=False)
    dfs.append(df)

# Concatenate all datasets
combined_df = pd.concat(dfs, ignore_index=True)

# Keep only selected columns
df_clean = combined_df[columns_to_keep]

# Drop rows missing the target variable (CURRENT_ENERGY_RATING)
df_clean = df_clean.dropna(subset=["CURRENT_ENERGY_RATING"])

# Fill remaining missing values appropriately
for col in df_clean.columns:
    if pd.api.types.is_numeric_dtype(df_clean[col]):
        df_clean[col] = df_clean[col].fillna(-1)  # Placeholder for numeric fields
    else:
        df_clean[col] = df_clean[col].fillna("Unknown")  # Placeholder for categorical fields

# Export the final cleaned dataset
df_clean.to_csv("certificates_combined_clean.csv", index=False)

print("Final cleaned dataset saved as 'certificates_combined_clean.csv'.")
