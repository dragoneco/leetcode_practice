# Last updated: 2026/4/26 22:47:30
# return customers.loc[~customers['id'].isin(orders['customerId']), ['name']].rename(columns={'name': 'Customers'})
1import pandas as pd
2
3def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
4    df=customers[~customers['id'].isin(orders['customerId'])]
5    df=df.rename(columns={'name':'Customers'})
6
7
8    return df[['Customers']]