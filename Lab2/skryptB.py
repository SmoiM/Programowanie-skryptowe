#-*-coding: utf-8-*-
import lista, slownik
from getopt import getopt
import sys

# Utwórz drugi skrypt — w oparciu o moduł getopt spowoduj, aby drugi skrypt, zamiast dwóch opcji ('--lista' lub '--slownik'), obsługiwał jedną: '--moduł=nazwa', gdzie nazwa to: lista lub słownik

# opts => [('--modul', 'slownik' lub 'lista')], czyli pierwszy parametr
# args => ['liczba podana przez użytkownika']
try:                                
    opts, args = getopt(sys.argv[1:], '', ["modul="])
    print(args)

except:        
    print("Niepoprawna skladnia. Pierwszym argumentem musi być '--modul=lista' lub '--modul=slownik'.")
    sys.exit() 

# Sprawdzamy, czy użytkownik podał pierwszy argument skryptu
if len(opts) == 0:
    print("Niepoprawna skladnia. Pierwszym argumentem musi być '--modul=lista' lub '--modul=slownik'.")
    sys.exit()       

# Sprawdzamy, czy użytkownik podał drugi argument skryptu
try:
    sys.argv[2]
except:
    print("Należy podać liczbę jako drugi argument")
    sys.exit()             

# opts[0][1] => wartosc po 'modul='
if opts[0][1] == 'lista':
    lista.zapisz()
    lista.wypisz()
elif opts[0][1] == 'slownik':
    slownik.zapisz()
    slownik.wypisz()
else:
    print("Niepoprawna skladnia. Pierwszym argumentem musi być '--modul=lista' lub '--modul=slownik'.")



