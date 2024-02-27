#-*-coding: utf-8-*-
import sys


#print('Ładowanie modułu "{0}"'.format(__name__))
############################################

def wypisz():
    sep = ""
    for key, value in slownik.items() :
        print ('{}{}:{}'.format(sep, key, value), end = "", sep = "")
        sep = ","

    #print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))

############################################
#print('Załadowano moduł "{0}"'.format(__name__))

# 1. Sprawdź (w konsoli) działanie następujących instrukcji:
#       >>> import lista
#       Ładowanie modułu "lista"
#       Załadowano moduł "lista"
#       >>> import lista
#       >>> import slownik
#       Ładowanie modułu "slownik"
#       Załadowano moduł "slownik"
#       >>> import slownik
#       >>> lista.wypisz()
#       Wywołano funkcję "wypisz()" modułu "lista"
#       >>> slownik.wypisz() 
#       Wywołano funkcję "wypisz()" modułu "slownik"

# 2. Zmodyfikuj zawartość ww. plików:
#       Plik "lista.py" ma zawierać definicję listy o nazwie lista, a plik "slownik.py", definicję słownika o nazwie slownik — zarówno lista jak i słownik, początkowo, nie zawierają żadnych elementów.

slownik = {}

#       Każdy z plików powinien zawierać dwie funkcje: zapisz() oraz wypisz()

def zapisz():
    for char in sys.argv[2]:
        try:
            int(char)
            if char not in slownik:
                slownik[char] = 1
            else:
                slownik[char] += 1
        except:
            pass


#       Pierwsza z tych funkcji aktualizuje listę / słownik informacjami o ilości wystąpień poszczególnych liczb zawartych w linii komend, zaś druga zwraca zawartość tej listy / słownika w postaci łańcucha znaków: "liczba1:liczbaWystąpień,liczba2:liczbaWystąpień, ...".

