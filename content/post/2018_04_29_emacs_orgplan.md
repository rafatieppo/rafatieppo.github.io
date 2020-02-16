---
title: "Planning all your projects with EMACS"
date: 2018-04-29
comments: true
excerpt: "Emacs org-mode rocks"
categories: ["emacs"]
tags: ["emacs", "org-mode", "planning", "column-view"]
toc: true
blogged: "blog"
type: "blog"
---

## Introduction

Every day I open [EMACS](https://www.gnu.org/software/emacs/) to check
my tasks and my schedule. Once I was wondering, why not plan and control
my research projects. I checked some sites
[site 1](https://www.devalot.com/articles/2008/07/project-planning),
[site 2](https://medium.com/@mwfogleman/implementing-a-second-brain-in-emacs-and-org-mode-ef0e44fb7ca5),
and
[site 3](https://orgmode.org/worg/org-tutorials/org-column-view-tutorial.html)
and it was piece of cake. I split in 4 steps.

### Step 1 - prepare your org file

Prepare a `.org` file like this:

```
* PROJECTS 
   :PROPERTIES:
   :COLUMNS:  %6TYPE %20ITEM  %OWNER  %13DEADLINE
   :TYPE_ALL: Proj Action
   :OWNER_ALL: Person1 Person2
   :Approved_ALL: "[ ]" "[X]"
   :DONE_ALL: Yes Nop
   :END:

** PROJECT 1
   :PROPERTIES:
   :TYPE: Pesq
   :END:
*** TODO Action 1 [33%]
   :PROPERTIES:
   :OWNER: Person1
   :DEADLINE: <2018-05-20 Fri>
   :DONE: Nop
   :END:
- [X] Version 1 
- [ ] Version 2 
*** TODO Action 2 [33%]
   :PROPERTIES:
   :OWNER: Person2
   :DEADLINE: <2018-07-20 Fri>
   :DONE: Nop
   :END:
- [X] Version 1 
- [ ] Version 2 
 ```

### Step 2 - Almost there

Once your file is done, you can check it in column-view, just press `C-c C-x C-c`
on `PROJECT1`. It turns each outline item into a table row displaying
some of its properties. 

<img src="/post/pics/2018_04_29_columnview.png" title=''>

>You can switch the column view off and return to the normal view by
>pressing `q` while the cursor is on the highlighted entry – but you can
>turn the column view on from any location in the buffer ([ORG-MODE](https://orgmode.org/worg/org-tutorials/org-column-view-tutorial.html)).

### Step 3 - Improving visualization

*Column view* is a
[dynamic block](https://www.gnu.org/software/emacs/manual/html_node/org/Dynamic-blocks.html#Dynamic-blocks),
so you can capture and and create an overview about all your
projects. In the last line create a new item called `Report` or any
name, and insert the `block` as follows:

```
** Report

#+BEGIN: columnview :maxlevel 5 :hlines t

#+END:
```

On the `BEGIN` press `C-c C-c` and you see the magic:

```
#+BEGIN: columnview :maxlevel 5 :hlines t
| TYPE | ITEM                   | OWNER  | DEADLINE       |
|------|------------------------|--------|----------------|
|      | * PROJECTS             |        |                |
| Pesq | ** Project 1           |        |                |
|      | *** TODO Action 1[33%] | Daniel | 2018-04-20 Fri |
|      | *** TODO Action 2 [%]  | Daniel | 2018-04-27 Fri |
|      | *** TODO PAPER [%]     | Daniel | 2018-04-27 Fri |
|      | ** Report              |        |                |
#+END:

```

### Step 4 - See all in `hmtl` file

[EMACS](https://www.gnu.org/software/emacs/) really rocks. You can
export your file like `.html`, just `C-c C-e`, press `h` and `h` and set
a name. Now in your web browser you can see all you plan like a web page
with your own `CSS`. 

<img src="/post/pics/2018_04_29_hmtlreport.png" title=''>


> Tip: I use [pandoc](https://pandoc.org/) to set the `css`

`pandoc ALLPROJECT_MANAG.html -s --css ~/Dropbox/CSS/SIMONCED_pro_v2.css --toc -o ALLPROJECT_MANAG.html`

Let me know you have some question, just send me a e-mail.

