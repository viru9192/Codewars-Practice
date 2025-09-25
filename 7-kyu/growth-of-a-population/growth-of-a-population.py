def nb_year(p0, percent, aug, p):
    years = 0
    pop = p0
    while pop < p:
        pop = int(pop + pop * (percent / 100) + aug)
        years += 1
    return years