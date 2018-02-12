

## Locations of key files/directories

* Basic config options: _config.yml
* Top navigation bar config: _data/navigation.yml
* Single pages: _pages/
* Collections of pages are .md or .html files in:
  * _publications/
  * _portfolio/
  * _posts/
  * _teaching/
  * _talks/
* Footer: _includes/footer.html
* Static files (like PDFs): /files/
* Profile image (can set in _config.yml): images/profile.png

## Tips and hints

* Name a file ".md" to have it render in markdown, name it ".html" to render in HTML.
* Go to the [commit list](https://github.com/academicpages/academicpages.github.io/commits/master) (on your repo) to find the last version Github built with Jekyll. 
  * Green check: successful build
  * Orange circle: building
  * Red X: error
  * No icon: not built


## A data-driven personal website

Like many other Jekyll-based GitHub Pages templates, academicpages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

## Getting started

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

## Site-wide configuration

The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

## Create content & metadata

For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the academicpages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

## How to edit your site's GitHub repository

Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

## For more info

More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.

## Install Jekyll Ubuntu 16.04

* $ sudo apt-get update
* $ sudo apt-get install ruby ruby-dev make gcc
* $ sudo gem install jekyll bundler
* $ bundle install (into sites's folder)
* $ sudo apt-get install nodejs


## To run locally (not on GitHub Pages, to serve on your own computer)

    1. Clone the repository and made updates as detailed above
    2. Make sure you have ruby-dev, bundler, and nodejs installed: sudo apt install ruby-dev ruby-bundler nodejs
    3. Run bundle clean to clean up the directory (no need to run --force)
    4. Run bundle install to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
    5. Run bundle exec jekyll serve to generate the HTML and serve it from localhost:4000

## Home page

The `index.html` in `home` folder just call the layout in `_layouts`. Therefore, to change features in home page you must code at `./_layouts/LAYOUT_NAME.html`

## Changing site apearance features

To change fonts:
- `_variables.scss` into `_sass` dir.

To change side bar margin etc:
- `_sidebar.scss`

## Changing navigation menu

Access `./_data/navigation.yml`

## Add new icon in side bar

Assing the path in `./_inlcudes/head.htm`

<!-- Link to Academicon ORDID icon -->
<link rel="stylesheet" href="/assets/css/academicons.css"/>

Find the file `_includes/author-profile-custom-links.html` and type:

  <li>
    <a href="http://orcid.org/0000-0001-8132-4813" itemprop="sameAs">
      <i class="ai ai-orcid-square ai-fw"></i> ORCID
    </a>
  </li>

  <li>
    <a href="https://www.researchgate.net/profile/rafatieppo" itemprop="sameAs">
      <i class="ai ai-researchgate-square ai-fw"></i> ResearchGate
    </a>
  </li>

make sure to copy `./fonts` in `./assets`


## Add icon image in browser

Find `custom.html` in `_includes/head/`and set path in:

```
<link rel="shortcut icon" href="{{ base_path }}favicon.ico">
<link rel="shortcut icon" href="{{ base_path }}favicon.png">
```

## Controling pages

Each page has a intial frame. You can find the control files in `_pages`.
For instance, to show a list of **posts**, you just need to create a `.html` file with a appropriate head, e.g. `portfolio-archive.html`

```shell
---
layout: archive
title: "Portsss"
permalink: /portfolio/
author_profile: false
---

{% include base_path %}

<div class="grid__wrapper">
  {% for post in site.portfolio %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>
```
Further insert setting as follows in `_config.yml`

```shell
# Defaults
defaults:
  #  _posts
  - scope:
      path: "_posts"
      type: posts
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: # true
      share: true
      related: true
  # _portfolio
  - scope:
      path: "_portfolio"
      type: portfolio
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: # true
      share: true
      related: true

# Collections
collections:
  talks:
    output: true
    permalink: /:collection/:path/
  portfolio:
    output: true
    permalink: /:collection/:path/
  resources:
    output: true
    permalink: /:collection/:path/
  research:
    output: true
permalink: /:collection/:path/
```

## Make list of blogs

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

another format:

  {% for post in site.posts %}
<p>
      <small><a href="{{ post.url }}">{{ post.title }}</a></small>
      <small><a href="{{ post.url }}">{{ post.date | date: '%Y-%m-%d' }}</a> </small> 
      <small>{{ post.excerpt }}</small>
    <hr>
</p>

  {% endfor %}

https://jekyllrb.com/docs/posts/#displaying-an-index-of-posts
https://jekyllrb.com/docs/templates/
https://jekyllrb.com/docs/frontmatter/

