def bmi(waga:float,wzrost:float):
    wynik=waga/(wzrost**2)
    if(wynik<18.5):
        print("niedowaga")
        print("Wskaźnik BMI {:.1f}".format(wynik))
    elif(18.5<wynik<24.9):
        print("pożądana masa ciała")
        print("Wskaźnik BMI {:.1f}".format(wynik))
    elif(25<wynik<29.9):
        print("nadwaga")
        print("Wskaźnik BMI {:.1f}".format(wynik))
    elif(30<wynik<34.9):
        print("otyłośc I stopnia")
        print("Wskaźnik BMI {:.1f}".format(wynik))
    elif(35<wynik<39.9):
        print("otyłośc II stopnia")
        print("Wskaźnik BMI {:.1f}".format(wynik))
    else:
        print("otyłośc III stopnia")
        print("Wskaźnik BMI {:.1f}".format(wynik))


koncowy_wynik=bmi(80,1.74)
# waga(kg) wzrost(m)