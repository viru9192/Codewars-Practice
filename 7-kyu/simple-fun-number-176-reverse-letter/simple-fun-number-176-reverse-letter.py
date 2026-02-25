def reverse_letter(st):
    new = "".join(ch for ch in st if ch.isalpha())
    return new[::-1]