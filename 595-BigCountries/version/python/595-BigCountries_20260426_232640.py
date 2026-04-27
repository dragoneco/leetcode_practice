# Last updated: 2026/4/26 23:26:40
1import pandas as pd
2
3def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
4    return tweets[tweets.content.str.len()>15][['tweet_id']]