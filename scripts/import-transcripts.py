#!/usr/bin/env python3
"""
Import Lenny's Podcast transcripts from GitHub repository.
Converts transcripts to Jekyll collection format.

Usage:
    python scripts/import-transcripts.py

This script will:
1. Clone/update the source repository
2. Parse each transcript file
3. Generate _transcripts/*.md files with metadata
4. Optionally generate _data/transcript_content/*.json for full text
"""

import os
import json
import re
import subprocess
from pathlib import Path
from datetime import datetime

# Configuration
SOURCE_REPO = "https://github.com/ChatPRD/lennys-podcast-transcripts.git"
CLONE_DIR = Path("_source_transcripts")
OUTPUT_DIR = Path("_transcripts")
DATA_DIR = Path("_data/transcript_content")
INDEX_DIR = CLONE_DIR / "index"

def clone_or_update_repo():
    """Clone the source repo or pull latest changes."""
    if CLONE_DIR.exists():
        print("Updating existing repository...")
        subprocess.run(["git", "-C", str(CLONE_DIR), "pull"], check=True)
    else:
        print("Cloning repository...")
        subprocess.run(["git", "clone", "--depth", "1", SOURCE_REPO, str(CLONE_DIR)], check=True)

def parse_transcript_file(filepath):
    """Parse a transcript markdown file and extract frontmatter and body."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter from body
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1].strip()
            body = parts[2].strip()
        else:
            return None, None
    else:
        return None, None

    # Parse YAML frontmatter manually (simple parser)
    frontmatter = {}
    current_key = None
    current_list = None

    for line in frontmatter_text.split('\n'):
        line = line.rstrip()

        # Check for list item
        if line.startswith('  - '):
            if current_list is not None:
                current_list.append(line[4:].strip())
            continue

        # Check for key-value
        if ':' in line and not line.startswith(' '):
            if current_list is not None and current_key:
                frontmatter[current_key] = current_list
                current_list = None

            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            if value == '':
                # This might be a list
                current_key = key
                current_list = []
            else:
                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                frontmatter[key] = value
                current_key = key

    # Don't forget the last list
    if current_list is not None and current_key:
        frontmatter[current_key] = current_list

    return frontmatter, body

def get_slug_from_path(filepath):
    """Extract slug from file path (parent directory name)."""
    return filepath.parent.name

def build_topic_index():
    """Build a mapping of episode slugs to topics from index files."""
    topic_map = {}  # slug -> [topics]

    if not INDEX_DIR.exists():
        return topic_map

    for index_file in INDEX_DIR.glob("*.md"):
        if index_file.name == "README.md":
            continue

        topic_name = index_file.stem.replace("-", " ").title()

        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all episode links: [Guest Name](../episodes/slug/transcript.md)
        pattern = r'\[([^\]]+)\]\(\.\./episodes/([^/]+)/transcript\.md\)'
        for match in re.finditer(pattern, content):
            slug = match.group(2)
            if slug not in topic_map:
                topic_map[slug] = []
            if topic_name not in topic_map[slug]:
                topic_map[slug].append(topic_name)

    return topic_map

def generate_transcript_md(slug, frontmatter, body, topics):
    """Generate a Jekyll-compatible markdown file for a transcript."""
    # Build new frontmatter
    new_fm = {
        'slug': slug,
        'guest': frontmatter.get('guest', 'Unknown'),
        'title': frontmatter.get('title', ''),
        'youtube_url': frontmatter.get('youtube_url', ''),
        'video_id': frontmatter.get('video_id', ''),
        'publish_date': frontmatter.get('publish_date', ''),
        'duration': frontmatter.get('duration', ''),
        'duration_seconds': frontmatter.get('duration_seconds', ''),
        'view_count': frontmatter.get('view_count', ''),
        'keywords': frontmatter.get('keywords', []),
        'topics': topics,
        'description': frontmatter.get('description', '')[:200] if frontmatter.get('description') else '',
    }

    # Build YAML
    lines = ['---']
    lines.append(f'slug: "{slug}"')

    guest = new_fm["guest"].replace('"', '\\"')
    lines.append(f'guest: "{guest}"')

    title = new_fm["title"].replace('"', '\\"')
    lines.append(f'title: "{title}"')

    lines.append(f'youtube_url: "{new_fm["youtube_url"]}"')
    lines.append(f'video_id: "{new_fm["video_id"]}"')
    lines.append(f'publish_date: {new_fm["publish_date"]}')
    lines.append(f'duration: "{new_fm["duration"]}"')

    if new_fm['duration_seconds']:
        lines.append(f'duration_seconds: {new_fm["duration_seconds"]}')

    if new_fm['view_count']:
        lines.append(f'view_count: {new_fm["view_count"]}')

    if new_fm['keywords']:
        lines.append('keywords:')
        for kw in new_fm['keywords']:
            kw_escaped = kw.replace('"', '\\"')
            lines.append(f'  - "{kw_escaped}"')

    if new_fm['topics']:
        lines.append('topics:')
        for topic in new_fm['topics']:
            topic_escaped = topic.replace('"', '\\"')
            lines.append(f'  - "{topic_escaped}"')

    if new_fm['description']:
        desc = new_fm["description"].replace('"', '\\"')
        lines.append(f'description: "{desc}"')

    lines.append('---')
    lines.append('')

    # Add transcript body
    lines.append(body)

    return '\n'.join(lines)

def generate_transcript_json(slug, body):
    """Generate a JSON file with the full transcript text."""
    return json.dumps({
        'slug': slug,
        'transcript': body
    }, ensure_ascii=False, indent=2)

def main():
    print("=" * 60)
    print("Lenny's Podcast Transcript Importer")
    print("=" * 60)

    # Clone or update repo
    clone_or_update_repo()

    # Create output directories
    OUTPUT_DIR.mkdir(exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Build topic index
    print("\nBuilding topic index...")
    topic_map = build_topic_index()
    print(f"Found topics for {len(topic_map)} episodes")

    # Find all transcript files
    episodes_dir = CLONE_DIR / "episodes"
    transcript_files = list(episodes_dir.glob("*/transcript.md"))
    print(f"\nFound {len(transcript_files)} transcript files")

    # Process each transcript
    success_count = 0
    error_count = 0

    for filepath in transcript_files:
        slug = get_slug_from_path(filepath)

        try:
            frontmatter, body = parse_transcript_file(filepath)

            if frontmatter is None:
                print(f"  [SKIP] {slug}: No valid frontmatter")
                error_count += 1
                continue

            # Get topics for this episode
            topics = topic_map.get(slug, [])

            # Generate and save markdown file
            md_content = generate_transcript_md(slug, frontmatter, body, topics)
            md_path = OUTPUT_DIR / f"{slug}.md"
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)

            # Generate and save JSON file (optional, for on-demand loading)
            json_content = generate_transcript_json(slug, body)
            json_path = DATA_DIR / f"{slug}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                f.write(json_content)

            success_count += 1

            if success_count % 50 == 0:
                print(f"  Processed {success_count} transcripts...")

        except Exception as e:
            print(f"  [ERROR] {slug}: {e}")
            error_count += 1

    print("\n" + "=" * 60)
    print(f"Import complete!")
    print(f"  Successful: {success_count}")
    print(f"  Errors: {error_count}")
    print(f"  Output: {OUTPUT_DIR}/")
    print(f"  Data: {DATA_DIR}/")
    print("=" * 60)

    # Write manifest
    manifest = {
        'imported_at': datetime.now().isoformat(),
        'source_repo': SOURCE_REPO,
        'total_episodes': success_count,
        'errors': error_count
    }
    with open(OUTPUT_DIR / '_manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)

if __name__ == '__main__':
    main()
