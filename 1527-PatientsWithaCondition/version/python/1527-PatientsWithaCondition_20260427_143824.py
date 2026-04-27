# Last updated: 2026/4/27 14:38:24
1import pandas as pd
2
3def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
4    scores['rank']=scores['score'].rank(method='dense', ascending=False)
5    return scores.loc[:,['score','rank']].sort_values('score',ascending=False)
6