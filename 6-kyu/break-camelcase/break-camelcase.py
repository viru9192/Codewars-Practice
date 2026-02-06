def solution(s):
    result = ""
    for ch in s:
        if ch.isupper():
            result += " " + ch
        else:
            result += ch
    return result