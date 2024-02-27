#-*-coding: utf-8-*-
import sys

#print('Ładowanie modułu "{0}"'.format(__name__))
############################################

def wypisz():
    sep = ""
    for i in range(0, len(lista), 2):
        print ('{}{}:{}'.format(sep, lista[i], lista[i + 1]), end = "", sep = "")
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

lista = []

#       Każdy z plików powinien zawierać dwie funkcje: zapisz() oraz wypisz()

def zapisz():
    dane = list(set(sys.argv[2]))
    
    
    for char in dane:
        try:
            int(char)
            lista.append(char)
            lista.append(sys.argv[2].count("{}".format(char)))
        except:
            pass

#       Pierwsza z tych funkcji aktualizuje listę / słownik informacjami o ilości wystąpień poszczególnych liczb zawartych w linii komend, zaś druga zwraca zawartość tej listy / słownika w postaci łańcucha znaków: "liczba1:liczbaWystąpień,liczba2:liczbaWystąpień, ...".
#       UWAGA: Lista powinna być możliwie najkrótsza tzn. nie powinna przechowywać informacji o krotności jeżeli dana liczba nie występuje w ciągu wejściowym
