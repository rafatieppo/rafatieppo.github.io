---
layout: archive
title: "Posts"
permalink: /posts/
excerpt: "A List of Posts"
---

	
  {% for post in site.posts %}
<p align="left">


      <h4><b>&check; <a href="{{ post.url }}">{{ post.date | date: '%Y-%m-%d' }}</a> 
           &#62;&#62; <a href="{{ post.url }}">{{ post.title }}</b></a> 
      
      <i><h5>{{ post.excerpt }}</h5></i>
      </h4>
</p>
<hr>
  {% endfor %}
