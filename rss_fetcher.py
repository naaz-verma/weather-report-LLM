import feedparser
from newspaper import Article
from typing import List, Dict
from urllib.parse import urlparse

def fetch_from_rss(feed_urls: List[str], max_articles: int = 5) -> List[Dict]:
    articles = []
    seen_titles = set()

    for feed_url in feed_urls:
        try:
            feed = feedparser.parse(feed_url)
        except Exception as e:
            print(f"[!] Failed to parse feed: {feed_url} — {e}")
            continue

        for entry in feed.entries:
            title = entry.title
            if title in seen_titles:
                continue  # skip duplicates

            url = entry.link
            try:
                article_obj = Article(url)
                article_obj.download()
                article_obj.parse()
                full_text = article_obj.text
            except Exception as e:
                print(f"[!] Failed to fetch article: {url} — {e}")
                full_text = "No Content..."

            article = {
                "title": title,
                "url": url,
                "summary": entry.get("summary", ""),
                "published": entry.get("published", ""),
                "content": full_text
            }
            articles.append(article)
            seen_titles.add(title)

            if len(articles) >= max_articles:
                return articles  # Stop once max_articles is reached

    return articles
