n = int(input("Podaj liczbe studentów w grupie"))
i = 0
oceny_studentów = 0
while i < n:
    ocena_studenta = int(input(f"Podaj ocene {i+1} studenta "))
    if 1 <= ocena_studenta <= 100:
        oceny_studentów += ocena_studenta
        i += 1
    else:
        print("Niepoprawna punktacja")
        continue
if n == i:
    oceny_studentów /= n
    print(f"{oceny_studentów:.2f} to średnia ocen studentów w grupie")