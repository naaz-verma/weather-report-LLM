def format_output(article, style="bullet"):
    parts = [
        f"🔹 **Title**: {article['title']}",
        f"🔹 **Summary**: {article['summary']}",
        f"🔹 **Tags**: {', '.join(article.get('tags', []))}",
        f"🔹 **Forecast Consistency**: {article['forecast_consistency']}",
        "🔹 **References:**",
        *[f"    - {ref}" for ref in article['references']],
        f"🔹 **Content Validation**: {article['validation']}",
    ]
    return "\n".join(parts)
