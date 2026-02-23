def find_even_index(arr):
    total = sum(arr)
    left_arr = 0
    
    for i in range(len(arr)):
        right_arr = total - left_arr - arr[i]
        
        if left_arr == right_arr:
            return i
        
        left_arr += arr[i]
        
    return -1
            