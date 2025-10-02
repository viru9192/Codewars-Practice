def order(sentence):
    if not sentence:
        return ""
    
    words = sentence.split()
    result =[]
    
    for i in range(1, len(words) + 1):
        for w in words:
            if str(i) in w:
                result.append(w)
                break
    return " ".join(result)