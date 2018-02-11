---
title: "Reading and storing several files at one step"
date: 2017-05-08
excerpt: ""
categories:
  - R
tags:
  - R
  - lists
toc: true
---

## Introduction

Usually we need to read several files to create a data bank (data frame
with all data). If you have two or three files it is simple. However, if
you have five or more files like `.csv`, `.dat`, etc, it can demand more
time. One of the options to solve it using R is possibility to work with
*lists*. 

## Case I

Vamos supor que você tenha uma série de arquivos no formato `.csv`
Supposing you have `.csv` files.


```r
### Criando um data.frame hipotético
DF <-
    data.frame(BLOCO = rep(seq(1,4), each = 12),
               TRAT=rep(c("T1", "T2", "T3"), each = 4),
               REP = seq(1,4),
               Z = rnorm(48, 30, 2.6))
head(DF)
```

```
##   BLOCO TRAT REP        Z
## 1     1   T1   1 30.50221
## 2     1   T1   2 30.11910
## 3     1   T1   3 27.47513
## 4     1   T1   4 30.58861
## 5     1   T2   1 30.31546
## 6     1   T2   2 28.90498
```

```r
### Gerando uma série de arquivos csv
sapply(c("foo1.csv", "foo2.csv", "foo3.csv", "foo4.csv", "foo5.csv"),
       function(i){
       write.csv(DF, paste(i))})
```

```
## $foo1.csv
## NULL
## 
## $foo2.csv
## NULL
## 
## $foo3.csv
## NULL
## 
## $foo4.csv
## NULL
## 
## $foo5.csv
## NULL
```

```r
### Verifique se os arquivos .csv foram criados
dir()
```

```
## [1] "170514_READING_FILES.md"  "170514_READING_FILES.Rmd"
## [3] "foo1.csv"                 "foo2.csv"                
## [5] "foo3.csv"                 "foo4.csv"                
## [7] "foo5.csv"
```

```r
### Lendo os nomes dos arquivos .csv
temp = list.files(pattern="*.csv")
temp
```

```
## [1] "foo1.csv" "foo2.csv" "foo3.csv" "foo4.csv" "foo5.csv"
```

```r
### Gerando uma lista com os arquivos .csv

DF_LIST <-
    lapply(seq(1, length(temp)),
           function(z)
               read.csv(temp[z],
                        header = TRUE,
                        dec = ".",
                        sep = ","))

### Agrupando em um único data.frame
DF_LIST_agrup <-
    do.call(rbind.data.frame, DF_LIST)

head(DF_LIST_agrup)
```

```
##   X BLOCO TRAT REP        Z
## 1 1     1   T1   1 30.50221
## 2 2     1   T1   2 30.11910
## 3 3     1   T1   3 27.47513
## 4 4     1   T1   4 30.58861
## 5 5     1   T2   1 30.31546
## 6 6     1   T2   2 28.90498
```

```r
dim(DF_LIST_agrup)
```

```
## [1] 240   5
```

## Estudo de caso II 

Quando se tem arquivos `.xls` ou `.xlsx` pode-se utilizar o pacote
`readxl`.


```r
#library(readxl)

DF1 <- 
read_excel("NOME_DO_ARQUIVO.xlsx")
```
Caso seja necessário ler uma pasta específica do seu arquivo `.xls` ou
`xlxs` basta usar as opções da função.


```r
#library(readxl)

DF2 <-
    read_excel("NOME_DO_ARQUIVO.xlsx",
               sheet = "NOME_DA_PASTA")
```

## Estudo de caso III

Se seu arquivo `.xls` ou `xlxs` tiver uma série de pastas, basta usar a
mesma lógica do **Estudo de caso I**.


```r
#library(readxl)

LISTA_PASTAS <- c("PASTA1",
                  "PASTA2",
                  "PASTA3")

### Lendo as pastas do arquivo  "NOME_DO_ARQUIVO.xlsx"

DF3_LISTA <-
    sapply(LISTA_PASTAS,
           function(L){
               read_excel("NOME_DO_ARQUIVO.xlsx",
                          sheet = L)
               },
           simplify = FALSE)

### DB ACCOUNT
DF3_DF <- do.call(rbind.data.frame, DF3_LISTA)
```

Para maiores detalhes sobre ler os dados de arquivos `.xls` ou `.xlsx`
consulte as referências.

[]


>“Without data, you're just another person with an opinion.”
>* W. Edwards Deming*


## Referências

[Convert a list of data frames into one data frame](http://stackoverflow.com/questions/2851327/convert-a-list-of-data-frames-into-one-data-frame)
[Concatenating a list of data frames](https://www.r-bloggers.com/concatenating-a-list-of-data-frames/)
[readxl](http://readxl.tidyverse.org/)







