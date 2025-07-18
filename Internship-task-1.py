import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

import pandas as pd
df = pd.read_csv('/content/sales_data.csv')

df.head(10)

duplicate_rows = df[df.duplicated()]
print("Duplicate Rows:")
print(duplicate_rows)

print("DataFrame with boolean representation of nulls:")
print(df.isnull())

print("DataFrame with boolean representation of nulls:")
print(df.isnull())

print("\nNumber of null values per column:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df.head()

object_columns = df.select_dtypes(include='object').columns
for col in object_columns:
    df[col] = df[col].str.lower()
    df[col] = df[col].str.strip()
    print(f"Standardized column: {col}")

print("\nText columns standardized.")

df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

print("Converted 'sale_date' column to datetime format.")
print(df['Sale_Date'].head())
print("\nData type of 'sale_date' column after conversion:")
print(df['Sale_Date'].dtype)

df.columns = [col.lower().replace(' ', '_') for col in df.columns]

print("Columns renamed using a list comprehension:")
print(df.columns)

print("DataFrame Info (including data types):")
df.info()

print("\nData Types of each column:")
print(df.dtypes)
