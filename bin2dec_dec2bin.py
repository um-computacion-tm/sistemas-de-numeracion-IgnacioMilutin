import unittest
def decimal2binario(decimal):
    bin=''
    while decimal//2 > 1:
        bin=bin + str(decimal%2)
        decimal=int(decimal//2)
    bin=bin + str(decimal%2)
    decimal=int(decimal//2)
    bin = bin +'1'
    if len(bin)%4==3:
        bin=bin + str(0)
    elif len(bin)%4==2:
        bin=bin+str(00)
    elif len(bin)%4==1:
        bin=bin+str(000)
    else: bin
    return bin[::-1]

def binario2decimal(binario):
    lista=list(binario[::-1])
    for j in range(len(lista)):
        lista[j]=int(lista[j])
    exp=0
    dec=0
    for i in lista:
        num=i*(2**exp)
        dec+=num
        exp+=1
    return dec