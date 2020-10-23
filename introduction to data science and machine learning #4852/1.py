import pandas as pd
import numpy as np


d = {'type': ['A', 'A', 'B', 'B'], 'value': [10, 14, 12, 23]}
my_data = pd.DataFrame(data=d)
   

subset_1 = my_stat.iloc[0:10, 0:3:2]
subset_2 = my_stat.iloc[1:4, 1:4:2].append(my_stat.iloc[5:, 1:4:2])


subset_1 = my_stat.query("V1 > 0 & V3 == 'A'")
subset_2 = my_stat.query("V2 != 10 | V4 >= 1.0")


my_stat['V5'] = my_stat.V1 + my_stat.V4
my_stat['V6'] = np.log(my_stat.V2)


my_stat = my_stat.rename(index=str, 
                         columns={"V1": "session_value", 
                                  "V2": "group", 
                                  "V3": "time", 
                                  "V4": "n_users"})


my_stat['session_value'] = my_stat['session_value'].fillna(0)
med = my_stat.query("n_users >= 0")['n_users'].median()
my_stat.loc[my_stat['n_users'] < 0, ['n_users']] = med


mean_session_value_data = my_stat.groupby('group', as_index = False)
                                 .agg({'session_value': 'mean'})
                                 .rename(index=str, columns={'session_value': 'mean_session_value'})
