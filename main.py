from dotenv import load_dotenv
from fetch_news import fetch_climate_news
from format_utils import (
    format_news_articles,
    extract_news_text,
    structure_the_response
)
from reference_utils import find_research_references_correlating_with_each_news_snnipets
from summarizer import summarize_text
import os
from classifier import classify_article
from analyze_forecast import analyze_forecast




load_dotenv()

def main():
    # Step 1: Fetch
    articles = fetch_climate_news()
    print("\n[+] Raw Articles:\n", format_news_articles(articles))

    try:
        # Step 2: Summarize
        content = extract_news_text(articles)
        summary = summarize_text(content)
        print("\n[+] HuggingFace Summary:\n", summary)

        # Step 3: Structure
        structured = structure_the_response(articles)

        # Classify each summary
        for article in structured:
            summary = article.get("summary", "")
            content = article.get("content", summary)
            url = article.get("url", "")
            
            article['tags'] = classify_article(summary)
            article["forecast_consistency"] = analyze_forecast(content, url)


        # Step 4: Research References
        enriched_articles, references = find_research_references_correlating_with_each_news_snnipets(structured)

        # Final Output
        for item in enriched_articles:
            print(f"\nTitle: {item['title']}")
            print(f"Summary: {item['summary']}")
            print(f"Tags: {item.get('tags', [])}")
            print(f"Forecast Match: {item['forecast_consistency']}")
            print(f"References: {item['references']}")

    except Exception as e:
        print("[!] Summarization error:", str(e))

if __name__ == "__main__":
    main()
