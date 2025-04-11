from transformers import pipeline
from utils.chunking import chunk_text

def summarize_text(text: str, model_name="facebook/bart-large-cnn", max_chunk_tokens=1000):
    summarizer = pipeline("summarization", model=model_name)
    chunks = chunk_text(text, max_tokens=max_chunk_tokens)
    summaries = summarizer(chunks, max_length=130, min_length=30, do_sample=False)
    return "\n".join([s['summary_text'] for s in summaries])
