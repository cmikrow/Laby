from datetime import datetime,timedelta
czas_teraz = datetime.now()
print(f"Czas teraz:",czas_teraz.strftime("%Y-%m-%d"))
miesiace = ["styczeń","luty","maczec","kwiecień","maj","czerwic","lipiec","sierpień","wrzesień","pażdziernik","listopad","grudzień"]
def last_lab(y,m,d):
    lab = datetime(y,m,d)
    dni_od_lab = (czas_teraz - lab).days
    lab_data = f"{lab.year} {miesiace[lab.month - 1]} {lab.day}"
    print(f"Ostatnie laboratorium: {lab_data}")
    print(f"{dni_od_lab} dni od laboratorium")
def fut_kol(y,m,d):
    kol = datetime(y,m,d)
    dni_do_kol = (kol - czas_teraz).days
    kol_data = f"{kol.year} {miesiace[kol.month - 1]} {kol.day}"
    print(f"Kolokwium odbędzie się: {kol_data}")
    print(f"{dni_do_kol} dni do kolokwium")
fut_kol(2025,1,4)
last_lab(2024,12,15)