def duplicate_count(text):
    t_lower = text.lower()
    count = 0
    for char in set(t_lower):
        if t_lower.count(char) > 1:
            count += 1
    return count