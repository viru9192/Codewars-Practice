def expanded_form(num):
    result= []
    n = str(num)
    
    for i,digit in enumerate(n):
        if digit != "0":
            value = digit + "0" * (len(n) - i - 1)
            result.append(value)
        
    return " + ".join(result)