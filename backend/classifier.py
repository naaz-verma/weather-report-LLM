# classifier.py
from transformers import pipeline

# Define your domain categories
DOMAIN_LABELS = ["Climate Risk", "InsureTech", "Policies", "Impact on Underwriting"]

# Load once and reuse
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_article(summary: str) -> list:
    result = classifier(summary, candidate_labels=DOMAIN_LABELS, multi_label=True)
    return [label for label, score in zip(result["labels"], result["scores"]) if score > 0.4]  # threshold can be tuned
