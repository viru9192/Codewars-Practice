def increment_string(string):
    num = ""
    
    for ch in reversed(string):
        if ch.isdigit():
            num = ch + num
        else:
            break
​
    if num == "":
        return string + "1"
​
    new = str(int(num) + 1).zfill(len(num))
    return string[:-len(num)] + new