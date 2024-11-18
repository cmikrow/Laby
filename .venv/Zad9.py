imie = str(input("Podaj imie"))
print(f"Witaj {imie.capitalize()}")

wiek = (input("Podaj wiek"))
print(f"Twój wiek to: {wiek}")

nazwisko = str(input("Podaj nazwisko"))
imied = str(input("Podaj imie"))
print(imied[0].capitalize(),nazwisko[0].capitalize())

lancuch = input("Podaj łańcuch do powtórzenia x5")
print(lancuch_a*5)

lancuch_x = input("Podaj łańcuch 1")
lancuch_y = input("Podaj łańcuch 2")
lancuch_z = "".join([lancuch_x,lancuch_y])
print(lancuch_z)

lancuch_a = input("Podaj łańcuch 1")
lancuch_b = input("Podaj łańcuch 2")
lancuch_c = "".join([lancuch_a[:len(lancuch_a)//2],lancuch_b[:len(lancuch_b)//2]])
print(lancuch_c)
