from tabnanny import check
from card_validator import check_luhn
import unittest

class testCardValidator(unittest.TestCase):

    def testCases(self):
        self.assertTrue(check_luhn("79927398713"))
        self.assertFalse(check_luhn("79927398715"))
    
        with self.assertRaises(TypeError):
            check_luhn(79927398713)

if __name__ == '__main__':
    unittest.main()