import unittest
from solutions import sentence_reverse

class SentenceReverse(unittest.TestCase):
    def test_case_1(self):
        input = [" "," "]

        expected = [" "," "]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_2(self):

        input = ["a"," "," ","b"]

        expected = ["b"," "," ","a"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_3(self):
        input = ["h","e","l","l","o"]

        expected = ["h","e","l","l","o"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        input = ["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"]

        expected = ["p","r","a","c","t","i","c","e"," ","m","a","k","e","s"," ","p","e","r","f","e","c","t"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        input = ["y","o","u"," ","w","i","t","h"," ","b","e"," ","f","o","r","c","e"," ","t","h","e"," ","m","a","y"]

        expected = ["m","a","y"," ","t","h","e"," ","f","o","r","c","e"," ","b","e"," ","w","i","t","h"," ","y","o","u"]
        actual = sentence_reverse(input)
      
        self.assertEqual(expected, actual)

    def test_case_6(self):
        input = ["g","r","e","a","t","e","s","t"," ","n","a","m","e"," ","f","i","r","s","t"," ","e","v","e","r"," ","n","a","m","e"," ","l","a","s","t"]

        expected = ["l","a","s","t"," ","n","a","m","e"," ","e","v","e","r"," ","f","i","r","s","t"," ","n","a","m","e"," ","g","r","e","a","t","e","s","t"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()