# save_dataset.py
import json

def save_to_dataset(articles, filename="dataset.jsonl"):
    with open(filename, "w", encoding="utf-8") as f:
        for article in articles:
            entry = {
                "title": article.get("title"),
                "summary": article.get("summary"),
                "tags": article.get("tags", []),
                "references": article.get("references", []),
                "url": article.get("url"),
                "date_collected": article.get("date", None),
                "Forecast Match": article.get('forecast_consistency',None),
                "Validation": article.get('validation',None),
            }
            json.dump(entry, f)
            f.write("\n")
