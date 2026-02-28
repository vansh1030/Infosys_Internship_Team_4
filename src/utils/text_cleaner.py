def clean_chat(text):
    # Basic normalization
    text = text.strip()
    text = text.replace("\n\n", "\n")
    return text