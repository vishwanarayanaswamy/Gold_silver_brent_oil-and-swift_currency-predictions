import pandas as pd

# Load dataset
gold = pd.read_csv("Datasets/Gold 100years (1).csv")

print("Original Dataset")
print(gold.head())

# Convert Date column to datetime
gold["Date"] = pd.to_datetime(gold["Date"], format="%d/%m/%Y")

# Sort by date
gold = gold.sort_values("Date")

# Check missing values
print("\nMissing Values")
print(gold.isnull().sum())

# Rename columns for Prophet
gold = gold.rename(columns={
    "Date": "ds",
    "Value": "y"
})

print("\nCleaned Dataset")
print(gold.head())

# Save cleaned dataset
gold.to_csv("Datasets/Gold_Clean.csv", index=False)

print("\nDataset cleaned successfully!")