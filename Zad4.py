import random
a = random.randint(1,100)
licznik = 1
b = int(input("Wprowadź b"))
while b!=a:
    licznik+=1
    if b>a:
        print("Liczba b > a")
    else:
        print("Liczba b < a")
    b = int(input("Wprowadź b"))
print(a)
print(licznik)