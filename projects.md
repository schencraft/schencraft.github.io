---
layout: default
title: Projects
permalink: /projects/
---

# Projects

{% for project in site.projects %}
## [{{ project.title }}]({{ project.url }})

{{ project.description }}

{% if project.tech %}**Tech:** {{ project.tech | join: ", " }}{% endif %}

---
{% endfor %}
