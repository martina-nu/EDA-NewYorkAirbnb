import pandas as pd 

df = pd.read_csv('data/raw/AB_NYC_2019.csv')

df_processed = df.copy()

# Dealing with missing values

# Droping irrelevant columns

df_processed.drop(['id','name','host_name','last_review'], axis=1, inplace=True)

# Replacing data

df_processed.reviews_per_month.fillna(0, inplace=True)

# Save processed data

df_processed.to_csv('data/processed/clean_airbnb.csv')

