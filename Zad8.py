def czy_palindrom(napis):
    if len(napis) == 1 or len(napis) == 0:
        return True
    if napis[0] != napis[-1]:
        return False
    return czy_palindrom(napis[1:-1])
print(czy_palindrom("kajak"))
print(czy_palindrom("radar"))
print(czy_palindrom("hello"))
print(czy_palindrom("agata"))
print(czy_palindrom(""))