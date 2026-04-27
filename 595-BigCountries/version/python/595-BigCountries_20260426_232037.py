# Last updated: 2026/4/26 23:20:37
1import pandas as pd
2
3def article_views(views: pd.DataFrame) -> pd.DataFrame:
4    df=views.query("author_id==viewer_id")[['author_id']].drop_duplicates().rename(columns={'author_id':'id'})
5
6    df=df.sort_values(by='id')  ## 只有一一个columns时候也需要用by 指定一个排序的column
7
8
9    return df