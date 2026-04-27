# Last updated: 2026/4/27 00:00:06
1import pandas as pd
2
3def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
4    employees['bonus']=0
5    employees.loc[((employees['employee_id']%2==1) & (~employees['name'].str.startswith('M'))), 'bonus']=employees['salary']
6
7    return employees[['employee_id','bonus']].sort_values(by='employee_id')