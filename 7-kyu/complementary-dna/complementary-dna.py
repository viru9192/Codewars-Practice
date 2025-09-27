def DNA_strand(dna):
    result = ""
    for char in dna:
        if char == 'A':
            result += 'T'
        elif char == 'T':
            result += 'A'
        elif char == 'G':
            result += 'C'
        elif char == 'C':
            result += 'G'
    return result