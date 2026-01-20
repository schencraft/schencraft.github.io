# Update Transcripts

Update the Lenny's Podcast transcript archive with new episodes from the source repository.

**This skill runs fully automated** — no user confirmation required.

## Usage

```
/update-transcripts
```

## Instructions

1. **Run the import script** to fetch and convert new transcripts:
   ```bash
   python3 scripts/import-transcripts.py
   ```

   This script will:
   - Clone or update the source repository (ChatPRD/lennys-podcast-transcripts)
   - Parse all transcript files from `episodes/*/transcript.md`
   - Generate `_transcripts/*.md` files with metadata
   - Generate `_data/transcript_content/*.json` files
   - Build topic index from the source `index/` folder
   - Write a manifest file with import timestamp

2. **Check for new episodes** by comparing counts:
   ```bash
   ls _transcripts/*.md | wc -l
   ```

3. **Verify the build** works locally (if Jekyll is installed):
   ```bash
   bundle exec jekyll build
   ```

4. **Commit and push** the new transcripts:
   ```bash
   git add _transcripts/
   git commit -m "Update transcripts - add [N] new episodes"
   git push
   ```

5. **Report results** to the user:
   - Number of new episodes added
   - Total episode count
   - Any errors encountered
   - Live URL: https://schencraft.github.io/transcripts/

## Transcript File Structure

Each transcript in `_transcripts/` has this frontmatter:

```yaml
---
slug: "guest-name"
guest: "Guest Name"
title: "Episode Title"
youtube_url: "https://www.youtube.com/watch?v=VIDEO_ID"
video_id: "VIDEO_ID"
publish_date: YYYY-MM-DD
duration: "H:MM:SS"
duration_seconds: 1234.0
view_count: 12345
topics:
  - "Product Management"
  - "Leadership"
description: "Short description..."
---
```

## Source Repository

- **URL**: https://github.com/ChatPRD/lennys-podcast-transcripts
- **Structure**: `episodes/[guest-slug]/transcript.md`
- **Topics**: `index/*.md` files with episode links by category

## Troubleshooting

**Import script fails:**
- Check Python 3 is installed: `python3 --version`
- Check git is available: `git --version`
- Delete `_source_transcripts/` and retry if repo is corrupted

**Missing topics:**
- Topics come from the source `index/` folder
- If a new episode has no topics, it may not be indexed yet upstream

**Build fails:**
- Check for YAML syntax errors in new transcript files
- Look for special characters in titles that need escaping
