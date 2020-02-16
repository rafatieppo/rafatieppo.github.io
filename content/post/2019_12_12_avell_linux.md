---
title: "Minha experiência com Avell e Linux"
date: 2019-12-12
comments: true
excerpt: "entre distros e repositórios"
categories: [computer and eletronics]
tags: ["avell", "linux", "distros", "PopOS"]
toc: true
blogged: "blog"
type: "blog"
---

## Introdução

Usualmente antes de comprar um novo laptop eu pesquiso, pois nos
dias de hoje há muitas opções e variações de preços. Todavia, como toda
regra tem exceção, uma promoção de *black friday* colaborou para uma
tomada de decisão em que o impulso venceu a razão.

Para ir direto ao assunto, adquiri um laptop da
[Avell](https://avell.com.br), e como uso linux, apesar de no momento da
compra ter verificado a compatibilidade da placa de vídeo, algumas
surpresas surgiram (detalhes do laptop
[aqui](https://avell.com.br/a52-muv-5-bs)). 

## Instalação, problemas e solução

A distro que uso é a [Debian](http://www.debian.org/), fiz um breve post
[AQUI](https://www.linuxdescomplicado.com.br/2019/08/como-escolhi-minha-distribuicao-linux.html)
de como escolhi uma distro. Iniciei a instalação do sistema e tudo
funcionou bem. Quando fiz o login veio a surpresa.

Após o carregamento da interface gráfica (Gnome) ocorria um congelamento
da tela. Após algumas pesquisas, o resultado mais encontrado para
justificar o congelamento da tela é um problema com o "driver"
Noveau. Tentei entrar em modo de segurança e instalar o "driver"
recomendado para o [Debian](http://www.debian.org/), e nada. 

Como não queria retornar ao [Ubuntu](https://ubuntu.com/), testei  como
alternativa o [OpeSUSE](https://www.opensuse.org/), não 
consegui iniciar nem a *grub*. Reiniciei a pesquisa, encontrei *posts*
que relatavam sucesso com o [ArchLinux](https://www.archlinux.org/), mas
como não tenho experiência com a referida distro, e queria um distro
*LTS*, abortei a ideia.

Após algumas horas pesquisando, encontrei uma opção que indiretamente
me direcionou ao [Ubuntu](https://ubuntu.com/), resolvi testar  o
[Pop!_OS](https://system76.com/pop). A instalação foi tranquila, em modo
UEFI, com reconhecimento da GPU, wifi, etc. Com o sistema funcionando
iniciei a instalação dos softwares.

## Sobre distro

O ambiente gráfico padrão é o *Gnome*, contudo os atalhos para
gerenciamento das janelas e *workspaces* são diferentes do Gnome do
[Debian](http://www.debian.org/) ou do [Ubuntu](https://ubuntu.com/),
mas nada que não se possa configurar ou se adaptar. Os ícones e detalhes
das janelas são interessantes, além disso, há alguns temas bem
trabalhados para se escolher. De modo geral a aparência é agradável.

Quanto a repositórios, a distro [Pop!_OS](https://system76.com/pop) usa
a base do [Ubuntu](https://ubuntu.com/), dessa forma, basicamente todos
os pacotes que uso foram encontrados com facilidade. A "loja" de
aplicativos do [Pop!_OS](https://system76.com/pop) é bem legal, e tem
aplicativos como o *spotify*, *telegram*, etc. Comparando com a loja do
[Ubuntu](https://ubuntu.com/), a loja de aplicativos do
[Pop!_OS](https://system76.com/pop) é superior.

O que achei de mais interessante na distro foi o suporte à
*GPU*. Já no instante em que se vai fazer o download da `iso` é possível
escolher entre um instalador dedicado à *Radeon* ou *Nvidia*. A distro
também oferece uma interface para alternar entre a placa dedicada
(*nvidia* ou *Radeon*) e *intel*. Trata-se de uma distro para um usuário
que busca algo pronto, que funcione *out of box*, seja para o trabalho
do dia a dia (escritório, estudo, desenvolvimento, data science), ou até
mesmo para jogos. Se você busca uma distro para estudar o **Linux**, ou
entender melhor o sistema operacional, sugiro outras opções.

A distro [Pop!_OS](https://system76.com/pop) oferece um fluxo de
trabalho bem interessante, e se alguém me perguntar se eu recomendo, a
resposta é **sim**, **sem dúvida**. 

## Opiniões sobre máquina

Ainda não testei nada de muito pesado na máquina, apenas abri algumas
imagens (com mais de 500 MB), então em questão de desempenho não posso
opinar. No geral, não posso reclamar. Tratando-se de uma máquina com
foco em games, considero que a mesma é relativamente silenciosa.

Em relação ao monitor, o mesmo tem, contraste, brilho e nitidez
excelentes. As minhas observações ficam para o teclado:

**1.** a retro iluminação fica com várias cores, pois a
[Avell](https://avell.com.br) não tem suporte para *Linux*, dessa forma
não há um recurso oficial para controle da cores e intensidade. O
teclado fica padrão camaleão!

**2.** o que eu estou mais estranhando é a posição da tecla da *barra*
`/`, porque a referida tecla fica junto com a letra `Q`. Assim como a
tecla *interrogação* `?`, que fica junto com a letra `W`. Deduzo que foi
a solução da [Avell](https://avell.com.br) para otimizar o espaçamento
entre as teclas e deixar as teclas `shift` do lado direito e o `enter`
um pouco maiores.

<figure>
  <img src="/post/pics/20191212_keyboard.png" width="550" height="auto"/>
  <figcaption>
      <p>Figure 1: Avell keyboard<p>
  </figcaption>
</figure>

No mais o teclado é muito bom (pelo menos para mim). Quanto a disposição
das teclas, acredito que é questão de se adaptar.

## Considerações finais

Recomendo a compra, mas de qualquer forma faça uma boa pesquisa de preço
nos concorrentes. O atendimento de vendas da
[Avell](https://avell.com.br) é fenomenal, muito superior ao da
[Dell](https://www.dell.com/pt-br). Infelizmente a Avell não oferece
suporte para *Linux* (ao menos até dezembro de 2019). 

Quem obter um Avell e quiser mais personalização do teclado, tem um
tutorial
[AQUI](https://www.vivaolinux.com.br/dica/Teclado-Retroiluminado-Backlight-Notebook-Avell-Clevo-no-Linux-Mint-ou-Ubuntu-Configuracao),
não testei esta solução. Para resolver o conflito com o teclado colorido
testei um pacote *Python*, diponível
[AQUI](https://github.com/petryx/avell-a52-lights), basta seguir as
instruções de instalação e uso (testei e funcionou).

Futuramente vou tentar estudar um pouco mais sobre *GPU*  para tentar
instalar o [Debian](http://www.debian.org/).

Alguns sites sobre GPU em linux (há muitos outros):

- https://www.vivaolinux.com.br/dica/Teclado-Retroiluminado-Backlight-Notebook-Avell-Clevo-no-Linux-Mint-ou-Ubuntu-Configuracao
- https://plus.diolinux.com.br/t/o-mint-fica-preto-logo-depois-de-inserir-a-senha-de-login/756
- https://bugs.launchpad.net/linuxmint/+bug/1309395














