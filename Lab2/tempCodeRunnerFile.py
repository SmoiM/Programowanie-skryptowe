import skrypt
import unittest

class Test_TestSum(unittest.TestCase):
    def word(self):
        lancuch = "pies"
        self.assertEqual(skrypt.szukaj(lancuch), "Wyraz: pies" )
    def number(self):
        lancuch = "54"
        self.assertEqual(skrypt.szukaj(lancuch), "Liczba: 54" )
    def wordPlusNumber(self):
        lancuch = "Ala123"
        self.assertEqual(skrypt.szukaj(lancuch), """Wyraz: Ala
        Liczba: 123""" )
    def numberPlusWord(self):
        lancuch = "4koty"
        self.assertEqual(skrypt.szukaj(lancuch), "Liczba: 4\nWyraz: koty" )
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
