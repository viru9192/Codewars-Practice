def title_case(title, minor_words=''):
    if not title:
        return ""
    
    minor = set(minor_words.lower().split())
    words = title.lower().split()
    
    result = []
    
    for i, word in enumerate(words):
        if i == 0 or word not in minor:
            result.append(word.capitalize())
        else:
            result.append(word)
            
    return " ".join(result)