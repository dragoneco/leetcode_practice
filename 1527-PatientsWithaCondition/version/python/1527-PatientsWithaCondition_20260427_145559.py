# Last updated: 2026/4/27 14:55:59
1import pandas as pd
2
3def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
4    return products.melt(id_vars=['product_id'],value_vars=['store1','store2','store3'],var_name='store',value_name='price').dropna()