import pandas as pd

# Load the cleaned dataset
file_path = "certificates_combined_clean.csv"
df = pd.read_csv(file_path)

# Number of samples per class
samples_per_class = 1000

# Downsample each class to 1000 instances
df_balanced = df.groupby("CURRENT_ENERGY_RATING").apply(
    lambda x: x.sample(n=samples_per_class, random_state=42)
).reset_index(drop=True)

# Save the reduced dataset
df_balanced.to_csv("certificates_balanced_7k.csv", index=False)

print("Balanced dataset with 7,000 instances saved as 'certificates_balanced_7k.csv'.")
