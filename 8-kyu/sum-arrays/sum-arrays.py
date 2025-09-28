def sum_array(a):
    total = 0
    for i in a:
        if a == []:
            return 0
        elif a != []:
            total += i
    return total