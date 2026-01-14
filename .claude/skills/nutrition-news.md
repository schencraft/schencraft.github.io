# Nutrition News

Research recent nutrition news and add bilingual (English/Chinese) updates to the Nutrition News project page as horizontal scrollable knowledge cards.

**This skill runs fully automated** — no user confirmation required. It will search, curate, write, and publish in one go.

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
   - **Proceed directly to updating the page — do not ask for user approval**

3. **Check for month rollover** before updating:
   - Read `_projects/nutrition-news.md` to check the current month of entries
   - If the current month differs from today's month:
     a. Archive the old content to `_projects/nutrition-news-YYYY-MM.md`
     b. Clear the main page content (keep intro and archive links)
     c. Add a link to the new archive in the "Past Updates" section

4. **Update the main project page** at `_projects/nutrition-news.md`:
   - Add a new date section with cards format (see below)
   - Insert AFTER the intro section `---` and BEFORE any existing date sections

5. **Format as horizontal scrollable knowledge cards**:

   ```html
   <div class="news-date">Month Day, Year <span class="date-cn">| YYYY年M月D日</span></div>
   <p class="scroll-hint">Scroll for more</p>
   <div class="news-cards-container">
   <div class="news-cards">

   <div class="news-card">
   <h4>🎯 Short Catchy Title</h4>
   <div class="card-content">
   Concise summary of the finding (2-4 sentences). Include key numbers/stats. Keep it scannable and informative.
   </div>
   <div class="card-takeaway"><strong>Takeaway:</strong> One actionable insight the reader can use.</div>
   <div class="card-source">来源: <a href="URL">Source Name</a></div>
   </div>

   <!-- More cards... -->

   </div>
   </div>
   ```

6. **Card content guidelines**:
   - **Title**: Use an emoji + short catchy title (max 5-6 words)
   - **Content**: 2-4 sentences, include key numbers, keep scannable
   - **Takeaway**: One practical, actionable insight
   - **Source**: Use "来源:" (bilingual) with linked source name
   - Use appropriate emojis: 🍊🥗☕🧪📋📊🫒🧀🌱🏛️🔬⏰🐟💊🧠💪🥦

7. **Translation approach for cards**:
   - Cards use primarily English for scannability
   - "来源:" is bilingual (Source/来源)
   - Date header includes Chinese: `<span class="date-cn">| 2026年1月13日</span>`
   - Keep technical terms in English (GLP-1, omega-3, etc.)

8. **Archive page format** (`nutrition-news-YYYY-MM.md`):
   - Same card format as main page
   - Include back link: `[Back to current news | 返回最新](/projects/nutrition-news/)`

9. **Important content guidelines**:
   - Always cite sources with links
   - Distinguish between preliminary research and established science
   - Include practical takeaways
   - Note if studies are in animals vs humans, small sample sizes, etc.
   - Keep each card concise — users scroll horizontally to see more

10. **Commit and push to GitHub** by running:
    ```bash
    .claude/scripts/push-nutrition-news.sh "Add nutrition news for [Date] - [brief summary of items]"
    ```

11. Confirm the push succeeded and share the live URL shown in the script output.
