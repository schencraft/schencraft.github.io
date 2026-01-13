# Update Blog Post

Update an existing Jekyll blog post on schencraft.github.io.

## Usage

```
/update-post [search term or filename]
```

If no search term provided, list recent posts for the user to choose from.

## Instructions

1. **Find the post** to update:
   - If a search term is provided, search in `_posts/` directory
   - If no term provided, list all posts in `_posts/` with their titles and dates
   - Let the user select which post to edit

2. **Read the current post** and show a summary to the user:
   - Current title
   - Current date
   - Current categories
   - Brief content preview (first few paragraphs)

3. **Ask what to update**:
   - Title
   - Categories
   - Add new content/sections
   - Edit existing content
   - Fix typos or formatting
   - Complete rewrite

4. **Make the requested changes** while preserving:
   - The original front matter structure
   - The author sign-off (`*- Simon Chen*`)
   - Consistent markdown formatting

5. **Show a diff summary** of what changed after editing.

6. **Commit and push to GitHub** by running:
    ```bash
    .claude/scripts/push-post.sh "Update post: [post title]"
    ```

7. Confirm the push succeeded and share the live URL shown in the script output.
