---
layout: archive
title: Posts
excerpt: "A List of Posts"
---

	
  {% for post in site.posts %}
<p align="left">


      <h6> &check; <a href="{{ post.url }}">{{ post.date | date: '%Y-%m-%d' }}</a> 
           &#62;&#62; <a href="{{ post.url }}">{{ post.title }}</a> 
      </h6>
      <small>{{ post.excerpt }}</small>

</p>
<hr>
  {% endfor %}


