# Klasę Term (w pliku 'term.py') w skład której wchodzą:
# trzy publiczne pola:
#   hour — godzina rozpoczęcia zajęć
#   minute — minuta rozpoczęcia zajęć
#   duration — czas trwania zajęć (w minutach)
# konstruktor, akceptujący dwa parametry: hour, minute, przypisujący ww. polom podane wartości, a polu duration wartość 90
# metodę __str__(), która zamienia termin na napis postaci: "godzina:minuta [czas trwania]", przykładowo dla: hour = 9 oraz minute = 45, napis powinien mieć postać "9:45 [90]"
# metoda earlierThan(termin), akceptującą inny obiekt tej klasy i zwracającą wartość True, jeżeli bieżący termin jest wcześniejszy niż ten podany
# metoda laterThan(termin), akceptującą inny obiekt tej klasy i zwracającą wartość True, jeżeli bieżący termin jest późniejszy niż ten podany
# metodę equals(termin), zwracającą wartość logiczną True, jeżeli obydwa terminy są sobie równe (godzina rozpoczęcia oraz czas trwania zajęć).
# Zmodyfikuj klasę Term:
#   dodaj "prywatne" pole day typu Day
#   zmodyfikuj konstruktor tak, aby uwzględniał możliwość przypisania powyższemu polu określonej wartości, tj. dnia tygodnia
#   zmodyfikuj metody — mają uwzględniać dni tygodnia

from day import Day

class Term():
    def __init__(self, day, hour, minute, duration = 90):
        self.__day = day
        self.hour = hour
        self.minute = minute 
        self.duration = duration

    def __str__(self):
        match self.__day:
            case Day.MON:
                dzien = "Poniedziałek"
            case Day.TUE:
                dzien = "Wtorek"
            case Day.WED:
                dzien = "Środa"
            case Day.THU:
                dzien = "Czwartek"
            case Day.FRI:
                dzien = "Piątek"
            case Day.SAT:
                dzien = "Sobota"
            case Day.SUN:
                dzien = "Niedziela"

        return "{} {}:{:02d} [{}]".format(dzien, self.hour, self.minute, self.duration)

    def earlierThan(self, termin):
        if self.__day.difference((termin.__day)) > 0:
            return True
        elif self.__day.difference((termin.__day)) == 0:
            if self.hour < termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute < termin.minute:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def laterThan(self, termin):
        if self.__day.difference((termin.__day)) < 0:
            return True
        elif self.__day.difference((termin.__day)) == 0:
            if self.hour > termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute > termin.minute:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def equals(self, termin):
        if self.__day == termin.__day and self.hour == termin.hour and self.minute == termin.minute and self.duration == termin.duration:
            return True
        else:
            return False


# if __name__ == '__main__':   
#     term1 = Term(Day.TUE, 9, 45)
#     print(term1)                     # Ma się wypisać: "Wtorek 9:45 [90]"
#     term2 = Term(Day.WED, 10, 15)
#     print(term2)                     # Ma się wypisać: "Środa 10:15 [90]"
#     print(term1.earlierThan(term2)); # Ma się wypisać: "True"
#     print(term1.laterThan(term2));   # Ma się wypisać: "False"
#     print(term1.equals(term2));      # Ma się wypisać: "False"
