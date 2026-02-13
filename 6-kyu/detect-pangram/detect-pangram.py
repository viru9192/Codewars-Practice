def is_pangram(st):
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in st.lower():
            return False
        
    return True