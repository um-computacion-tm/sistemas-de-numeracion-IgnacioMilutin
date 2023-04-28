import unittest
from bin2dec_dec2bin import decimal2binario
from bin2dec_dec2bin import binario2decimal
from dec2hex_hex2dec import decimal2hexadecimal
from dec2hex_hex2dec import hexadecimal2decimal
from dec2oct_oct2dec import decimal2octal
from dec2oct_oct2dec import octal2decimal

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
    def test_hexadecimal2decimal1(self):
        self.assertEqual(hexadecimal2decimal("A35D"),41821)
    def test_hexadecimal2decimal2(self):
        self.assertEqual(hexadecimal2decimal("C29"),3113)
    def test_hexadecimal2decimal3(self):
        self.assertEqual(hexadecimal2decimal("D2"),210)
    def test_decimal2hexadecimal1(self):
        self.assertEqual(decimal2hexadecimal(7921),"1EF1")
    def test_decimal2hexadecimal2(self):
        self.assertEqual(decimal2hexadecimal(737),"2E1")
    def test_decimal2hexadecimal3(self):
        self.assertEqual(decimal2hexadecimal(58),"3A")
    def test_decimal2octal1(self):
        self.assertEqual(decimal2octal(54),66)
    def test_decimal2octal2(self):
        self.assertEqual(decimal2octal(739),1343)
    def test_decimal2octal3(self):
        self.assertEqual(decimal2octal(6481),14521)
    def test_octal2decimal1(self):
        self.assertEqual(octal2decimal(63),51)
    def test_octal2decimal2(self):
        self.assertEqual(octal2decimal(427),279)
    def test_octal2decimal3(self):
        self.assertEqual(octal2decimal(5371),2809) 

if __name__=='__main__':
    unittest.main()
    