# Nutrition News

Research recent nutrition news and add bilingual (English/Chinese) updates to the Nutrition News project page as mobile-friendly Swiper carousel cards.

**This skill runs fully automated** — no user confirmation required. It will search, curate, write, generate XHS images, and publish in one go.

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
   - Add a new date section with Swiper carousel (see format below)
   - Insert AFTER the intro `---` and BEFORE any existing date sections
   - Update the "Last updated" date at the bottom

5. **Format as Swiper carousel** (copy this structure exactly):

   ```html
   <div class="news-date">
     <span class="date-text">January 15, 2026 <span class="date-cn">| 2026年1月15日</span></span>
     <button class="export-btn" onclick="exportAllCards('2026-01-15')">Export All</button>
   </div>

   <p class="scroll-hint">Swipe to see more cards</p>

   <div class="news-carousel">
     <div class="swiper" id="swiper-2026-01-15">
       <div class="swiper-wrapper">

   <div class="swiper-slide">
   <div class="news-card" data-date="2026-01-15" data-emoji="🎯" data-title="Short English Title" data-title-cn="中文标题">
   <h4>🎯 Short English Title</h4>
   <div class="title-cn">中文标题</div>
   <p>English summary (2-3 sentences). Include key numbers/stats.</p>
   <div class="content-cn">中文摘要（2-3句）。包含关键数据。</div>
   <div class="takeaway"><strong>Takeaway:</strong> English insight.</div>
   <div class="takeaway-cn"><strong>要点：</strong> 中文要点。</div>
   <div class="source">Source/来源: <a href="URL">Source Name</a></div>
   </div>
   </div>

   <!-- More swiper-slide cards... -->

       </div>
       <div class="swiper-pagination"></div>
       <div class="swiper-button-prev"></div>
       <div class="swiper-button-next"></div>
     </div>
   </div>
   ```

6. **Card content guidelines**:
   - **data attributes**: Include date, emoji, title, title-cn for XHS export
   - **Title (h4)**: Emoji + short English title (max 5-6 words)
   - **title-cn**: Chinese translation of the title
   - **p**: 2-3 sentences in English, include key numbers
   - **content-cn**: Chinese translation of the content
   - **takeaway**: English practical insight with `<strong>Takeaway:</strong>`
   - **takeaway-cn**: Chinese translation with `<strong>要点：</strong>`
   - **source**: Use "Source/来源:" with linked source name
   - Emojis: 🍊🥗☕🧪📋📊🫒🧀🌱🏛️🔬⏰🐟💊🧠💪🥦

7. **Translation guidelines**:
   - Use Simplified Chinese (简体中文)
   - Keep technical terms in English (GLP-1, omega-3, α-glucosidase)
   - Translate naturally, not word-for-word
   - Maintain balanced, non-sensationalist tone in both languages

8. **Important content guidelines**:
   - Always cite sources with links
   - Distinguish between preliminary research and established science
   - Include practical takeaways
   - Note if studies are in animals vs humans, small sample sizes, etc.
   - Keep each card concise for easy scanning

9. **Generate XHS card images** automatically:
   ```bash
   python scripts/generate_xhs_cards.py --parse-md _projects/nutrition-news.md --date YYYY-MM-DD --output xhs_cards
   ```
   Output: 1242x1660px PNG images (3:4 ratio) in `xhs_cards/` directory

10. **Commit and push to GitHub** by running:
    ```bash
    .claude/scripts/push-nutrition-news.sh "Add nutrition news for [Date] - [brief summary of items]"
    ```

11. Confirm the push succeeded and share:
    - Live URL: https://schencraft.github.io/projects/nutrition-news/
    - Generated XHS images in `xhs_cards/` directory
