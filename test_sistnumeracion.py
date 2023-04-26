import unittest
from bin2dec_dec2bin import decimal2binario
from bin2dec_dec2bin import binario2decimal

class TestNumeracion(unittest.TestCase):
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal('01011100'),92)
    def test_binario2decimal2(self):
        self.assertEqual(binario2decimal('10000000'),128)
    def test_binario2decimal3(self):
        self.assertEqual(binario2decimal('0111'),7)
    def test_decimal2binario(self):
        self.assertEqual(decimal2binario(97), '01100001')
    def test_decimal2binario2(self):
        self.assertEqual(decimal2binario(120),'01111000')
    def test_decimal2binario3(self):
        self.assertEqual(decimal2binario(4),'0100')

if __name__=='__main__':
    unittest.main()
    