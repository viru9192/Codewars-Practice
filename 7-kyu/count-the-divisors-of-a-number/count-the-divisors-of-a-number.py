def divisors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
            i += 1
            
    return len(result)