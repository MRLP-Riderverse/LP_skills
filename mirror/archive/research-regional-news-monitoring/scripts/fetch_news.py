#!/usr/bin/env python3
"""
Fetch and parse regional news from RSS feeds and web sources.
Designed for Acadian/NB region but adaptable to any region.

Usage:
    python fetch_regional_news.py --region acadian --days 7
    python fetch_regional_news.py --rss "https://news.google.com/rss/search?q=..." --days 7
"""

import argparse
import re
from datetime import datetime
from hermes_tools import terminal

# Region configurations
REGIONS = {
    'acadian': {
        'rss_urls': [
            'https://news.google.com/rss/search?q=Acadie+Nouveau-Brunswick&hl=fr-CA&gl=CA&ceid=CA:fr',
            'https://news.google.com/rss/search?q=Acadie+New+Brunswick&hl=en-CA&gl=CA&ceid=CA:en',
        ],
        'web_urls': [
            'https://www.cbc.ca/news/canada/new-brunswick',
            'https://radio-canada.ca/aci',
        ],
        'keywords': ['Acadie', 'Acadien', 'Caraquet', 'Bathurst', 'Péninsule', 'Shippagan', 'Tracadie']
    }
}

def fetch_rss(rss_url):
    """Fetch and parse RSS feed items."""
    result = terminal(f'curl -s -A "Mozilla/5.0" -L "{rss_url}" --connect-timeout 20')
    content = result.get('output', '')
    
    if not content or len(content) < 500:
        return []
    
    items = re.findall(r'<item>(.*?)</item>', content, re.DOTALL)
    articles = []
    
    for item in items:
        title_match = re.search(r'<title>([^<]+)', item)
        link_match = re.search(r'<link>([^<]+)', item)
        date_match = re.search(r'<pubDate>([^<]+)', item)
        
        if not title_match:
            continue
            
        title = title_match.group(1).strip()
        link = link_match.group(1) if link_match else '#'
        date_str = date_match.group(1) if date_match else ''
        
        # Parse date
        days_ago = 999
        try:
            pub_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
            days_ago = (datetime.now() - pub_date).days
        except:
            pass
        
        articles.append({
            'title': title,
            'link': link,
            'date': date_str,
            'days_ago': days_ago,
            'source': 'RSS'
        })
    
    return articles

def fetch_web_headlines(url):
    """Fetch headlines from web page JSON metadata."""
    result = terminal(f'curl -s -A "Mozilla/5.0" -L "{url}" --connect-timeout 15')
    content = result.get('output', '')
    
    if not content:
        return []
    
    # Try CBC pattern (headline)
    headlines = re.findall(r'"headline"\s*:\s*"([^"]+)"', content)
    
    # Try Radio-Canada pattern (title)
    if not headlines:
        headlines = re.findall(r'"title"\s*:\s*"([^"]+)"', content)
    
    articles = []
    for title in headlines:
        # Unescape Unicode
        title = (title.replace('\\u00e9', 'é').replace('\\u00e8', 'è')
                .replace('\\u00ea', 'ê').replace('\\u00e0', 'à')
                .replace('\\u00f4', 'ô').replace('\\u00ee', 'î')
                .replace('&nbsp;', ' '))
        
        articles.append({
            'title': title,
            'link': url,
            'date': '',
            'days_ago': 0,
            'source': 'WEB'
        })
    
    return articles

def categorize_story(title):
    """Categorize a story based on keywords."""
    title_lower = title.lower()
    
    categories = {
        'Economic': ['économ', 'pêch', 'homard', 'crabe', 'tourisme', 'emploi', 'entreprise', 'commerce', 'budget', 'trades', 'workforce'],
        'Infrastructure': ['infrastruct', 'eau', 'électric', 'route', 'connect', 'internet', 'vet', 'health', 'dental'],
        'Cultural': ['culture', 'identité', 'langue', 'français', 'acadie', 'acadien', 'fête', 'festival', 'hockey', 'election'],
        'Environmental': ['climat', 'météo', 'forêt', 'environ', 'pluie', 'érosion', 'whale', 'plover', 'conservation']
    }
    
    matched = []
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw.lower() in title_lower:
                matched.append(cat)
                break
    
    return matched[0] if matched else 'General'

def main():
    parser = argparse.ArgumentParser(description='Fetch regional news')
    parser.add_argument('--region', choices=REGIONS.keys(), help='Region to fetch news for')
    parser.add_argument('--rss', help='Custom RSS URL')
    parser.add_argument('--days', type=int, default=7, help='Filter to stories from last N days')
    parser.add_argument('--format', choices=['text', 'json'], default='text', help='Output format')
    
    args = parser.parse_args()
    
    all_articles = []
    
    # Fetch from RSS
    if args.rss:
        articles = fetch_rss(args.rss)
        all_articles.extend(articles)
    elif args.region:
        config = REGIONS[args.region]
        
        # Fetch from RSS feeds
        for rss_url in config['rss_urls']:
            articles = fetch_rss(rss_url)
            all_articles.extend(articles)
        
        # Fetch from web sources
        for web_url in config['web_urls']:
            articles = fetch_web_headlines(web_url)
            all_articles.extend(articles)
    
    # Filter by days
    recent = [a for a in all_articles if a['days_ago'] <= args.days]
    
    # Sort by date
    recent.sort(key=lambda x: x['days_ago'])
    
    # Output
    if args.format == 'json':
        import json
        print(json.dumps(recent, indent=2, ensure_ascii=False))
    else:
        print(f"=== Regional News ({len(recent)} stories from last {args.days} days) ===\n")
        for i, a in enumerate(recent[:20], 1):
            days = a['days_ago']
            date_str = f"{days}d ago" if days < 999 else "Unknown"
            cat = categorize_story(a['title'])
            print(f"{i}. [{date_str}] [{cat}]")
            print(f"   {a['title'][:90]}")
            print(f"   Source: {a['source']}")
            print()

if __name__ == '__main__':
    main()
