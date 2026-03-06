def number(lines):
    result = []
    for i, ch in enumerate(lines):
        result.append(f"{i+1}: {ch}")
    return result