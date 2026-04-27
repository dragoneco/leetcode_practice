# Last updated: 2026/4/26 22:30:08
# query里面 的 变量名称 不需要加引号，但是整个的代码需要加双引号。
1import pandas as pd
2
3def find_products(products: pd.DataFrame) -> pd.DataFrame:
4    return products.query("low_fats=='Y'  and recyclable=='Y'")[['product_id']]