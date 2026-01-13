#!/bin/bash
# Push nutrition news updates to GitHub Pages
# Usage: .claude/scripts/push-nutrition-news.sh "commit message"

set -e

COMMIT_MSG="${1:-Update nutrition news}"

cd "$(git rev-parse --show-toplevel)"

# Stage nutrition news files
git add _projects/nutrition-news*.md

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
echo "Live at: https://schencraft.github.io/projects/nutrition-news/"
