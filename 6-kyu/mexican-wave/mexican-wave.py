def wave(people):
    result = []
    for i, ch in enumerate(people):
        if ch == ' ':
            continue
        
        wave = people[:i] + ch.upper() + people[i+1:]
        result.append(wave)
    
    return result