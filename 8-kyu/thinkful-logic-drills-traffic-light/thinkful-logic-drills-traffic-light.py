def update_light(current):
    chain = {
        'green' : 'yellow',
        'yellow' : 'red',
        'red' : 'green'
    }
    
    return chain[current]