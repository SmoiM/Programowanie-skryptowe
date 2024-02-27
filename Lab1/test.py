# 1. Utwórz skrypt 'test.py', z testami, o następującej zawartości:
import main
import unittest
from fractions import Fraction
import cmath

class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(ValueError):
            self.assertEqual(main.sum(2, 'Ala ma kota123'), 2)
            
    def test_fraction(self):
        self.assertEqual(main.sum(Fraction(2, 4), Fraction(3, 8)), Fraction(7, 8))
        
    def test_complex(self):
        self.assertEqual(main.sum(complex(3, 4), complex(5, 7)), complex(8, 11))
    
    def test_not_number_nor_striing(self):
        with self.assertRaises(ValueError):
            self.assertEqual(main.sum(1, [2, 3]), 1)

if __name__ == '__main__':
    unittest.main()

# 2. Uruchom skrypt 'test.py' (python3 test.py) i zobacz jakie wyniki zwraca

#    suma = 9
#    __name__ = main
#    Pośrednio
#    ..
#    ----------------------------------------------------------------------
#    Ran 2 tests in 0.000s

#   OK

# 3. Odkomentuj dodatkowe dodatkowe testy zawarte w liniach 12-19 pliku 'test.rb'

# 4. Zmodyfikuj definicję (treść) funkcji sum(arg1, arg2) tak, aby dodatkowe testy kończyły się powodzeniem — funkcja ma również sumować liczby będące napisami

# 5. Zmodyfikuj testy (a w razie potrzeby również i skrypt) — oprócz sprawdzania poprawności sumowania liczb całkowitych oraz rzeczywistych, powinny także sprawdzać poprawność sumowania liczb wymiernych oraz zespolonych

# 6. Zbadaj czy skrypt lub testy wykrywają, że argumentem funkcji jest napis, którego nie da się skonwertować na liczbę: sum(2, 'Ala ma kota123')
#       Tak

# 7. Zmodyfikuj testy — test ma dodatkowo, za pomocą assertRaises(), sprawdzać czy w przypadku podania napisu, którego nie da się skonwertować na liczbę, generowany jest wyjątek

# 8. Sprawdź czy testy wykrywają fakt wywołania funkcji z argumentami niebędącym ani liczbą, ani napisem, np. sum(1, [2, 3])