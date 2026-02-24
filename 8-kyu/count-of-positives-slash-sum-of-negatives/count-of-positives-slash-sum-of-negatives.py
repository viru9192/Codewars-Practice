def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    
    if not arr:
        return []
    
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += i
        
    return [positive, negative]