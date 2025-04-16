from transformers import pipeline
from utils.chunking import chunk_text

def summarize_text(text: str, model_name="facebook/bart-large-cnn", max_chunk_tokens=1000):
    summarizer = pipeline("summarization", model=model_name)

    # Prepend the focused summarization instruction
    instruction = (
    "Extract the following from the article:\n"
    "- Key facts and climate trends in Hyderabad\n"
    "- Historical comparisons (1950–2020) if available\n"
    "- Insurance or economic impact (if mentioned)\n"
    "- Any future risk or prediction\n\n"
    "Return the answer in JSON with keys: 'trends', 'comparisons', 'impacts', 'risks'.\n\n"
    "Article:\n"
)

    full_text = instruction + text
    chunks = chunk_text(full_text, max_tokens=max_chunk_tokens)

    summaries = summarizer(chunks, max_length=130, min_length=30, do_sample=False)

    return "\n".join([s['summary_text'] for s in summaries])
