def tower_builder(n_floors):
    result = []
    for i in range(n_floors):
        spaces = " " * (n_floors - i - 1)
        stars = "*" * (2 * i + 1)
        result.append(spaces + stars + spaces)
        
    return result