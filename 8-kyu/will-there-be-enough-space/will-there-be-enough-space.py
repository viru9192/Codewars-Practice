def enough(cap, on, wait):
    total = on + wait
    if cap < total:
        return total - cap
    else:
        return 0