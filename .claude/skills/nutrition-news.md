# Nutrition News

Research recent nutrition news and add bilingual (English/Chinese) updates to the Nutrition News project page as Swiper.js card carousels.

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
   - Add a new date section with Swiper carousel (see below)
   - Insert AFTER the intro `---` and BEFORE any existing date sections

5. **Format as Swiper.js bilingual card carousel**:

   ```html
   <div class="news-date">Month Day, Year <span class="date-cn">| YYYY年M月D日</span></div>

   <div class="news-carousel">
   <div class="swiper news-swiper-[unique-id]">
   <div class="swiper-wrapper">

   <div class="swiper-slide">
   <div class="news-card">
   <h4>🎯 Short English Title</h4>
   <div class="card-title-cn">中文标题</div>
   <div class="card-content">
   English summary (2-3 sentences). Include key numbers/stats.
   </div>
   <div class="card-content-cn">
   中文摘要（2-3句）。包含关键数据。
   </div>
   <div class="card-takeaway"><strong>Takeaway:</strong> English insight.</div>
   <div class="card-takeaway-cn"><strong>要点：</strong> 中文要点。</div>
   <div class="card-source">Source/来源: <a href="URL">Source Name</a></div>
   </div>
   </div>

   <!-- More slides... -->

   </div>
   <div class="swiper-pagination"></div>
   <div class="swiper-button-prev"></div>
   <div class="swiper-button-next"></div>
   </div>
   </div>
   ```

6. **Card content guidelines**:
   - **Title**: Emoji + short English title (max 5-6 words)
   - **Title CN**: Chinese translation of the title
   - **Content**: 2-3 sentences in English, include key numbers
   - **Content CN**: Chinese translation of the content
   - **Takeaway**: English practical insight
   - **Takeaway CN**: Chinese translation with `<strong>要点：</strong>`
   - **Source**: Use "Source/来源:" with linked source name
   - Emojis: 🍊🥗☕🧪📋📊🫒🧀🌱🏛️🔬⏰🐟💊🧠💪🥦

7. **Translation guidelines**:
   - Use Simplified Chinese (简体中文)
   - Keep technical terms in English (GLP-1, omega-3, α-glucosidase)
   - Translate naturally, not word-for-word
   - Maintain balanced, non-sensationalist tone in both languages

8. **Archive page format** (`nutrition-news-YYYY-MM.md`):
   - Same Swiper format as main page
   - Include back link: `[Back to current news | 返回最新](/projects/nutrition-news/)`
   - Include the Swiper init script at the end

9. **Important content guidelines**:
   - Always cite sources with links
   - Distinguish between preliminary research and established science
   - Include practical takeaways
   - Note if studies are in animals vs humans, small sample sizes, etc.
   - Keep each card concise for easy scanning

10. **Swiper init script** (already at bottom of page, no need to add again):
    ```html
    <script>
    document.addEventListener('DOMContentLoaded', function() {
      document.querySelectorAll('.swiper').forEach(function(el) {
        new Swiper(el, {
          slidesPerView: 'auto',
          spaceBetween: 16,
          grabCursor: true,
          pagination: {
            el: el.querySelector('.swiper-pagination'),
            clickable: true,
          },
          navigation: {
            nextEl: el.querySelector('.swiper-button-next'),
            prevEl: el.querySelector('.swiper-button-prev'),
          },
        });
      });
    });
    </script>
    ```

11. **Commit and push to GitHub** by running:
    ```bash
    .claude/scripts/push-nutrition-news.sh "Add nutrition news for [Date] - [brief summary of items]"
    ```

12. Confirm the push succeeded and share the live URL shown in the script output.
