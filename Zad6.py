# Prostsze
# owoce = ('jabłko','banan','gruszka','banan','banan','malina')
# banany = owoce.count('banan')
# print("Liczba bananów",banany)
owoce = ('jabłko','banan','gruszka','banan','banan','malina')
n=0
for owoc in owoce:
    if owoc == 'banan':
        n+=1
    else:
        continue
print("Liczba bananów",n)
