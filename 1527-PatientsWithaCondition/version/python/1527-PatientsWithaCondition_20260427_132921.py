# Last updated: 2026/4/27 13:29:21
1import pandas as pd
2
3def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
4    scores['rank']=scores['score'].rank(method='dense',ascending=False)
5    result=scores[['score','rank']].sort_values('score',ascending=False)
6    return result