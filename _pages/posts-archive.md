---
layout: archive
title: "Posts"
permalink: /posts/
excerpt: "A List of Posts"
---

  {% for post in site.posts %}
<p align="left">


      <h4> &check; <a href="{{ post.url }}">{{ post.date | date: '%Y-%m-%d' }}</a> 
           &#62;&#62; <a href="{{ post.url }}">{{ post.title }}</a> 
      <br>
      <i>{{ post.excerpt }}</i>
      </h4>
</p>
<hr>
  {% endfor %}

