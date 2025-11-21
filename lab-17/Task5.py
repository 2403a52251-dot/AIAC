import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

data = {
    'date': pd.date_range(start='2025-01-01', periods=10, freq='D'),
    'company_name': ['AlphaCorp', 'BetaLtd', 'AlphaCorp', 'GammaInc', 'BetaLtd', 'AlphaCorp', 'GammaInc', 'AlphaCorp', 'BetaLtd', 'GammaInc'],
    'sector': ['Tech', 'Finance', 'Tech', 'Energy', 'Finance', 'Tech', 'Energy', 'Tech', 'Finance', 'Energy'],
    'stock_price': [120.5, 98.3, np.nan, 150.1, 100.2, 122.8, np.nan, 130.4, 102.7, 160.9],
    'volume': [1000, 850, 910, np.nan, 920, 1010, 890, np.nan, 870, 950]
}

df = pd.DataFrame(data)
print(" Original Dataset:")
print(df)

df['stock_price'].fillna(df['stock_price'].mean(), inplace=True)
df['volume'].fillna(df['volume'].mean(), inplace=True)

df['MA_7'] = df['stock_price'].rolling(window=7, min_periods=1).mean()
df['MA_30'] = df['stock_price'].rolling(window=3, min_periods=1).mean()  # 30-day reduced for small data

scaler = StandardScaler()
df[['stock_price_scaled', 'volume_scaled', 'MA_7_scaled', 'MA_30_scaled']] = scaler.fit_transform(
    df[['stock_price', 'volume', 'MA_7', 'MA_30']]
)

le_sector = LabelEncoder()
le_company = LabelEncoder()

df['sector_encoded'] = le_sector.fit_transform(df['sector'])
df['company_encoded'] = le_company.fit_transform(df['company_name'])

print("\n Feature-Engineered Dataset:")
print(df)

df.to_csv("financial_feature_engineered.csv", index=False)
print("\n File saved as 'financial_feature_engineered.csv'")
