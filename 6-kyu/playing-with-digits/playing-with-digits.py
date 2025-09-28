def dig_pow(n, p):
    initial = n
    total = 0
    while n:
        rem = n % 10
        curr_p = p + len(str(n)) - 1
        total += rem ** curr_p
        n //= 10
    
    return total // initial if total % initial == 0 else -1
        