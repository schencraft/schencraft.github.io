# New Blog Post

Create a new Jekyll blog post for schencraft.github.io.

## Usage

```
/new-post [title]
```

If no title is provided, ask the user for the post title and topic.

## Instructions

1. **Get post details** from the user:
   - Title (required)
   - Topic/content description
   - Categories (optional, default to relevant ones like: general, tech, design, tutorial, project)

2. **Create the post file** in `_posts/` with the naming convention:
   ```
   YYYY-MM-DD-title-slug.md
   ```
   - Use today's date
   - Convert title to lowercase slug (spaces to hyphens, remove special characters)

3. **Use this front matter template**:
   ```yaml
   ---
   layout: post
   title: "Post Title Here"
   date: YYYY-MM-DD
   categories: [category1, category2]
   ---
   ```

4. **Write the content** based on what the user describes. Structure it with:
   - An engaging introduction
   - Clear sections with markdown headers (##, ###)
   - Code blocks with syntax highlighting where appropriate
   - A conclusion or call-to-action if fitting

5. **Sign off** with `*- Simon Chen*` at the end

6. **Commit and push to GitHub** by running:
    ```bash
    .claude/scripts/push-post.sh "Add new post: [post title]"
    ```

7. Confirm the push succeeded and share the live URL shown in the script output.
