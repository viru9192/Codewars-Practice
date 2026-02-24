def capitals(word):
    result = []
    for i, ch in enumerate(word):
        if ch.isupper():
            result.append(i)
    return result