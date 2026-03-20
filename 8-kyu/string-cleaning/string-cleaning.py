def string_clean(s):
    result = ''
    for ch in s:
        if not ch.isdigit():
            result += ch
    return result