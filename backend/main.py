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
from analyze_forecast import analyze_forecast, match_news_with_forecast
from output_formatter import format_output
from validator import validate_article
from forecast_generator import generate_forecast
from save_dataset import save_to_dataset

load_dotenv()

def main(mode="historical", output_style="bullet"):
    # 🔁 Choose the mode: "recent", "historical", or "rss"
      # CHANGE THIS TO "historical" or "rss" when needed

    # Step 1: Fetch
    articles = fetch_climate_news(mode=mode)
    print(f"\n[+] Raw Articles ({mode}):\n", format_news_articles(articles))

    try:
        # Step 2: Summarize
        content = extract_news_text(articles)
        summary = summarize_text(content)
        print("\n[+] HuggingFace Summary:\n", summary)

        # Step 3: Structure
        structured = structure_the_response(articles)

        # Step 4: Classify + Validate + Forecast (if not RSS)
        for article in structured:
            summary = article.get("summary", "")
            content = article.get("content", summary)
            url = article.get("url", "")

            # Tagging always happens
            article['tags'] = classify_article(summary)

            # Only analyze forecast and validate if NOT RSS
            if mode in ["recent", "historical"]:
                article["forecast_consistency"] = analyze_forecast(content, url)
                article["validation"] = validate_article(article, article_type=mode)
            else:
                article["forecast_consistency"] = "N/A"
                article["validation"] = validate_article(article, article_type="rss")

        # Step 5: Research References
        enriched_articles, references = find_research_references_correlating_with_each_news_snnipets(structured)

        # Step 6: Output
         # or "json"
        if output_style == "bullet":
            for item in enriched_articles:
                formatted = format_output(item, style=output_style)
                print(formatted)
        else:
            for article in enriched_articles:
                print(f"\nTitle: {article['title']}")
                print(f"Summary: {article['summary']}")
                print(f"Tags: {article.get('tags', [])}")
                print(f"Forecast Match: {article['forecast_consistency']}")
                print(f"References: {article['references']}")
                print(f"Validation: {article['validation']}")
        
        return enriched_articles
        # # Step 7: Forecast matching and dataset saving (ONLY for recent/historical)
        # if mode in ["recent", "historical"]:
        #     forecast_df = generate_forecast()
        #     enriched_articles = match_news_with_forecast(enriched_articles, forecast_df)
        #     save_to_dataset(enriched_articles)
        #     print("[✔] Saved dataset to dataset.jsonl")

    except Exception as e:
        print("[!] Summarization error:", str(e))


if __name__ == "__main__":
    enriched_articles = main()  # Capture the return value
    if enriched_articles:
        save_to_dataset(enriched_articles)
    else:
        print("[!] No enriched articles returned from main()")
