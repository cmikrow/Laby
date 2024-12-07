def oblicz_potege(a, n):
    if n == 0:
        return 1
    return a * oblicz_potege(a,n-1)
print(oblicz_potege(2,10))