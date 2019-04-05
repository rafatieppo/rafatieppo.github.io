--- 
title: Converter lista com data.frame(s) em um data.frame
date: 2017-05-10
tags: ["R", "list", "dataframe", "csv"]
draft: false
author: Rafael Tieppo 
categories: ["R"]
featured_image: "images/FOS_teaser.png"
blogged: "blog"
--- 

# Introdução

Trabalhando com banco de dados, em algum momento torna-se necessária a
extração de determininados elementos que satisfaçam um dada condição. Na
linguagem **R**, uma das opções de se realizar esta operação é a
utilização de *listas*.

# Estudo de caso

Vamos supor que você tenha um `data.frame` com três tratamentos e quatro
repetições 

```
DF <-
    data.frame(BLOCO = rep(seq(1,4), each = 12),
               TRAT=rep(c("T1", "T2", "T3"), each = 4),
               REP = seq(1,4),
               Z = rnorm(48, 30, 2.6))

head(DF)
>
##   BLOCO TRAT REP        Z
## 1     1   T1   1 27.34090
## 2     1   T1   2 30.36415
## 3     1   T1   3 31.35214
## 4     1   T1   4 25.11936
## 5     1   T2   1 29.22582
## 6     1   T2   2 29.71030
```

Uma vez que o `data.frame` foi criado, vamos supor que seja
necessário separar para cada bloco, os valores de cada tratamento entre
as repetições 2 e 3. Para isto podemos criar uma lista de `data.frames`.


```
LISTOFDATAFRAME  <- vector(mode = "list", length = 4)

k=1
for (b in (1:4)) ### from block 1 up to 4
    {    
        LISTOFDATAFRAME[[k]] <-
            sapply(c("T1", "T2", "T3"),
                   function(n)
                       subset(DF,
                              BLOCO == b &
                              TRAT == n)[2:3,],
                   simplify = FALSE)
        k = k+1
        }

### Repare que para entrada da lista há um bloco com os tratamentos
### "T1", "T2", "T3" e suas respectivas repetições 2 e 3:

head(LISTOFDATAFRAME)
>
## [[1]]
## [[1]]$T1
##   BLOCO TRAT REP        Z
## 2     1   T1   2 30.36415
## 3     1   T1   3 31.35214
## 
## [[1]]$T2
##   BLOCO TRAT REP        Z
## 6     1   T2   2 29.71030
## 7     1   T2   3 33.59699
## 
## [[1]]$T3
##    BLOCO TRAT REP        Z
## 10     1   T3   2 28.72656
## 11     1   T3   3 29.71134
## 
## 
## [[2]]
## [[2]]$T1
##    BLOCO TRAT REP        Z
## 14     2   T1   2 34.55354
## 15     2   T1   3 29.69425
## 
## [[2]]$T2
##    BLOCO TRAT REP        Z
## 18     2   T2   2 27.48108
## 19     2   T2   3 31.22254
## 
## [[2]]$T3
##    BLOCO TRAT REP        Z
## 22     2   T3   2 30.16999
## 23     2   T3   3 25.35998
## 
## 
## [[3]]
## [[3]]$T1
##    BLOCO TRAT REP        Z
## 26     3   T1   2 27.03317
## 27     3   T1   3 30.34640
## 
## [[3]]$T2
##    BLOCO TRAT REP        Z
## 30     3   T2   2 21.11056
## 31     3   T2   3 32.07944
## 
## [[3]]$T3
##    BLOCO TRAT REP        Z
## 34     3   T3   2 30.83631
## 35     3   T3   3 30.51380
## 
## 
## [[4]]
## [[4]]$T1
##    BLOCO TRAT REP        Z
## 38     4   T1   2 31.63475
## 39     4   T1   3 31.88315
## 
## [[4]]$T2
##    BLOCO TRAT REP        Z
## 42     4   T2   2 26.45181
## 43     4   T2   3 31.26221
## 
## [[4]]$T3
##    BLOCO TRAT REP        Z
## 46     4   T3   2 28.85554
## 47     4   T3   3 31.30958
```

Para unir a lista em um novo `data.frame` há pelo menos duas opções:



```
### Primeira opçção:

df1 <-
    sapply(1:3, function(w)
        do.call(rbind, LISTOFDATAFRAME[[w]]),
        simplify = FALSE) 

df1 <-
    do.call(rbind, df1)
df1
>
##       BLOCO TRAT REP        Z
## T1.2      1   T1   2 30.36415
## T1.3      1   T1   3 31.35214
## T2.6      1   T2   2 29.71030
## T2.7      1   T2   3 33.59699
## T3.10     1   T3   2 28.72656
## T3.11     1   T3   3 29.71134
## T1.14     2   T1   2 34.55354
## T1.15     2   T1   3 29.69425
## T2.18     2   T2   2 27.48108
## T2.19     2   T2   3 31.22254
## T3.22     2   T3   2 30.16999
## T3.23     2   T3   3 25.35998
## T1.26     3   T1   2 27.03317
## T1.27     3   T1   3 30.34640
## T2.30     3   T2   2 21.11056
## T2.31     3   T2   3 32.07944
## T3.34     3   T3   2 30.83631
## T3.35     3   T3   3 30.51380
```

```
### Segunda opção, pacote dplyr
#library(dplyr)

df2 <- do.call("bind_rows", LISTOFDATAFRAME)
df2
>
##    BLOCO TRAT REP        Z
## 1      1   T1   2 30.36415
## 2      1   T1   3 31.35214
## 3      1   T2   2 29.71030
## 4      1   T2   3 33.59699
## 5      1   T3   2 28.72656
## 6      1   T3   3 29.71134
## 7      2   T1   2 34.55354
## 8      2   T1   3 29.69425
## 9      2   T2   2 27.48108
## 10     2   T2   3 31.22254
## 11     2   T3   2 30.16999
## 12     2   T3   3 25.35998
## 13     3   T1   2 27.03317
## 14     3   T1   3 30.34640
## 15     3   T2   2 21.11056
## 16     3   T2   3 32.07944
## 17     3   T3   2 30.83631
## 18     3   T3   3 30.51380
## 19     4   T1   2 31.63475
## 20     4   T1   3 31.88315
## 21     4   T2   2 26.45181
## 22     4   T2   3 31.26221
## 23     4   T3   2 28.85554
## 24     4   T3   3 31.30958
```

Ambas as soluções retornam um `data.frame` com os dados
selecionados. Dependendo do tamanho do banco de dados pode haver
diferença de tempo no processamento, maiores detalhes podem ser
encontrados nas referências.

>Sem dados você é apenas mais uma pessoa com uma opinião.
>*W. Edwards Deming (1900-1993)*

## Referências

[Convert a list of data frames into one data frame](http://stackoverflow.com/questions/2851327/convert-a-list-of-data-frames-into-one-data-frame)
[Concatenating a list of data frames](https://www.r-bloggers.com/concatenating-a-list-of-data-frames/)


