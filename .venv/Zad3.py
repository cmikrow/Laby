def powitanie(imie="Użytkowniku",jezyk="polski"):
    if jezyk=="polski":
        print(f"Cześć, {imie}")
    elif jezyk=="angielski":
        print(f"Hello, {imie}")
    elif jezyk=="niemiecki":
        print(f"Guten Tag, {imie}")
    else:
        print(f"Witaj, {imie}")
imie= input("Podaj imie")
jezyk= input("Podaj język")
powitanie(imie,jezyk)