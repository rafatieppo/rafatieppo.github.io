---
title: "Julian date with python 3"
date: 2018-12-01
comments: true
excerpt: "to convert julian date to standard date and vice versa"
categories: [datascience]
tags: ["python", "datetime", "meteorology", "tidy"]
toc: true
blogged: "blog"
---

## Introduction

The work in data science must be tidy. A simple file name can help you
to save a lot of time. For instance, if you have a series of satellite
images from LANDSAT 8, the files are ordered by Julian date:

```
rt@rt-d5567:~/Documents/$ find -name '*305*.TIF'
./LO82280702018305CUB00_B3.TIF
./LO82280702018305CUB00_B9.TIF
./LO82280702018305CUB00_B5.TIF
```

If you did not realize, note that after `2018` there are three numbers
`305`. The number `305` means the 305<sup>th</sup> day of the year. If
we join `2018` and `305`, we get `2018305` (305<sup>th</sup> day of 2018
year). It is the same of `2018-11-01` (standard date: year, month, day).

Another user of Julian date is in meteorology. Usually the data are
organized by Julian date:

Table 1: Climate date table

| year | jday | temperature |  ur |
|------|------|-------------|-----|
| 2017 |   55 |          23 |  70 |
| 2017 |   56 |          22 |  74 |
|  ... |  ... |         ... | ... |
| 2018 |   55 |          26 |  68 |
| 2018 |   56 |          25 |  71 |
|  ... |  ... |         ... | ... |

The idea in this post is to provide a simple code to extract day of year
and Julian day from a string date in python. 

## From standard Date to Julian date

Once your date is in `datetime` format, just convert to `timetuple`,
as follows:

```python
import datetime

def datestdtojd (stddate):
    fmt='%Y-%m-%d'
    sdtdate = datetime.datetime.strptime(stddate, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday
    return(jdate)
```
Let's suppose that you would like to know the Julian date
for **2018-11-01**. Running the code: 

```python
>>> datestdtojd('2018-11-01')
305
```
It means 305<sup>th</sup> day of 2018.

## From Julian date to standard Date

```python
def jdtodatestd (jdate):
    fmt = '%Y%j'
    datestd = datetime.datetime.strptime(jdate, fmt).date()
    return(datestd)
```
If you need to know month and day for the 305<sup>th</sup> of 2018.

```python
>>> jdtodatestd('2018305')
datetime.date(2018, 11, 1)
```

## Conclusion

Julian date is pretty handy to tidy files and data bank. Thus some
functions are important to manage transformation from one to another
format. 

Let me know you have some question.


## References

- [abarnert](https://stackoverflow.com/questions/13943062/extract-day-of-year-and-julian-day-from-a-string-date-in-python)
- [Brendan Abel](https://stackoverflow.com/questions/37743940/python3-convert-julian-date-to-standard-date)

