def queue_time(customers, n):
    
    if not customers:
        return 0
    
    
    tills = [0] * n
    
    for customer in customers:
        
        next_free = tills.index(min(tills))
        
        
        tills[next_free] += customer
    
    
    return max(tills)