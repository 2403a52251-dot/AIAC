import pandas as pd
from sklearn.preprocessing import MinMaxScaler


data = {
    'transaction_id': [1,2,3,4,5,6,7,8,9,10],
    'customer_id': [101,102,103,104,105,106,107,108,109,110],
    'transaction_date': ['2025-10-01','2025-10-03','2025-10-05','2025-11-01',
                         '2025-11-02','2025-11-03','invalid_date','2025-11-05',
                         '2025-11-06','2025-11-07'],
    'transaction_amount': [250,0,-50,450,300,500,200,0,150,600],
    'product': ['Notebook','Pen','Marker','Printer','Paper','Laptop','Mouse','Keyboard','Stapler','Desk']
}

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)


df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')


df = df.dropna(subset=['transaction_date'])


df['month_year'] = df['transaction_date'].dt.to_period('M')


df = df[df['transaction_amount'] > 0]


scaler = MinMaxScaler()
df['transaction_amount_normalized'] = scaler.fit_transform(df[['transaction_amount']])


df.reset_index(drop=True, inplace=True)


print("\nCleaned Dataset:")
print(df)



df.to_csv('sales_data_cleaned.csv', index=False)
