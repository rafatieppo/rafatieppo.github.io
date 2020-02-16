--- 
title: Ordenar dados INMET
date: 2014-12-11
tags: ["R", "inmet", "meteorologia", "dados climáticos"]
draft: false
author: Rafael Tieppo 
categories: ["datascience"]
featured_image: "images/LOGO_RT.svg"
blogged: "blog"
type: "blog"
--- 

# Introdução

Em algum momento da graduação ou pós-graduação, você já trabalhou com
séries históricas de clima. No seu estudo, provavelmente você se deparou
com o desafio de organizar e analisar, arquivos que comumente atingem
10000 linhas. 

Uma das fontes mais comuns para obtenção de dados climáticos é o <a
href="http://www.inmet.gov.br" target="_blank">INMET</a>. Contudo, os
arquivos que são obtidos pelo site do INMET, não possuem uma formatação
das mais práticas (Figura 1). 

![Figura 1 - Dados importados do INMET](https://sistemasagricolas.files.wordpress.com/2014/12/inmet_fig_1.png)

Repare que para cada dia registrado duas linhas são ocupadas. Nessa
disposição de dados, dependendo do software que você utiliza, obter a
média ou realizar alguma análise, pode se tornar inviável. Além disso,
sem ordenar os dados, identificar os dias que não foram registrados é um
trabalho que onera um tempo considerável. 

Para colaborar no processamento dos dados, uma função foi desenvolvida
no sistema computacional R. Apesar de não ser uma função que oferece
resultados tão rápidos (como uma similar que poderia ser desenvolvida em
C), foi a solução mais rápida que encontrei no momento que surgiu o
problema. 

Para obter a função e inserir no seu ambiente R, além de obter as demais
instruções, acesse o link: 

<a href="https://github.com/rafatieppo/INMET_DATA_ORDER/blob/master/INMET_DATA_ORDER.r" target="_blank">https://github.com/rafatieppo/INMET_DATA_ORDER/blob/master/INMET_DATA_ORDER.r</a>

Posteriormente, para executar um exemplo do uso da função, basta
executar o código: 

```
#PASSO 1 - Para ler dados do GITHUB (local dos dados do exemplo)
library(RCurl)
#1.1
EXAMPLE <-  getURL("https://raw.githubusercontent.com/rafatieppo/INMET_DATA_ORDER/master/INMET_DATA_EXAMPLE.csv")
#1.2
EXAMPLE_DATA <- read.csv(text = EXAMPLE, sep=";")
#1.3 verifique seus dados
edit(EXAMPLE_DATA)

#obs: provavelvelmente seus dados estarão no seu computador, dessa forma
#basta usar a função "read.csv("caminho do arquivo, sep=";)"
        
#PASSO 2
#2.1 execute a função
EXAMPLE_ONELINE <- one_line(EXAMPLE_DATA)
#2.2 verifique seus dados agora
edit(EXAMPLE_ONELINE)

#PASSO 3
#3.1 Se necessário exporte seus dados
write.table(EXAMPLE_ONELINE, "EXAMPLE_DONE.csv", sep=";", col.names = TRUE, row.names = FALSE)
#============================================================
```

Se tudo correu bem, o exemplo que é formado por aproximadamente 500
linhas, foi ordenado em +- 2s. Um arquivo com 25000 linhas levará +- 25
minutos. Verifique como ficaram os dados após o uso da função: 

<a
href="https://sistemasagricolas.files.wordpress.com/2014/12/inmet_fig_2.png"><img
class="aligncenter size-large wp-image-117"
src="https://sistemasagricolas.files.wordpress.com/2014/12/inmet_fig_2.png?w=660"
alt="INMET_FIG_2" width="660" height="432" /></a>

Fique a vontade para copiar, alterar e distribuir o código.
