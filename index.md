---
layout: default
title: Home
---

# Welcome to SChen Craft

I'm **Simon Chen**, a creative technologist exploring the intersection of design and technology.

## Latest Posts

{% for post in site.posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}

---

*Building things that matter.*
