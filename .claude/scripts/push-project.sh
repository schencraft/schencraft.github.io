#!/bin/bash
# Push project changes to GitHub Pages
# Usage: .claude/scripts/push-project.sh "commit message"

set -e

COMMIT_MSG="${1:-Update project}"

cd "$(git rev-parse --show-toplevel)"

# Stage project files (and any config/layout changes for first-time setup)
git add _projects/*.md 2>/dev/null || true
git add _config.yml 2>/dev/null || true
git add _layouts/project.html 2>/dev/null || true
git add projects.md 2>/dev/null || true

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Commit with co-author
git commit -m "$COMMIT_MSG

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

# Push to GitHub
git push origin main

echo ""
echo "Pushed to GitHub Pages!"
echo "Live at: https://schencraft.github.io/projects/"
