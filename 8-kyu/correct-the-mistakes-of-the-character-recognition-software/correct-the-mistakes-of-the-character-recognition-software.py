def correct(s):
    result = []
    for ch in s:
        if ch == '5':
            result.append('S')
        elif ch == '0':
            result.append('O')
        elif ch == '1':
            result.append('I')
        else:
            result.append(ch)
    return ''.join(result)