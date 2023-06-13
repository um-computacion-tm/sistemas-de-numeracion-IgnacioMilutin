from bin2dec_dec2bin import binario2decimal 
from dec2oct_oct2dec import decimal2octal 
from bin2dec_dec2bin import decimal2binario
from dec2oct_oct2dec import octal2decimal

def binario2octal(binario):
    decimal=binario2decimal(binario)
    return decimal2octal(decimal)

def octal2binario(octal):
    decimal=octal2decimal(octal)
    return decimal2binario(decimal)