import math

def p_trojkata(a:int,b:int,c:int):
    try:
        if a+b<=c or a+c<=b or b+c<=a:
            raise ValueError("Boki nie spełniają nierówności trójkąta.")

        s = (a+b+c)/2
        pole = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Pole trójkąta wynosi: {:.2f}".format(pole))
    except ValueError as e:
        print(f"Błąd: {e}")

p_trojkata(3,4,5)