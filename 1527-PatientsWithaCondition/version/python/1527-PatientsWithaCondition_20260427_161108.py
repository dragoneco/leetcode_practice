# Last updated: 2026/4/27 16:11:08
1import pandas as pd
2
3def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
4    nofcustomer=store.loc[store['amount']>500,'customer_id'].drop_duplicates()
5    return pd.DataFrame({'rich_count':[len(nofcustomer)]})
6
7
8
9
10    ##当你在创建 DataFrame 时，如果字典里的值是一个单个的数字（标量），比如 len(nofcustomer) 返回的是整数 3，Pandas 会不知道该怎么生成行索引。修复方法：只需要给这个数字套上一个列表（方括号）即可。