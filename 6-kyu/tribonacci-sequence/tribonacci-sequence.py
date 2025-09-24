def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < 3:
        return signature[:n]
    
    final = signature[:]
    
    while len(final) < n:
        final.append(sum(final[-3:]))
    return final