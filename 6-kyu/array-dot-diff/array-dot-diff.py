def array_diff(a, b):
    result = []
    for x in a:
        if x not in b:
            result.append(x)
    return result