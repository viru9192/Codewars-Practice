def replace_exclamation(st):
    vowel = 'aeiouAEIOU'
    result = ""
    for ch in st:
        if ch in vowel:
            result += "!"
        else:
            result += ch
            
    return result