# categories

- datascience
- emacs
- geoprocessing
- python
- R


# mathjax

We have 2 options for this theme:

1. Just type in the post header

mathjax: true

2. Make a file in partials folder:

`mathjax_support.html`with the content:

```
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    displayMath: [['$$','$$'], ['\[','\]']],
    processEscapes: true,
    processEnvironments: true,
    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre','code'],
    TeX: { equationNumbers: { autoNumber: "AMS" },
         extensions: ["AMSmath.js", "AMSsymbols.js"] }
  }
});
</script>
```

and call in the `header.html`

{{ partial "mathjax_support" . }}


# icones na barra lateral

- neste tema o gerenciamento dos icones fica no `icons.html`
- neste tema o social menu fica no `widgets.toml`
- ajustar o social base no `theme.toml`

1.no arquivo no head.html inserir o código

1.1 Fontawesome

WEBFONT:
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">

ou
1.1 Academic icons
<link rel="stylesheet" href="https://cdn.rawgit.com/jpswalsh/academicons/master/css/academicons.min.css">


2. Escolher icon

https://fontawesome.com/icons?d=gallery

3. Adicionar onde quiser o icon

Fontawesome
<i class="fas fa-stroopwafel"></i>
Academicons
<i class="ai ai-google-scholar-square ai-1x"></i>
