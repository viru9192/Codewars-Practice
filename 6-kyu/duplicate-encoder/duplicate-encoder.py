def duplicate_encode(word):
    new_w = word.lower()
    result = ""
    for ch in new_w:
        if new_w.count(ch) > 1:
            result += ")"
        else:
            result += "("
        
    return result