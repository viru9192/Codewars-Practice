def sum_digits(number):
    total = 0
    split = (int(n) for n in str(abs(number)))
    for i in split:
        total += i
    return total
        