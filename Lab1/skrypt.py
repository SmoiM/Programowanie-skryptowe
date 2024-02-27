import sys

# Napisz skrypt, który dla napisów zawartych w linii komend, sprawdza, który z nich jest liczbą pierwszą. Napisy, które nie tworzą prawidłowej liczby mają być ignorowane

def czyPierwsza(arg):
    if arg <= 1:
        return False
    
    for i in range(2, int(arg/2)):
        if arg % i == 0:
            return False

    return True

# sys.argv[1::] sprawdza wszystkie wpisane przez użytkownika wartości w terminalu 
for arg in sys.argv[1::]:
    try:
        # int(arg) zamieniamy arg ze stringa na inta
        if czyPierwsza(int(arg)) == True:
            print(arg)
    except:
        # pomijamy wyjątek i w ten sposób nie przerywamy działania programu przy podaniu wartości nie będącej liczbą
        pass 
