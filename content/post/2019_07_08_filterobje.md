---
title: "Filtering objects from a workdir"
date: 2019-07-08
comments: true
excerpt: "Learning python, how to filter"
categories: [datascience]
tags: ["python", "filter", "datascience"]
toc: true
blogged: "blog"
type: "blog"
---

## Introduction

Usually, if you work with in data science field, you need to create
several objects, like `list`, `DataFrame`, `matrix`, etc. Besides, you
have to handle some files to read and make copies. For that and other
actions, sometime you have to select some objects from your `workdir`.

The goal in this post is to show some options about how to filter
objects from your `workdir`.

## Listing and Filtering your objects

There are several options to list the objects from a `workdir`. We will
use the packages `os` and `glob`.

First of all, load the packages:

```python
import os
import glob
```

You can check your workdir:


```python
# check workdir
os.getcwd()
```
or se your workdir:

```python
# set your workdir
os.chdir('/home/rafa//1710_SR_EVAPO/1807_G/')
```

If you want see all files in your `workdir`:

```python
>>> os.listdir()
['CORR_TEST_fm940glt.png', 'ET_Fev_Maio_Agosto_OK.xlsm', 'T_sup_Fev_Maio_Agosto_OK.xlsm', 'H_final_Fev_Maio_Agosto_OK.xlsm', 'variveisdissertao.zip', '.#DATA_TIDY.py', 'Saldo_24h_Fev_Maio_Agosto_OK.xlsm', 'CORR_TEST_tmg43ws.png', 'Saldo_inst_Fev_Maio_Agosto_ok.xlsm', 'Fluxo_calor_solo_Fev_Maio_Agosto_OK.xlsm', 'Calor_latente_Fev_Maio_Agosto_ok.xlsm', 'DATA_TIDY.py', 'NDVI_Fev_Maio_Agosto_OK.xlsm', 'Albedo_Fev_Maio_Agosto_OK.xlsm', 'DATA_ANALYSIS.py', 'IAF_Fev_Maio_Agosto_OK.xlsm']
```

If you want all `xlsm` files in your `workdir`, one option is:

```python
>>> glob.glob('*.xlsm')
['ET_Fev_Maio_Agosto_OK.xlsm', 'T_sup_Fev_Maio_Agosto_OK.xlsm', 'H_final_Fev_Maio_Agosto_OK.xlsm', 'Saldo_24h_Fev_Maio_Agosto_OK.xlsm', 'Saldo_inst_Fev_Maio_Agosto_ok.xlsm', 'Fluxo_calor_solo_Fev_Maio_Agosto_OK.xlsm', 'Calor_latente_Fev_Maio_Agosto_ok.xlsm', 'NDVI_Fev_Maio_Agosto_OK.xlsm', 'Albedo_Fev_Maio_Agosto_OK.xlsm', 'IAF_Fev_Maio_Agosto_OK.xlsm']
```

Let's suppose that you need to filter all `.xlsm` files that has `T_`
in the name:

```python
>>> res = list(filter(lambda k: 'T_' in k, lst_xlsm))
>>> print(res)
['ET_Fev_Maio_Agosto_OK.xlsm', 'T_sup_Fev_Maio_Agosto_OK.xlsm']
```

If, just in case, you want to filter all `.xlsm` files that has NO `T_`
in the name (*note the* `not`):

```python
lst_xlsm = glob.glob('*.xlsm')
>>> res = list(filter(lambda k: not 'T_' in k, lst_xlsm))
>>> print(res)
['H_final_Fev_Maio_Agosto_OK.xlsm', 'Saldo_24h_Fev_Maio_Agosto_OK.xlsm', 'Saldo_inst_Fev_Maio_Agosto_ok.xlsm', 'Fluxo_calor_solo_Fev_Maio_Agosto_OK.xlsm', 'Calor_latente_Fev_Maio_Agosto_ok.xlsm', 'NDVI_Fev_Maio_Agosto_OK.xlsm', 'Albedo_Fev_Maio_Agosto_OK.xlsm', 'IAF_Fev_Maio_Agosto_OK.xlsm']
```

Another usual case in data science a list of objects to filter. If you
use `dir()` you get all your environment content:

```python
>>> dir()
['__PYTHON_EL_native_completion_setup', '__annotations__', '__builtins__', '__code', '__doc__', '__loader__', '__name__', '__package__', '__pyfile', '__spec__', 'codecs', 'df_ET', 'df_ETaug', 'df_ETfev', 'df_ETmay', 'df_H', 'df_HEATFLOW', 'df_HEATFLOWaug', 'df_HEATFLOWfev', 'df_HEATFLOWmay', 'df_Haug', 'df_Hfev', 'df_Hmay', 'df_IAF', 'df_IAFaug', 'df_IAFfev', 'df_IAFmay', 'df_LE', 'df_LEaug', 'df_LEfev', 'df_LEmay', 'df_RN24', 'df_RN24aug', 'df_RN24fev', 'df_RN24may', 'df_RNins', 'df_RNinsaug', 'df_RNinsfev', 'df_RNinsmay', 'df_TsupK', 'df_TsupKaug', 'df_TsupKfev', 'df_TsupKmay', 'df_albaug', 'df_albedo', 'df_albfev', 'df_albmay', 'df_fulldata1807G', 'df_fullfm940glt', 'df_fullfm940glt_pivot', 'df_fulltmg43ws', 'df_fulltmg43ws_pivot', 'glob', 'lst_xlsm', 'np', 'os', 'pd', 'res']
```

If you need to get all objects with `df_` in the begin:

```python
>>> lst_ob = dir()
>>> res = [k for k in lst_ob if 'df_' in k]
>>> print(res)
['df_ET', 'df_ETaug', 'df_ETfev', 'df_ETmay', 'df_H', 'df_HEATFLOW', 'df_HEATFLOWaug', 'df_HEATFLOWfev', 'df_HEATFLOWmay', 'df_Haug', 'df_Hfev', 'df_Hmay', 'df_IAF', 'df_IAFaug', 'df_IAFfev', 'df_IAFmay', 'df_LE', 'df_LEaug', 'df_LEfev', 'df_LEmay', 'df_RN24', 'df_RN24aug', 'df_RN24fev', 'df_RN24may', 'df_RNins', 'df_RNinsaug', 'df_RNinsfev', 'df_RNinsmay', 'df_TsupK', 'df_TsupKaug', 'df_TsupKfev', 'df_TsupKmay', 'df_albaug', 'df_albedo', 'df_albfev', 'df_albmay', 'df_fulldata1807G', 'df_fullfm940glt', 'df_fullfm940glt_pivot', 'df_fulltmg43ws', 'df_fulltmg43ws_pivot']
```

## Conclusion

If you keep organized the files names and the objects names you can filter
them easily. We only showed some options to filter lists. You can create
more ways to achieve the same result. Let me know you know another one.

Best regards

## References

[stackoverflow](https://stackoverflow.com/questions/2152898/filtering-a-list-of-strings-based-on-contents)

[eli-bendersky](https://stackoverflow.com/users/8206/eli-bendersky)

[itay-maman](https://stackoverflow.com/users/27198/itay-maman)
