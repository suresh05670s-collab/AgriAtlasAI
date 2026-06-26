import pandas as pd

# Read the Excel dataset
df = pd.read_excel("dataset/crop_data.xlsx")

# Show the first 5 rows
print(df.head())

# Show dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Clean text columns
df["State"] = df["State"].str.strip().str.title()
df["District"] = df["District"].str.strip().str.title()
df["Crop"] = df["Crop"].str.strip().str.title()
df["Season"] = df["Season"].str.strip().str.title()
df["Soil_Type"] = df["Soil_Type"].str.strip().str.title()
df["Fertility"] = df["Fertility"].str.strip().str.title()

# Save cleaned dataset
df.to_excel("dataset/cleaned_crop_data.xlsx", index=False)

print("\n✅ Cleaned dataset saved successfully!")