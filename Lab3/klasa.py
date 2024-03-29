import sys
##################################
def methodBody(self, name):
    return "Wywołano metodę \033[{color}m{name:^17}\033[0m obiektu \033[{color}m{objectId}\033[0m".format(
            name     = name,
            color    = "38:5:{}".format(id(self) % 13 + 1),
            objectId = id(self)
        )
##################################
class Klasa(object):
    tab = [1, 2, 3]

    def __init__(self, tab, zmienna1, zmienna2):
        print(methodBody(self, sys._getframe().f_code.co_name))
        #Zdefiniuj dwie zmienne instancyjne o nazwach: _zmienna1 oraz __zmienna2, a następnie przypisz im (w treści metody __init__()) wartości określne w drugim i trzecim argumencie wywołania konstruktora
        self.tab = tab
        self._zmienna1 = zmienna1
        self.__zmienna2 = zmienna2

    def __del__(self):
        print(methodBody(self, sys._getframe().f_code.co_name))

    def __str__(self):
        return methodBody(self, sys._getframe().f_code.co_name)

    def __repr__(self):
        return methodBody(self, sys._getframe().f_code.co_name)

    def metodaInstancyjna(self):
        print(methodBody(self, sys._getframe().f_code.co_name))
        # Metoda metodaInstancyjna() ma wypisywać wartość obydwu zmiennych tab — zarówno instancyjnej, jak i klasowej
        print("Zmienna klasowa:", Klasa.tab)
        print("Zmienna instancyjna:", self.tab)

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę \033[1m{name:^17}\033[0m klasy   \033[1m{cls}\033[0m".format(
            name = sys._getframe().f_code.co_name,
            cls  = cls.__name__)
        )

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę \033[1m{name:^17}\033[0m klasy   \033[1m{cls}\033[0m".format(
            name = sys._getframe().f_code.co_name,
            cls  = __class__.__name__)
        )
##################################
print("Załadowano zawartość pliku '{name}'".format(name=__file__))

# Sprawdź jakie metody są w                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                del__      obiektu 2174221928144
# obiekt => Wywołano metodę     __repr__      obiektu 2174221928288
# print(obiekt) => Wywołano metodę      __str__      obiektu 2174221928288
# obiekt.metodaInstancyjna() => Wywołano metodę metodaInstancyjna obiektu 2174221928288
# Klasa.metodaKlasowa() => Wywołano metodę   metodaKlasowa   klasy   Klasa
# Klasa.metodaStatyczna() => Wywołano metodę  metodaStatyczna  klasy   Klasa

# Wpisz poniższy kod i sprawdź, czy wykonuje się on poprawnie:
# obiekt = Klasa([4, 5, 6], 10, 20)

# print(obiekt.tab)
# print(obiekt._zmienna1)
# print(obiekt.__zmienna2)

# Jak można zauważyć wykonanie kodu print(obiekt.__zmienna2) kończy się błędem. Korzystając z informacji przedstawionych na wykładzie lub w artykule wypisz wartość własności __zmienna2
#   >>> print(obiekt._Klasa__zmienna2) 
#   20