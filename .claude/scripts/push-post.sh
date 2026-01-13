#!/bin/bash
# Push blog post changes to GitHub Pages
# Usage: .claude/scripts/push-post.sh "commit message"

set -e

COMMIT_MSG="${1:-Update blog post}"

cd "$(git rev-parse --show-toplevel)"

# Stage post files
git add _posts/*.md

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
echo "Live at: https://schencraft.github.io/"
