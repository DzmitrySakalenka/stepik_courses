import pandas as pd
import numpy as np


print(pd.__version__)


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data=data, index=labels)
print(df)


print(df[input()][input()])


print(df.describe()['age']['count'])
print(df.describe()['age']['75%'])


print(df.head(3))


print(df.iloc[[0, 2, 3]])


print(df[['name', 'age']])


print(df[['name', 'age']].iloc[[0, 2, 3]])


critical_age = 3
print(df[df.age > critical_age])


print(df[df.age.isnull()])