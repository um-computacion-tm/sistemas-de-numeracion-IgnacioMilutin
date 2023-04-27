import unittest 

hexdicc={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
hexdicc2={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def hexadecimal2decimal(hexadecimal):
    dec=0
    exp=0
    for i in hexadecimal[::-1]:
        dec+=hexdicc.get(i)*(16**exp)
        exp+=1
    return dec

def decimal2hexadecimal (decimal):
    lista=[]
    while decimal//16>0:
        num=0
        num=decimal%16
        decimal=decimal//16
        lista.append(num)
    lista.append(decimal)
    hex=""
    for i in lista[::-1]:
    
        hex+=hexdicc2[i]
    return hex

class TestNumeracion(unittest.TestCase):
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

if __name__=='__main__':
    unittest.main()

