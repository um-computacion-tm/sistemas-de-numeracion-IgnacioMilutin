import unittest

def decimal2binario(decimal):
    bin=''
    while decimal//2 != 1:
        bin=bin + str(decimal%2)
        decimal=decimal//2 

    bin + '1'
    if len(bin)%4==3:
        bin=bin + '000'
    elif len(bin)%4==2:
        bin=bin+'00'
    elif len(bin)%4==1:
        bin=bin+'0'
    
    return bin[::-1]

def binario2decimal(binario):
    dicbin=[]
    pass


class TestNumeracion(unittest.TestCase):
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal('01011100'),92)
    def test_decimal2binario(self):
        self.assertEqual(decimal2binario(97), '01100001')

if __name__=='__main__':
    unittest.main()
    