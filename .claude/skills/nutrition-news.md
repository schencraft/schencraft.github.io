# Nutrition News

Research recent nutrition news and add bilingual (English/Chinese) updates to the Nutrition News project page.

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
     a. Archive the old content to `_projects/nutrition-news-YYYY-MM.md`
     b. Clear the main page content (keep intro and archive links)
     c. Add a link to the new archive in the "Past Updates" section

5. **Update the main project page** at `_projects/nutrition-news.md`:
   - Add a new date section: `## Month Day, Year | YYYY年M月D日`
   - Add news items under that date in bilingual format

6. **Format each news item with English AND Chinese**:
   ```markdown
   ### [English Title]

   English summary of the finding/news.

   **Key takeaway:** English actionable insight.

   ---

   **中文摘要：** Chinese translation of the summary.

   **关键要点：** Chinese translation of the key takeaway.

   *Source/来源: [Publication Name](url)*

   ---
   ```

7. **Main page structure**:
   ```markdown
   ---
   title: "Nutrition News | 营养新闻"
   description: "Curated updates on nutrition research | 营养研究精选更新"
   tech: [Health, Research, Nutrition Science]
   featured: true
   ---

   A curated collection of the latest nutrition research...

   最新营养研究、饮食指南和健康科学的精选更新。

   ---

   ## [Date entries with bilingual content]
   ...

   ---

   ## Past Updates | 往期更新

   - [January 2026 | 2026年1月](/projects/nutrition-news-2026-01/)

   *Last updated | 最后更新: [date]*
   ```

8. **Archive page format** (`nutrition-news-YYYY-MM.md`):
   - Same bilingual format as main page
   - Include back link: `[Back to current news | 返回最新](/projects/nutrition-news/)`

9. **Translation guidelines**:
   - Use Simplified Chinese (简体中文)
   - Keep technical terms accurate (e.g., GLP-1, omega-3 can stay in English)
   - Translate naturally, not word-for-word
   - Maintain the same balanced, non-sensationalist tone

10. **Important content guidelines**:
    - Always cite sources with links
    - Distinguish between preliminary research and established science
    - Include practical takeaways when possible
    - Note if studies are in animals vs humans, small sample sizes, etc.

11. After updating, show what was added and confirm the file path.
