"""
Cree un programa que reciba dos números y muestre el mayor. En caso de que los números sean iguales
también se debe mostrar al usuario
"""
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))

if n1>n2:
    print("El mayor es",n1)
elif n2>n1:
    print("El mayor es",n2)
else:
    print("Los numeros son iguales")
