def decimal2octal(decimal):
    oct=''
    while decimal//8>1:
        oct+=str(decimal%8)
        decimal=decimal//8
    oct+=str(decimal%8)
    oct+=str(decimal//8)
    oct=oct[::-1]
    oct=int(oct)
    return oct

def octal2decimal(octal):
    octal=str(octal)
    dec=0
    exp=0
    for i in octal[::-1]:
        dec+=int(i)*(8**exp)
        exp=exp+1
    return dec