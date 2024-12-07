imie0 = str(input("Wpisz swoje imie "))
print(f"Witaj {imie0}")
wiek = int(input("Podaj wiek "))
print(f"Twój wiek {wiek}")
imie1 = str(input("Podaj swoje imie "))
nazwisko1 = str(input("Podaj swoje nazwisko "))
print(imie1[0].capitalize(),nazwisko1[0].capitalize())
lancuch1 = [1,2]
lancuch2 = [3,4,5,6]
lancuch0 = lancuch1*5
print(lancuch0)
lancuch3 = lancuch1 + lancuch2
print(lancuch3)
p_polowa = int(len(lancuch1)/2)
d_polowa = int(len(lancuch2)/2)
lancuch4 = lancuch1[:p_polowa] + lancuch2[d_polowa:]
print(lancuch4)