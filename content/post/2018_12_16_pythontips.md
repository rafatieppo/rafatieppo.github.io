---
title: "Python beginner tips"
date: 2018-12-16
comments: true
excerpt: "Learning python, begginer level"
categories: [datascience]
tags: ["python", "tips", "datascience"]
toc: true
blogged: "blog"
---

## Introduction

I spent around 4 years working with R, and I can say that R is
amazing. However, I decided to start a new stage in my professional
life, and a need came, a multi proposal language. My option was
**Python**, because It provides have data science tools, and has a huge support
for others applications. 

After some months, studying in my free time, I would like to share some
code that I learned (from several sources). Moreover, to write a blog is
a way to improve my learning. 

## Getting values from dictionary
 
```python
>>> dic = {'Mary': '1235'}
>>> try:
        V = dic['some']
    except KeyError:
        V = 'error'
>>> V
'error'
```

Instead, You can try it

```python
>>> V = dic.get('Mary')
>>> V
'1235'
```

Or for a second parameter:

```python
>>> V = dic.get('some', -99)
>>> V
-99
```

## Conditional


**For some values**

```python
>>> a, b, c, d = 10, 20, 30, 40
>>> if a == 10 and b == 20 and c == 30 and d == 40:
        print('all True!')
>>> all True!

```

We can simplify, let's try:

```python
>>> cond1 = [a == 10,
             b == 20,
             c == 30,
             d == 40]

>>> if all(cond1):
       print('All is true')
>>> All is true

# if we change the conditions

cond2 = [
    a == 910,
    b == 920,
    c == 930,
    d == 40]

>>> if any(cond2):
    print('one is true at least')
>>> one is true at least

```

A more complex example. For instance you have cars sells, for 3 sellers
in 3 months. You would like to know for *March* what seller achieved the
goal. The goal is more than 3 cars in march and a profit greater than
0.25.

```python

# import packs
>>> import pandas as pd
>>> import numpy as np
# data frame
>>> DF = pd.DataFrame({"MONTH": np.repeat(['Jan', 'Fev', 'Mar'], 3),
        "SELLER": np.tile(['Max', 'Ted', 'Saul'], 3),
        "CARSOLD": [6, 4, 5, 2, 4, 4, 2, 3, 3],
        "PROFIT": [0.3, 0.2, 0.2, 0.4, 0.2, 0.1, 0.25, 0.3, 0.3]})

>>> DF
  MONTH SELLER  CARSOLD  PROFIT
0   Jan    Max        6    0.30
1   Jan    Ted        4    0.20
2   Jan   Saul        5    0.20
3   Fev    Max        2    0.40
4   Fev    Ted        4    0.20
5   Fev   Saul        4    0.10
6   Mar    Max        2    0.25
7   Mar    Ted        3    0.30
8   Mar   Saul        3    0.30

# numpy can help us 
# condition
>>> cond3 = [
    (DF['MONTH'] == 'Mar') & (DF['CARSOLD'] >= 3) & (DF['PROFIT'] >= 0.25),
    (DF['MONTH'] == 'Mar') & (DF['CARSOLD'] < 3) & (DF['PROFIT'] < 0.25)
    ]
>>> choices = ['reward', 'regular']
# running, note that np.select provide a standard value 'nomatch' 
>>> DF['RESULT'] = np.select(cond3, choices, 'nomatch')

>>> DF
  MONTH SELLER  CARSOLD  PROFIT   RESULT
0   Jan    Max        6    0.30  nomatch
1   Jan    Ted        4    0.20  nomatch
2   Jan   Saul        5    0.20  nomatch
3   Fev    Max        2    0.40  nomatch
4   Fev    Ted        4    0.20  nomatch
5   Fev   Saul        4    0.10  nomatch
6   Mar    Max        2    0.25  nomatch
7   Mar    Ted        3    0.30   reward
8   Mar   Saul        3    0.30   reward

```

## Loop

Usually:

```python
>>> l1 = [1, 2, 3]

# a math operation
>>> l1_new = []
>>> for x in l1:
        l1_new.append(x + 1)
>>> l1_new
[2, 3, 4]
```

All in one line:

```python
>>> l1_new  = [x + 1 for x in l1]
>>> l1_new
[2, 3, 4]
```

## Functions in one line

When We need to replace a value in a list, we can use several tools, but
now, We want use a function. If We have a list with some letters, and We
need to replace by numbers:

- x = 0

```python
>>> l2 = ['x', 'y', 'y', 'z', 'a', 'b']

# function

>>> def replace_value(alist):
        new_list = []
        for i in alist:
            if i == 'x':
                new_list.append(0)
            else:
                new_list.append(i)
        return(new_list)

>>> replace_value(l2)
[0, 'y', 'y', 'z', 'a', 'b']

```

We can decrease the code size:

```python

# function
>>> def replace_v(i):
        if i == 'x':
            return 0
        return i

>>> l2_new = []
>>> for i in l2:
        l2_new.append(replace_v(i))

>>> l2_new
[0, 'y', 'y', 'z', 'a', 'b']
```

A little bit smaller:

```python
# function
>>> repl = lambda i: 0 if i == 'x' else i

>>> l2_new = []
>>> for i in l2:
        l2_new.append(repl(i))
>>> l2_new
[0, 'y', 'y', 'z', 'a', 'b']
```

# Conclusion

Python provides several ways to do the same thing. In my opinion, at the begin, you should not worry about
the size of your code. First of all, your code must work correctly,
after that you can think about processing speed, and for last one
action, you can think about the size of your code. 

