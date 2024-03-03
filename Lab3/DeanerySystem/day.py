# Utwórz skrypt o nazwie 'day.py', który zawiera:
# Klasę o nazwie Day z siedmioma wartościami: MON, TUE, WED, THU, FRI, SAT oraz SUN — użyj modułu enum
# Funkcję nthDayFrom(n, day) zwracającą dzień tygodnia przesunięty o n w stosunku do day
# Metodę instancyjną, dla klasy Day, o nazwie difference(day) zwracają ilość dni, jaka dzieli dwa dni: dzień reprezentowany przez aktualny obiekt (self) oraz dzień reprezentowany przez obiekt day

from enum import Enum

class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def difference(self, day):
        n = day.value - self.value

        if n < -3:
            return n + 7
        elif n > 3:
            return n - 7
        else:
            return n 

def nthDayFrom(n, day):
    n = n + day.value
    
    while n < 1:
        n = n + 7
    while n > 7:
        n = n - 7
    
    return Day(n)


    


