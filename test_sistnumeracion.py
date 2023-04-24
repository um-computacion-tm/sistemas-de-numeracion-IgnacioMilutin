import unittest
from bin2dec_dec2bin from decimal2binario
from bin2dec_dec2bin from binario2decimal

class TestNumeracion(unittest.TestCase):
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal('01011100'),92)
    def test_decimal2binario(self):
        self.assertEqual(decimal2binario(97), '01100001')
    def test_decimal2binario(self):
        self.assertEqual(binario2decimal(120),'01111000')

if __name__=='__main__':
    unittest.main()