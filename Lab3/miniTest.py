import unittest
from DeanerySystem.term import Term, Day

class Test_TestDay(unittest.TestCase):
    def test_print(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        self.assertEqual(str(term1), "Wtorek 9:45 [90]")
        self.assertEqual(str(term2), "Środa 10:15 [90]")

    def test_earlierThan(self):
        self.assertFalse(Term(Day.TUE, 12, 15).earlierThan(Term(Day.MON, 9, 10)))
        self.assertFalse(Term(Day.MON, 14, 15).earlierThan(Term(Day.MON, 7, 28)))
        self.assertTrue(Term(Day.MON, 6, 1).earlierThan(Term(Day.MON, 14, 20)))

    def test_laterThan(self):
        self.assertTrue(Term(Day.TUE, 10, 15).laterThan(Term(Day.MON, 10, 00)))
        self.assertTrue(Term(Day.MON, 11, 15).laterThan(Term(Day.MON, 10, 18)))
        self.assertFalse(Term(Day.MON, 11, 15).laterThan(Term(Day.MON, 11, 18)))
    
    def test_term_equals(self):
        self.assertTrue(Term(Day.TUE, 5, 15).equals(Term(Day.TUE, 5, 15)))
        self.assertFalse(Term(Day.MON, 10, 15).equals(Term(Day.MON, 10, 15)))
        self.assertFalse(Term(Day.FRI, 12, 25).equals(Term(Day.FRI, 12, 25)))

if __name__ == '__main__':
    unittest.main()