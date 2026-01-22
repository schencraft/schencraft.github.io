---
layout: default
title: Projects
permalink: /projects/
---

# Projects

<div class="project-grid">
{% for project in site.projects %}
<div class="project-card">
  <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
  <p>{{ project.description }}</p>
  {% if project.tech %}
  <div class="tech-tags">
    {% for t in project.tech %}
    <span class="tech-tag">{{ t }}</span>
    {% endfor %}
  </div>
  {% endif %}
</div>
{% endfor %}
</div>
