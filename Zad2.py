imiona1 = ["Tomisław","Apoloniusz","Curuś","Bachleda"]
print(sorted(imiona1))
imiona2 = ("Farel","Bomba")
imiona1.extend(imiona2)
imiona1.pop(5)
print(imiona1)
imiona1.insert(2,"Grażyna")
print(imiona1)
imiona1.reverse()
imiona3 = imiona1
imiona4 = imiona1 + imiona3
print(imiona4)