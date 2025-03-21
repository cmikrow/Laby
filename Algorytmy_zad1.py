import math
a=int(input("Wprowadź a,różne od 0"))
while a == 0:
    print("Wprowadź ponownie a")
    a = int(input("Wprowadź a,różne od 0"))
b=int(input("Wprowadź b"))
c=int(input("Wprowadź c"))
delta=b**2-4*a*c
if delta>0:
    delta_pierwiastek=delta**(1/2)
    b=-b
    x01=b+delta_pierwiastek
    x1=x01/(2*a)
    print("x1 to:",x1)
    x02=b-delta_pierwiastek
    x2=x02/(2*a)
    print("x2 to:",x2)
elif delta==0:
    b = -b
    x00 = b
    x0 = x00 / (2 * a)
    print("x0 to:",x0)
else:
    print("Ta funkcja kwardatowa nie mam miejsc zerowych")