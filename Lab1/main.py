from fractions import Fraction

# 1. Utwórz skrypt 'main.py' zawierający definicję funkcji sum(arg1, arg2), która oblicza, a następnie zwraca, wartość arg1 + arg2

def sum(arg1, arg2):
    try:
        # ISINSTANCE(OBIEKT, TYP) sprawdza czy obiekt jest tego typu, o który pytamy. Zwraca True lub False
        if not isinstance(arg1, complex) and not isinstance(arg1, Fraction): 
            arg1 = float(arg1)
        
    except:
        raise ValueError
    
    try:
        if not isinstance(arg2, complex) and not isinstance(arg2, Fraction):
            arg2 = float(arg2)
    except:
        raise ValueError
    
    return arg1 + arg2

# 2. Wywołaj tę funkcję (w skrypcie) z dwoma argumentami będącymi liczbami całkowitymi oraz wypisz, na ekranie, wynik jej działania następująco: suma = <wynikSumowania>

wynikSumowania = sum(1, 8)
print("suma = " + str(wynikSumowania))

# 3. Wykonaj skrypt — python3 main.py

# 4. Uruchom konsolę Python — python3

# 5. Sprawdź wynik ewaluacji poniższych wyrażeń:
#   2 + 2 => 4
#   2 + 2.0 => 4.0
#   2 + '2' => TypeError: unsupported operand type(s) for +: 'int' and 'str'
#   '2' + '2' => '22'
#   zmienna = 2
#   type(zmienna) => <class 'int'>
#   zmienna = '2' 
#   type(zmienna) => <class 'str'>

# Na podstawie otrzymanych wyników wywnioskuj jakie rodzaje typowania oferuje Python: silne, słabe, statyczne, dynamiczne
#       SILNE I DYNAMICZNE

# 6. Spowoduj, aby skrypt 'main.py' wypisywał wartość zmiennej __name__ w postaci następującego łańcucha: __name__ = <wartośćZmiennej>

print("__name__ = " + __name__)


# 7. Wywołaj komendę python3 main.py i zobacz jaka jest wartość tej zmiennej
#       Wartość zmiennej to: __main__

# 8. Uruchom konsolę Python, a następnie wykonaj komendę import main i ponownie sprawdź, jaka jest wartość ww. zmiennej
#       main
# Zobacz czy napis suma = <wynikSumowania> pojawia się przy kolejnych wywołaniach import main
#       nie

# 9. Korzystając z informacji zawartych w artykule, zmodyfikuj skrypt tak, aby nie był "gadatliwy" w środowisku testowym:
#       jeżeli skrypt jest uruchamiany bezpośrednio, tzn. z linii komend, to funkcja sum(arg1,arg2) ma być wywoływana, czyli skrypt ma wypisywać wynik sumowania
#       jeżeli skrypt jest ładowany jako moduł, tj. za pomocą import, to funkcja nie ma być wywoływana

if __name__ == '__main__':
    print("Bezpośrednio")
    print("suma = " + str(sum(8, '5')))
    
else:
    print("Pośrednio")