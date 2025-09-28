def dig_pow(n, p):
    total = 0
    org = n
    while n:
        d = n % 10
        curr_p = p + len(str(n)) - 1
        total += d ** curr_p
        n //= 10
    return total // org if total % org == 0 else -1