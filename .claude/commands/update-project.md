# Update Project

Update an existing project entry on schencraft.github.io.

## Usage

```
/update-project [search term or filename]
```

If no search term provided, list all projects for the user to choose from.

## Instructions

1. **Check if projects exist**:
   - If `_projects/` doesn't exist, inform the user and suggest using `/new-project` first
   - If empty, inform the user there are no projects yet

2. **Find the project** to update:
   - If a search term is provided, search in `_projects/` directory
   - If no term provided, list all projects with their titles and descriptions
   - Let the user select which project to edit

3. **Read the current project** and show a summary:
   - Current title
   - Description
   - Technologies
   - GitHub/Live URLs
   - Featured status
   - Brief content preview

4. **Ask what to update**:
   - Title or description
   - Technologies list
   - GitHub or live demo URLs
   - Featured status
   - Add new content/sections
   - Update existing content
   - Add screenshots/images

5. **Make the requested changes** while preserving:
   - The front matter structure
   - Consistent markdown formatting
   - Any existing images/links

6. **Show a diff summary** of what changed after editing.

7. **Commit and push to GitHub** by running:
    ```bash
    .claude/scripts/push-project.sh "Update project: [project name]"
    ```

8. Confirm the push succeeded and share the live URL shown in the script output.
