def validate_article(article, article_type="rss"):
    content = article.get("content", "")
    tags = article.get("tags", [])
    flags = []

    # Always check for insurance relevance
    if "insurance" not in content.lower():
        flags.append("May lack insurance relevance")

    # Only check for Hyderabad context in recent or historic articles
    if article_type in ["recent", "historical"] and "Hyderabad" not in content:
        flags.append("Missing location context: Hyderabad")

    confidence_score = 100 - (len(flags) * 20)

    return {
        "confidence": confidence_score,
        "flags": flags
    }
