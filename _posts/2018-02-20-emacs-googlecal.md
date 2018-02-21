---
title: "Integrating emacs org-mode and google calendar"
date: 2018-02-20
excerpt: "A python script to synchronize .ical file"
categories:
  - python
tags:
  - emacs
  - python
  - google calendar
  - org-cal
toc: true
---

I am an [EMACS](https://www.gnu.org/software/emacs/) user and
consequently I use the amazing **Org mode** to plan my schedule and to
manage my projects. However I was boring about how I synchronized the
`.ics` file from [EMACS](https://www.gnu.org/software/emacs/) and my
Google calendar. I spent some minutes in my Google calendar to clear the
appointments, and import a new file. So, a while ago I improved my
routine. I did know nothing about it.

![]({{ site.url }}{{ site.baseurl }}/assets/pics/posts/2018-02-20-knownothing.gif){: .align-center}

First of all, I read about
[org-cal](https://github.com/myuhe/org-gcal.el) and
[org-caldav](https://github.com/dengste/org-caldav). I found a great
blog [Cestlaz](http://cestlaz.github.io/posts/using-emacs-26-gcal/#.Wo1OkeZG3ix),
it provided me a good experience. A last topic was about [Google API
Client Libraries using  Python I didI](https://developers.google.com/api-client-library/python/start/installation).
I gathered all the information and created (or adapted) a *Python*
script to work for me.

The script is quite simple, from shell (I use
[Linux Ubuntu](https://ubuntu-mate.org/)) you just need to run the script. It erases
**all** appointments in *Google calendar*, and sends the `.ics`
file from [EMACS org mode](https://orgmode.org/).

```shell
./API_CAL_refresh.py
```

A weakness in that script is the speed. The appointments are sent one by
one, regarding the number of the appointments in `.ics` file, the upload
may take some minutes. For now it is good enough to me, maybe I will try to
improve that code.

You can find that script and more information on my
[Github](https://github.com/rafatieppo/PY_UTILITIES/tree/master/API_GOOGLECAL). Let
me know you have some question, just send me a e-mail.

