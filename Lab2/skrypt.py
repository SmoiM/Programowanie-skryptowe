#-*-coding: utf-8-*-

import lista, slownik
import sys
# Proszę utworzyć skrypt i użyć w nim, odpowiednio, funkcji z pliku "lista.py" / "slownik.py", w zależności od opcji z którą skrypt został wywołany ('--lista' / '--slownik')

match sys.argv[2]: 
    case '--lista':
        lista.zapisz()
        lista.wypisz()
    case '--slownik':
        slownik.zapisz()
        slownik.wypisz()
