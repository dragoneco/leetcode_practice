# Last updated: 2026/5/1 10:54:08
1import pandas as pd
2
3def total_time(employees: pd.DataFrame) -> pd.DataFrame:
4    employees['time']=employees.out_time-employees.in_time
5    result=employees.groupby(['emp_id','event_day'])['time'].sum().reset_index(name='total_time')
6
7
8    return result[['event_day','emp_id','total_time']].rename(columns={'event_day':'day'})