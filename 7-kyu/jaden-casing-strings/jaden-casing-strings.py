def to_jaden_case(string):
    return " ".join(word[0].upper() + word[1:].lower() for word in string.split())