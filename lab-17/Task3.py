import pandas as pd
import numpy as np
data = {
    'patient_id': [1,2,3,4,5],
    'name': ['Alice','Bob','Charlie','David','Eva'],
    'gender': ['F', 'M', 'male', 'Female', 'M'],
    'age': [25, 30, np.nan, 45, 50],
    'height_cm': [160, 175, 180, np.nan, 165],
    'weight_kg': [55, 70, 80, 90, np.nan],
    'blood_pressure': [120, 130, np.nan, 140, 135],
    'heart_rate': [80, np.nan, 78, 85, 90]
}

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

numeric_cols = ['age', 'height_cm', 'weight_kg', 'blood_pressure', 'heart_rate']
for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

df['height_m'] = df['height_cm'] / 100
df.drop(columns=['height_cm'], inplace=True)  # drop old column


df['gender'] = df['gender'].replace({'M':'Male', 'male':'Male', 'F':'Female', 'Female':'Female'})


df.drop(columns=['patient_id'], inplace=True)


print("\nCleaned Healthcare Dataset:")
print(df)

df.to_csv('healthcare_data_cleaned.csv', index=False)
