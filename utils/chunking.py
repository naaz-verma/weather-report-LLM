def chunk_text(text, max_tokens=1000):
    sentences = text.split('. ')
    chunks, current_chunk = [], ""
    for sent in sentences:
        if len(current_chunk) + len(sent) < max_tokens:
            current_chunk += sent + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sent + ". "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks
