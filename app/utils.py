def get_priority(text):
    text = text.lower()

    if "urgent" in text or "not working" in text:
        return "High"
    elif "issue" in text or "problem" in text:
        return "Medium"
    else:
        return "Low"