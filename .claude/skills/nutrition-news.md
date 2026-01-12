# Nutrition News

Research recent nutrition news and add updates to the Nutrition News project page.

## Usage

```
/nutrition-news [optional topic focus]
```

Examples:
- `/nutrition-news` - General nutrition news roundup
- `/nutrition-news gut health` - Focus on gut health news
- `/nutrition-news supplements` - Focus on supplement research

## Instructions

1. **Research recent nutrition news** using web search:
   - Search for recent nutrition research, studies, and health news
   - Look for reputable sources: medical journals, health organizations, nutrition science publications
   - Focus on the last 1-2 weeks of news unless user specifies otherwise
   - If a topic focus is provided, narrow the search accordingly

2. **Gather 3-5 newsworthy items** that are:
   - Based on credible research or expert sources
   - Relevant and actionable for general readers
   - Interesting and not overly technical

3. **Present findings to user** before updating:
   - Show a brief summary of each news item found
   - Include the source for each
   - Ask if they want to include all, select specific ones, or search for more

4. **Check for month rollover** before updating:
   - Read `_projects/nutrition-news.md` to check the current month of entries
   - If the current month differs from today's month:
     a. Archive the old content to `_projects/nutrition-news-YYYY-MM.md` (e.g., `nutrition-news-2026-01.md`)
     b. Clear the main page content (keep intro and archive links)
     c. Add a link to the new archive in the "Past Updates" section

5. **Update the main project page** at `_projects/nutrition-news.md`:
   - Add a new date section: `## Month Day, Year`
   - Add news items under that date
   - Keep only current month's entries on main page

6. **Format each news item**:
   ```markdown
   ### [News Item Title]

   Summary of the finding/news. What the research showed or what experts are saying.

   **Key takeaway:** Actionable insight for readers.

   *Source: [Publication Name](url)*

   ---
   ```

7. **Main page structure**:
   ```markdown
   ---
   title: "Nutrition News"
   description: "Curated updates on nutrition research..."
   tech: [Health, Research, Nutrition Science]
   featured: true
   ---

   Intro paragraph...

   ---

   ## [Current Month Entries]
   ...

   ---

   ## Past Updates

   - [January 2026](/projects/nutrition-news-2026-01/)
   - [December 2025](/projects/nutrition-news-2025-12/)

   *Last updated: [date]*
   ```

8. **Archive page format** (`nutrition-news-YYYY-MM.md`):
   ```markdown
   ---
   title: "Nutrition News - January 2026"
   description: "Nutrition news archive for January 2026"
   ---

   [All entries from that month]

   [Back to current news](/projects/nutrition-news/)
   ```

9. **Important guidelines**:
   - Always cite sources with links
   - Distinguish between preliminary research and established science
   - Avoid sensationalist claims - be balanced and accurate
   - Include practical takeaways when possible

10. After updating, show what was added and confirm the file path.
