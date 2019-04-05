---
title: "lucyLattes um script para manipular dados da plataforma Lattes"
date: 2019-03-13
comments: true
excerpt: "aprendendo python"
categories: [datascience]
tags: ["python", "lucyLattes", "datascience"]
toc: true
blogged: "blog"
---

## Introdução

Historicamente o [CNPq](http://www.cnpq.br/) gerencia uma base dados
sobre pesquisadores em C&T para diversos fins, cita-se como exemplo a
avaliação de programas de pós-graduação, seleção de bolsas para
pesquisadores, entre outros. Esta base dados é denominada [Plataforma
Lattes](http://lattes.cnpq.br/).

Devido esta referida plataforma ser amplamente utilizada, tornou-se
padrão em universidades, órgãos de pesquisa, etc. Nesta plataforma é
possível encontrar desde a formação acadêmica do profissional, as
empresas que trabalhou, até sua produção científica, e artística, etc.

O que deixava o uso do [Currículo
Lattes](http://buscatextual.cnpq.br/buscatextual/busca.do?metodo=apresentar)
tedioso era a extração dos dados, pois usualmente era manual, o que
consequentemente torna o trabalho massante. Contudo, tudo mudou com
[scriptLattes](http://scriptlattes.sourceforge.net/). Este script
GNU-GPL realiza a extração e compilação automática de: produções
bibliográficas, técnicas,artísticas, orientações, projetos de pesquisa,
etc, de um conjunto de pesquisadores cadastrados na plataforma Lattes.

Todavia, com a implementação do captcha (código de segurança), a
utilização do [scriptLattes](http://scriptlattes.sourceforge.net/) foi
impossibilitada, [veja
aqui](http://revistas.iel.unicamp.br/index.php/edicc/article/view/5208). 

Devido à necessidade estudar o panorama de um grupo de profissionais, e
para contornar a impossibilidade do uso do
[scriptLattes](http://scriptlattes.sourceforge.net/), o
[lucyLattes](https://github.com/rafatieppo/lucyLattes) foi
desenvolvido. 

O [lucyLattes](https://github.com/rafatieppo/lucyLattes) é um script em
[python](https://www.python.org/), que faz a extração, a compilação, 
a organização dos dados dos currículos da plataforma Lattes em arquivos de
texto, e a geração de um relatório simplificado, que proporcionam
agilidade para a geração de informação. O inconveniente é ter que fazer
o download dos arquivos `.xml` dos Currículo *Lattes* a serem
analisados.

Caso você esteja se perguntando o porquê do nome `lucyLattes`, a
resposta é simples. Como o nome mais obvio, que seria `scriptLattes`, já
está em uso, parei para pensar e olhei para o lado, e encontrando a Lucy
... 

<figure>
  <img src="/post/pics/20190313_lucy.jpg" width="330" height="auto"  />
  <figcaption>
      <p>Figure 1: Lucy<p>
  </figcaption>
</figure>

## Como usar e quais os resultados obtidos

Inicialmente, tudo ficará mais fácil se utilizar um sistema operacional
*Linux*. Eu uso e testei no
[Ubuntu](https://www.ubuntu.com/download/flavours), mas fique à vontade
para escolher a sua distribuição. No sistema Windows eu não fiz testes
(e não pretendo).

Os pacotes necessários e como proceder a instalação dos mesmos está descrito
[AQUI](https://github.com/rafatieppo/lucyLattes). 

Uma vez que os requisitos necessários foram atendidos, torna-se possível
utilizar o `lucyLattes`. Siga as seguintes etapas:

### Passo 1

Após fazer o download do `lucyLattes` ([download
aqui](https://github.com/rafatieppo/lucyLattes/archive/master.zip)),
descompacte o arquivo `lucyLattes-master.zip`. Após a descompactação a
pasta `lucyLattes-master` estará disponível. Abra esta pasta e você terá
acesso aos seguintes arquivos e diretórios:

```
| lucyLattes-master
   | --- csv_producao/
   | --- __pycache__/
   | --- relatorio/
   | --- xml_zip/
   | --- qualis_admconta_periodicos_2016.csv
   | --- qualis_agrarias_periodicos_2016.csv
   | --- qualis_ciencamb_periodicos_2016.csv
   | --- qualis_enfermag_periodicos_2016.csv
   | --- qualis_interdic_periodicos_2016.csv
   | --- qualis_lingliterat_periodicos_2016.csv
   | --- grid.edgelist
   | --- FLOWCHART.md
   | --- README.md
   | --- extrafuns.py
   | --- grapho.py
   | --- lucyLattes.py
   | --- readidlist.py
   | --- report.py
   | --- scraperlattes.py
   | --- tidydf.py
   | --- config.txt
   | --- LICENSE.txt
   | --- list_id_name.txt
```

### Passo 2

Acesse o site de busca de currículo
[Lattes](http://buscatextual.cnpq.br/buscatextual/busca.do) e faça o
download dos arquivos `.xml` de todos os currículos desejados. O botão
com o link para fazer o download do arquivo `.xml` fica no canto direito
superior da página com o currículo Lattes. Por exemplo, acesse
[http://lattes.cnpq.br/3275865819287843](http://lattes.cnpq.br/3275865819287843),
preencha o captcha, e olhe no canto direito da página o botão *XLM*, é
só clicar para fazer o download (Figure 2).

<figure>
  <img src="/post/pics/20190313_xlmbutton.png" width="auto" height="250"  />
  <figcaption>
      <p>Figure 2: Download do arquivo `.XML`<p>
  </figcaption>
</figure>

Após clicar no botão *XML* será realizado o download do arquivo `.zip`
com o nome `2300099357169820.zip`. **NÃO** descompacte ou renomeie este
arquivo, este número é o identificador do profissional na plataforma
*Lattes*.

Neste exemplo usamos quatro currículos, consequentemente fizemos o
download de quatro arquivos: `1292986021348016.zip`,
`2300099357169820.zip`, `3275865819287843.zip`,
`5859946324646438.zip`. **Copie** estes quatro arquivos na pasta `xml_zip`.

### Passo 3

No diretório `lucyLattes-master` abra o arquivo `list_id_name.txt` com o
**EDITOR de texto** e preencha de acordo com as orientações que estão no
arquivo. Repare que não há espaço antes e após a vírgula, e obedeça a
sequência: número do currículo, nome abreviado do profissional, grupo do
profissional (Figure 3).

<figure>
  <img src="/post/pics/20190313_listid.png" width="auto" height="250"  />
  <figcaption>
      <p>Figure 3: Preenchimento do arquivo  list_id_name.txt<p>
  </figcaption>
</figure>

### Passo 4

No diretório `lucyLattes-master` abra o arquivo `config.txt` com o
**EDITOR de texto**. Defina qual o qualis desejado, repare que no
diretório `lucyLattes-master` há seis arquivos disponíveis. Se precisar
de algum específico, pode entrar em contato que podemos preparar. Neste
exemplo utilizamos o qualis da ciências agrárias que está no arquivo
`qualis_agrarias_periodicos_2016.csv`, com início da análise desde o ano
2010 até 2019 (Figure 4).

<figure>
  <img src="/post/pics/20190313_config.png" width="auto" height="250"  />
  <figcaption>
      <p>Figure 4: Preenchimento do arquivo  config.txt<p>
  </figcaption>
</figure>

### Passo 5

Utilizando o **Terminal** acesse o diretório `lucyLattes-master` e
digite `python3 lucyLattes.py` e aperte `ENTER` (Figure 5).

<figure>
  <img src="/post/pics/20190313_terminal.png" width="auto" height="250"  />
  <figcaption>
      <p>Figure 5: Executando o script pelo terminal<p>
  </figcaption>
</figure>

### Passo 6 (último) :) 

Se tudo ocorreu bem, no diretório `lucyLattes-master`, acesse a pasta
relatório, e abra com o navegador (Firefox ou Chrome) o arquivo
`relatorio_producao.html`. No navegador aparecerá um relatório com as
seguinte informações: *Equipe*, *Resumo da produção*, *Projetos de
extensão*, *Projetos de pesquisa*, *Artigos em periódicos*, *Extrato de
periódicos por integrante*. 

Além das informações supracitadas, são gerados três gráficos: relação de
produção de artigos em periódicos por ano, relação de periódicos por
qualis, e se há intereção entre os pesquisadores (Figuras 6, 7, e 8).

<figure>
  <img src="/post/pics/20190313_period_dep_year.png" width="530" height="auto"  />
  <figcaption>
      <p>Figure 6: Número de publicações por ano<p>
  </figcaption>
</figure>

<figure>
  <img src="/post/pics/20190313_period_year_qualis.png" width="530" height="auto"  />
  <figcaption>
      <p>Figure 7: Publicações de periódicos por qualis.<p>
  </figcaption>
</figure>

<figure>
  <img src="/post/pics/20190313_grapho.png" width="530" height="auto"  />
  <figcaption>
      <p>Figure 7: Grafo de colaboração entre pesquisadores apenas em artigos.<p>
  </figcaption>
</figure>

O Extrato de periódicos por integrante resume o número de publicação(s)
por ano e qualis:

Rafael Cesar Tieppo: produção total = 20
<table>
<thead>
<tr><th style="text-align: right;">  </th><th style="text-align: right;">  YEAR</th><th style="text-align: right;">  A2</th><th style="text-align: right;">  B1</th><th style="text-align: right;">  B2</th><th style="text-align: right;">  B3</th><th style="text-align: right;">  B5</th><th style="text-align: right;">  C </th><th style="text-align: right;">  XX</th></tr>
</thead>
<tbody>
<tr><td style="text-align: right;"> 0</td><td style="text-align: right;">  2010</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   1</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td></tr>
<tr><td style="text-align: right;"> 1</td><td style="text-align: right;">  2011</td><td style="text-align: right;">   0</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   2</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td></tr>
<tr><td style="text-align: right;"> 2</td><td style="text-align: right;">  2012</td><td style="text-align: right;">   0</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td></tr>
<tr><td style="text-align: right;"> 3</td><td style="text-align: right;">  2013</td><td style="text-align: right;">   0</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td></tr>
<tr><td style="text-align: right;"> 4</td><td style="text-align: right;">  2014</td><td style="text-align: right;">   0</td><td style="text-align: right;">   2</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td></tr>
<tr><td style="text-align: right;"> 5</td><td style="text-align: right;">  2016</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td></tr>
<tr><td style="text-align: right;"> 6</td><td style="text-align: right;">  2017</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   2</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td></tr>
<tr><td style="text-align: right;"> 7</td><td style="text-align: right;">  2018</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   1</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   1</td></tr>
<tr><td style="text-align: right;"> 8</td><td style="text-align: right;">  2019</td><td style="text-align: right;">   1</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td><td style="text-align: right;">   0</td></tr>
</tbody>
</table>
 <hr> 
 
## Considerações

Espero que o `lucyLattes` seja útil de alguma forma, dentro do possível
estarei melhorando o script na sua funcionalidade.
 
 ![](https://i.gifer.com/QLRN.gif)
 
## Notas 

> O lucyLattes não tem vínculo com o CNPq. Este programa computacional é fruto de um esforço (independente) realizado com o objetivo de dar suporte às rotinas de análise de dados cadastradas nos Currículos Lattes (publicamente disponíveis).

> Este programa é um software livre; você pode redistribui-lo e/ou modificá-lo dentro dos termos da Licença Pública Geral GNU. Verifique o arquivo LICENSE.txt .

> Este programa é distribuído na esperança que possa ser util, mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Verifique o arquivo LICENSE.txt .






