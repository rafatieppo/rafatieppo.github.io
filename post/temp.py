

import numpy as np
import pandas as pd

dic = {'Mary': '1235'}

try:
    V = dic['some']
except KeyError:
    V = 'error'
V

V = dic.get('Mary')
V


V = dic.get('some', -99)
V

a, b, c, d = 10, 20, 30, 40


cond2 = [
    a == 910,
    b == 920,
    c == 930,
    d == 40]


if all(cond1):
    print('All is true')

if any(cond2):
    print('one is true at least')


DF = pd.DataFrame({"MONTH": np.repeat(['Jan', 'Fev', 'Mar'], 3),
                   "SELLER": np.tile(['Max', 'Ted', 'Saul'], 3),
                   "CARSOLD": [6, 4, 5, 2, 4, 4, 2, 3, 3],
                   "PROFIT": [0.3, 0.2, 0.2, 0.4, 0.2, 0.1, 0.25, 0.3, 0.3]})
DF

>> > cond3 = [
    (DF['MONTH'] == 'Mar'),
    (DF['CARSOLD'] >= 3) & (DF['PROFIT'] >= 0.25)]

cond3 = [
    (DF['MONTH'] == 'Mar') & (DF['CARSOLD'] >= 3) & (DF['PROFIT'] >= 0.25),
    (DF['MONTH'] == 'Mar') & (DF['CARSOLD'] < 3) & (DF['PROFIT'] < 0.25)
]
choices = ['reward', 'regular']
DF['RESULT'] = np.select(cond3, choices, 'nomatch')
DF

np.sel


l1 = [1, 2, 3]

# a math operation

l1_new = []
for x in l1:
    l1_new.append(x + 1)
l1_new

l1_new = [x + 1 for x in l1]
l1_new

# diif


df = pd.DataFrame({"DAY": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   "RAIN": [6, 0, 0, 20, 30, 40, 0, 0, 10, 15]})
df['RAIN'].cumsum()


df['RAIN'].diff()[1:]

df

df['RAIN'].rolling(2).mean()

for i in range(1, len(df)):
    cc = df['RAIN'].iloc[i-1:i+1].mean()
    print(cc)


df
df['RAIN'].iloc[i-1:2].mean()

arr = np.empty(shape=(3, 5))
arr[:] = np.NaN
arr

x = 7


df_a = pd.DataFrame({'NAME': ['Joe', 'Mary', 'Paul'],
                     'AGE': [25, 35, 46]})
df_b = df_a.copy()
df_a
df_b
df_a.iloc[2, 1] = 99


arr = np.empty(shape=(3, 5))
arr[:] = np.NaN
arr

arr[0] = np.random.randint(0, 20, 5)
arr[1] = np.random.randint(0, 20, 5)
arr[2] = np.random.randint(0, 20, 5)
arr.mean(axis=0)
arr.mean(axis=1)
