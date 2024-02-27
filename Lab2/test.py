import skrypt
import unittest

class Test_Szukaj(unittest.TestCase):
    def test_word(self):
        lancuch = "pies"
        wynik = "Wyraz: pies\n" 
        self.assertEqual(skrypt.szukaj(lancuch), wynik)

    def test_number(self):
        lancuch = "54"
        wynik = "Liczba: 54\n"
        self.assertEqual(skrypt.szukaj(lancuch), wynik)

    def test_wordPlusNumber(self):
        lancuch = "Ala123"
        wynik = "Wyraz: Ala\nLiczba: 123\n"
        self.assertEqual(skrypt.szukaj(lancuch), wynik)

    def test_numberPlusWord(self):
        lancuch = "4koty"
        wynik = "Liczba: 4\nWyraz: koty\n"
        self.assertEqual(skrypt.szukaj(lancuch), wynik)

    def test_otherCharactersPlusWord(self):
        lancuch = "@#Ala ma kota% 123&"
        wynik = """Wyraz: Ala\nWyraz: ma\nWyraz: kota\nLiczba: 123\n"""
        self.assertEqual(skrypt.szukaj(lancuch), wynik)

if __name__ == '__main__':
    unittest.main()
