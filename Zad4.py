alfabet = ["a","b","c","d","e","f","g",
           "h","i","j","k","l","m","n",
           "o","p","q","r","s","t","u","v","w","x","y","z"]
# 26 litery
zdanie = str(input("Wpisz zdanie bez polskich znaków "))
litery = []
for litera in zdanie:
    if litera not in litery:
        if litera == " ":
            continue
        else:
            litery.append(litera.lower())
print("Lista liter w zdaniu",litery)
print("Alfabetycznie",sorted(litery))
roznica_liter = [r_litera for r_litera in alfabet if r_litera not in litery ]
print("Różnica",roznica_liter)