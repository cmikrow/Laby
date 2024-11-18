ulice = ["Jagodowa","Lipowa","Kiwatowa","Kasztanowa","Polna"]
bloki = [1,2,3,4,5]
lokale = [1,2,3,4,5,6,7,8,9,10]
for ulica in ulice:
    for blok in bloki:
        for lokal in lokale:
            print(f"{ulica} {blok} blok , {lokal:2} lokal")