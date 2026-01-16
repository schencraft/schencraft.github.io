#!/usr/bin/env python3
"""
XHS (Xiaohongshu/RedNote) Card Generator

Generates beautiful card images for Xiaohongshu from nutrition news data.
Output: 3:4 ratio PNG images (1242x1660px)

Usage:
    python scripts/generate_xhs_cards.py [options]

Options:
    --input FILE      JSON file with news data (default: stdin)
    --output DIR      Output directory (default: ./xhs_cards)
    --date DATE       Filter by date (YYYY-MM-DD)
    --parse-md FILE   Parse existing nutrition-news.md file
    --style STYLE     Card style: morandi, vibrant, minimal (default: morandi)
"""

import argparse
import asyncio
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional, Union, List

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Error: playwright not installed. Run: pip install playwright && playwright install chromium")
    sys.exit(1)


# Card dimensions (3:4 ratio for XHS)
CARD_WIDTH = 1242
CARD_HEIGHT = 1660


@dataclass
class NewsCard:
    """Represents a single news card."""
    emoji: str
    title: str
    title_cn: str
    content: str
    content_cn: str
    takeaway: str
    takeaway_cn: str
    source: str
    source_url: str
    date: str


# Color schemes
STYLES = {
    "morandi": {
        "bg": "#F5F3EF",
        "card_bg": "#FFFFFF",
        "accent": "#8B9A82",
        "accent_light": "#E8EBE4",
        "title": "#2D3436",
        "text": "#4A5568",
        "text_cn": "#636E72",
        "takeaway_bg": "#F0EDE8",
        "source": "#9CA3AF",
        "emoji_bg": "#E8EBE4",
    },
    "vibrant": {
        "bg": "#FFF5F5",
        "card_bg": "#FFFFFF",
        "accent": "#E53E3E",
        "accent_light": "#FED7D7",
        "title": "#1A202C",
        "text": "#4A5568",
        "text_cn": "#718096",
        "takeaway_bg": "#FFF5F5",
        "source": "#A0AEC0",
        "emoji_bg": "#FED7D7",
    },
    "minimal": {
        "bg": "#FAFAFA",
        "card_bg": "#FFFFFF",
        "accent": "#1A202C",
        "accent_light": "#E2E8F0",
        "title": "#1A202C",
        "text": "#4A5568",
        "text_cn": "#718096",
        "takeaway_bg": "#F7FAFC",
        "source": "#A0AEC0",
        "emoji_bg": "#EDF2F7",
    },
}


def generate_html(card: NewsCard, style: str = "morandi") -> str:
    """Generate HTML for a single card."""
    colors = STYLES.get(style, STYLES["morandi"])

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap');

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            width: {CARD_WIDTH}px;
            height: {CARD_HEIGHT}px;
            background: {colors['bg']};
            font-family: 'Inter', 'Noto Sans SC', sans-serif;
            padding: 48px;
            display: flex;
            flex-direction: column;
        }}

        .card {{
            background: {colors['card_bg']};
            border-radius: 32px;
            padding: 56px;
            flex: 1;
            display: flex;
            flex-direction: column;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
        }}

        .header {{
            display: flex;
            align-items: flex-start;
            gap: 24px;
            margin-bottom: 40px;
        }}

        .emoji-container {{
            width: 88px;
            height: 88px;
            background: {colors['emoji_bg']};
            border-radius: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            flex-shrink: 0;
        }}

        .title-container {{
            flex: 1;
        }}

        .title {{
            font-size: 42px;
            font-weight: 700;
            color: {colors['title']};
            line-height: 1.3;
            margin-bottom: 12px;
        }}

        .title-cn {{
            font-size: 32px;
            font-weight: 500;
            color: {colors['text_cn']};
            line-height: 1.4;
        }}

        .content {{
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}

        .text {{
            font-size: 28px;
            line-height: 1.7;
            color: {colors['text']};
        }}

        .text-cn {{
            font-size: 26px;
            line-height: 1.7;
            color: {colors['text_cn']};
        }}

        .takeaway {{
            background: {colors['takeaway_bg']};
            border-left: 5px solid {colors['accent']};
            border-radius: 0 16px 16px 0;
            padding: 28px 32px;
            margin-top: auto;
        }}

        .takeaway-label {{
            font-size: 22px;
            font-weight: 600;
            color: {colors['accent']};
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }}

        .takeaway-text {{
            font-size: 26px;
            font-weight: 500;
            color: {colors['title']};
            line-height: 1.5;
            margin-bottom: 8px;
        }}

        .takeaway-cn {{
            font-size: 24px;
            color: {colors['text_cn']};
            line-height: 1.5;
        }}

        .footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 32px;
            padding-top: 24px;
            border-top: 1px solid {colors['accent_light']};
        }}

        .source {{
            font-size: 20px;
            color: {colors['source']};
        }}

        .brand {{
            font-size: 20px;
            font-weight: 600;
            color: {colors['accent']};
        }}

        .date {{
            font-size: 18px;
            color: {colors['source']};
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            <div class="emoji-container">{card.emoji}</div>
            <div class="title-container">
                <div class="title">{card.title}</div>
                <div class="title-cn">{card.title_cn}</div>
            </div>
        </div>

        <div class="content">
            <div class="text">{card.content}</div>
            <div class="text-cn">{card.content_cn}</div>

            <div class="takeaway">
                <div class="takeaway-label">Key Takeaway / 要点</div>
                <div class="takeaway-text">{card.takeaway}</div>
                <div class="takeaway-cn">{card.takeaway_cn}</div>
            </div>
        </div>

        <div class="footer">
            <div class="source">Source: {card.source}</div>
            <div class="brand">Nutrition News</div>
        </div>
    </div>
</body>
</html>"""
    return html


def parse_markdown(md_path: str) -> List[NewsCard]:
    """Parse existing nutrition-news.md file to extract cards."""
    cards = []

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all news-card divs
    card_pattern = re.compile(
        r'<div class="news-card"[^>]*data-date="([^"]*)"[^>]*data-emoji="([^"]*)"[^>]*data-title="([^"]*)"[^>]*data-title-cn="([^"]*)"[^>]*>.*?'
        r'<p>(.*?)</p>.*?'
        r'<div class="content-cn">(.*?)</div>.*?'
        r'<div class="takeaway"><strong>Takeaway:</strong>\s*(.*?)</div>.*?'
        r'<div class="takeaway-cn"><strong>要点：</strong>\s*(.*?)</div>.*?'
        r'<div class="source">Source/来源:\s*<a href="([^"]*)">(.*?)</a>',
        re.DOTALL
    )

    for match in card_pattern.finditer(content):
        date, emoji, title, title_cn, text, text_cn, takeaway, takeaway_cn, source_url, source = match.groups()

        cards.append(NewsCard(
            emoji=emoji,
            title=title,
            title_cn=title_cn,
            content=text.strip(),
            content_cn=text_cn.strip(),
            takeaway=takeaway.strip(),
            takeaway_cn=takeaway_cn.strip(),
            source=source.strip(),
            source_url=source_url.strip(),
            date=date
        ))

    return cards


def load_from_json(json_data: Union[dict, list]) -> List[NewsCard]:
    """Load cards from JSON data."""
    cards = []

    # Handle both list and dict with 'cards' key
    items = json_data if isinstance(json_data, list) else json_data.get('cards', [])

    for item in items:
        cards.append(NewsCard(
            emoji=item.get('emoji', '📰'),
            title=item.get('title', ''),
            title_cn=item.get('title_cn', ''),
            content=item.get('content', ''),
            content_cn=item.get('content_cn', ''),
            takeaway=item.get('takeaway', ''),
            takeaway_cn=item.get('takeaway_cn', ''),
            source=item.get('source', ''),
            source_url=item.get('source_url', ''),
            date=item.get('date', datetime.now().strftime('%Y-%m-%d'))
        ))

    return cards


async def render_card_to_image(html: str, output_path: str) -> None:
    """Render HTML to PNG image using Playwright."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': CARD_WIDTH, 'height': CARD_HEIGHT})

        await page.set_content(html)
        # Wait for fonts to load
        await page.wait_for_timeout(500)

        await page.screenshot(path=output_path, type='png')
        await browser.close()


async def render_cards_batch(cards: List[NewsCard], output_dir: str, style: str = "morandi") -> List[str]:
    """Render multiple cards efficiently with a single browser instance."""
    output_paths = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': CARD_WIDTH, 'height': CARD_HEIGHT})

        for i, card in enumerate(cards):
            html = generate_html(card, style)
            await page.set_content(html)
            await page.wait_for_timeout(300)  # Wait for fonts

            # Generate filename
            safe_title = re.sub(r'[^\w\s-]', '', card.title)[:30].strip().replace(' ', '-')
            filename = f"{card.date}_{i+1:02d}_{safe_title}.png"
            output_path = os.path.join(output_dir, filename)

            await page.screenshot(path=output_path, type='png')
            output_paths.append(output_path)
            print(f"Generated: {filename}")

        await browser.close()

    return output_paths


def main():
    parser = argparse.ArgumentParser(description='Generate XHS card images from nutrition news')
    parser.add_argument('--input', '-i', type=str, help='JSON file with news data')
    parser.add_argument('--output', '-o', type=str, default='./xhs_cards', help='Output directory')
    parser.add_argument('--date', '-d', type=str, help='Filter by date (YYYY-MM-DD)')
    parser.add_argument('--parse-md', type=str, help='Parse existing nutrition-news.md file')
    parser.add_argument('--style', '-s', type=str, default='morandi',
                        choices=['morandi', 'vibrant', 'minimal'], help='Card style')

    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    # Load cards
    cards = []

    if args.parse_md:
        print(f"Parsing markdown: {args.parse_md}")
        cards = parse_markdown(args.parse_md)
    elif args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        cards = load_from_json(json_data)
    else:
        # Read from stdin
        json_data = json.load(sys.stdin)
        cards = load_from_json(json_data)

    if not cards:
        print("No cards found!")
        sys.exit(1)

    # Filter by date if specified
    if args.date:
        cards = [c for c in cards if c.date == args.date]
        if not cards:
            print(f"No cards found for date: {args.date}")
            sys.exit(1)

    print(f"Found {len(cards)} cards")
    print(f"Style: {args.style}")
    print(f"Output: {args.output}")
    print("-" * 40)

    # Render cards
    output_paths = asyncio.run(render_cards_batch(cards, args.output, args.style))

    print("-" * 40)
    print(f"Generated {len(output_paths)} images in {args.output}/")

    return output_paths


if __name__ == '__main__':
    main()
