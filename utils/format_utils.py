def format_news_articles(articles):
    formatted = ""
    for i, article in enumerate(articles, 1):
        title = article.get("title", "No Title")
        content = article.get("content", "No Content")
        url = article.get("url", "")
        formatted += f"Article {i}:\nTitle: {title}\nContent: {content[:500]}...\nURL: {url}\n\n"
    return formatted

def extract_news_text(articles, limit=800):
    return "\n\n".join([a.get("content", "")[:limit] for a in articles])

def structure_the_response(response, *args):
    if isinstance(response, list):
        return [
            {
                "title": article.get("title"),
                "url": article.get("url"),
                "content": article.get("content", "")[:1000],
                "summary": article.get("content", "")[:300],  # quick preview for ref
            }
            for article in response
        ]
    elif isinstance(response, str):
        return {"summary": response}
    else:
        return {"error": "Unrecognized response format"}