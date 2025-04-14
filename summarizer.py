from transformers import pipeline
from utils.chunking import chunk_text

def summarize_text(text: str, model_name="facebook/bart-large-cnn", max_chunk_tokens=1000):
    summarizer = pipeline("summarization", model=model_name)

    # Prepend the focused summarization instruction
    instruction = (
        "Summarize the following article with a focus on:\n"
        "- Climate trends in Hyderabad\n"
        "- Historical comparisons (1950–2020)\n"
        "- Insurance or economic impact if mentioned\n\n"
        "Article:\n"
    )

    full_text = instruction + text
    chunks = chunk_text(full_text, max_tokens=max_chunk_tokens)

    summaries = summarizer(chunks, max_length=130, min_length=30, do_sample=False)

    return "\n".join([s['summary_text'] for s in summaries])
