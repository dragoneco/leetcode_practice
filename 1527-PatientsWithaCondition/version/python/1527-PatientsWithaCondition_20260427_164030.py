# Last updated: 2026/4/27 16:40:30
1import pandas as pd
2
3def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
4    nofi=len(delivery.query('order_date==customer_pref_delivery_date'))
5    noft=len(delivery)
6    percent=round((nofi/noft*100),2)
7    return pd.DataFrame({'immediate_percentage':[percent]})