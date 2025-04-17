from typing import List, Dict
from keybert import KeyBERT

# Stubbed search — replace with real search if needed
def search_research_sources(keywords: List[str]) -> List[str]:
    return [f"https://scholar.google.com/scholar?q={kw}" for kw in keywords]

def extract_keywords(text: str) -> List[str]:
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=5,
        use_mmr=True,
        diversity=0.7
    )
    manual_boost = ["Hyderabad", "climate change", "heatwave", "insurance", "weather trends"]
    return list({kw[0] for kw in keywords}.union(manual_boost))


def find_research_references_correlating_with_each_news_snnipets(structured_response):
    enriched_responses = []
    references_dict = {}

    for risk in structured_response:
        summary = risk.get("summary") or risk.get("content", "")[:300]
        keywords = extract_keywords(summary)
        references = search_research_sources(keywords)
        risk['references'] = references
        enriched_responses.append(risk)
        references_dict[risk['title']] = references

    return enriched_responses, references_dict