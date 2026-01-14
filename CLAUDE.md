# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based personal website and blog for Simon Chen, hosted on GitHub Pages at schencraft.github.io. It uses the Minima theme (v2.5.1) with custom fonts (Inter, JetBrains Mono) and SCSS styling.

## Common Commands

```bash
# Local development (requires Ruby and Bundler)
bundle exec jekyll serve

# Build the site
bundle exec jekyll build

# Serve with drafts visible
bundle exec jekyll serve --drafts
```

No build step is required for deployment—GitHub Pages builds automatically on push to main.

## Architecture

### Content Structure
- `_posts/` - Blog posts with format `YYYY-MM-DD-title-slug.md`
- `_projects/` - Portfolio project pages (custom collection)
- `_layouts/` - Custom layouts (project.html extends default)
- `_includes/` - Custom includes (custom-head.html for fonts)
- `assets/css/style.scss` - Custom SCSS overriding Minima theme

### Front Matter Conventions

**Posts:**
```yaml
---
layout: post
title: "Post Title"
date: YYYY-MM-DD
categories: [general, tech, design, tutorial, project]
---
```
End posts with `*- Simon Chen*` signature.

**Projects:**
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

### Claude Skills

The `.claude/skills/` directory contains workflow definitions:
- `new-post.md` - Create new blog posts
- `update-post.md` - Edit existing posts
- `new-project.md` - Add portfolio projects
- `update-project.md` - Edit projects
- `nutrition-news.md` - Research and add bilingual nutrition news updates

### Bilingual Content

The Nutrition News project uses bilingual (English/Chinese) format:
- English content first, then Chinese summary
- Chinese uses Simplified Chinese (简体中文)
- Technical terms (GLP-1, omega-3) stay in English
- Monthly archiving: old content moves to `nutrition-news-YYYY-MM.md`
