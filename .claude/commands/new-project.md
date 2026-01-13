# New Project

Create a new project entry for schencraft.github.io portfolio.

## Usage

```
/new-project [project name]
```

If no name is provided, ask the user for project details.

## Setup (First Time Only)

If `_projects/` directory doesn't exist, set up the projects infrastructure:

1. **Create `_projects/` directory**

2. **Update `_config.yml`** to add the projects collection:
   ```yaml
   collections:
     projects:
       output: true
       permalink: /projects/:name/
   ```

   Add to `defaults:`:
   ```yaml
   - scope:
       path: ""
       type: "projects"
     values:
       layout: "project"
   ```

3. **Create `_layouts/project.html`**:
   ```html
   ---
   layout: default
   ---
   <article class="project">
     <header>
       <h1>{{ page.title }}</h1>
       <p class="project-meta">
         {% if page.tech %}
         <span class="tech">{{ page.tech | join: ", " }}</span>
         {% endif %}
         {% if page.github %}<a href="{{ page.github }}">GitHub</a>{% endif %}
         {% if page.live %}<a href="{{ page.live }}">Live Demo</a>{% endif %}
       </p>
     </header>
     <div class="project-content">
       {{ content }}
     </div>
   </article>
   ```

4. **Create `projects.md`** index page:
   ```markdown
   ---
   layout: default
   title: Projects
   permalink: /projects/
   ---
   # Projects

   {% for project in site.projects %}
   ### [{{ project.title }}]({{ project.url }})
   {{ project.description }}

   **Tech:** {{ project.tech | join: ", " }}
   {% endfor %}
   ```

5. **Add to header navigation** in `_config.yml`:
   ```yaml
   header_pages:
     - about.md
     - projects.md
   ```

## Creating a Project

1. **Get project details** from the user:
   - Project name (required)
   - Short description (1-2 sentences)
   - Technologies used
   - GitHub URL (optional)
   - Live demo URL (optional)
   - Detailed description/story

2. **Create the project file** in `_projects/` as `project-slug.md`

3. **Use this front matter template**:
   ```yaml
   ---
   title: "Project Name"
   description: "Short description for listings"
   tech: [tech1, tech2, tech3]
   github: https://github.com/schencraft/repo
   live: https://example.com
   featured: true
   ---
   ```

4. **Write the content** with sections like:
   - Overview
   - The Problem / Motivation
   - Solution / Approach
   - Key Features
   - Challenges & Learnings
   - Screenshots (if provided)

5. **Commit and push to GitHub** by running:
    ```bash
    .claude/scripts/push-project.sh "Add new project: [project name]"
    ```

6. Confirm the push succeeded, share the live URL, and remind to add images to `assets/projects/` if needed.
