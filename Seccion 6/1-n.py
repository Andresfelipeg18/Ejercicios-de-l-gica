""" 
Cree un programa que muestre los números naturales de 1 a n.
"""
def numeros(n):
    for i in range(1, n+1):
        print(i)
num= int (input("Ingrese numero a consultar: "))
print("Los numeros naturales son : " )
resultado = numeros (num)