#-*-coding: utf-8-*-

#1. Stwórz skrypt oraz test weryfikujący poprawność działania tego skryptu. Skrypt, w oparciu o moduł re, rozpoznaje ciąg napisów (zawierających polskie znaki Unicode) wczytany z klawiatury (jeden napis w pojedynczej linii) i wypisuje rozpoznany napis wraz informacją o jego rodzaju (liczba lub wyraz), a w przypadku tekstu mieszanego, wypisuje tekst tworzący liczbę oraz tekst tworzący wyraz. Przykład działania:
# $ python3 skrypt.py
# Ala
#   Wyraz: Ala
# 1kota
#   Liczba: 1
#   Wyraz: kota
# oraz
#   Wyraz: oraz
# psów20
#   Wyraz: psów
#   Liczba: 20
# 50
#   Liczba: 50
# ^D

import re

def szukaj(napis):
    znajdz = re.compile('[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+|\d+') # | => lub; \d => cyfry [0-9]; + => najdłuższy możliwy ciąg znaków
    wynik = znajdz.findall(napis)
    odpowiedz = ""
    for wyraz in wynik:
        try:
            int(wyraz)
            #print("Liczba:", wyraz)
            odpowiedz += "Liczba: " + str(wyraz) + "\n"
        except:
            #print("Wyraz:", wyraz)
            odpowiedz += "Wyraz: " + wyraz + "\n"
    return odpowiedz
    

# if __name__ == '__main__':
#     while True:
#         napis = str(input())
#         szukaj(napis)
    