def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    
    for _ in range(n):
        half = len(encrypted_text) // 2
        odd = encrypted_text[:half]
        even = encrypted_text[half:]
        
        encrypted_text = "".join(
            even[i//2] if i % 2 == 0 else odd[i//2]
            for i in range(len(encrypted_text))
        )
    
    return encrypted_text
​
​
def encrypt(text, n):
    if not text or n <= 0:
        return text
    
    for _ in range(n):
        odd = text[1::2]
        even = text[0::2]
        text = odd + even
    
    return text