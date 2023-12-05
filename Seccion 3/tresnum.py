""" 
ree un programa que reciba tres números y muestre el mayor. En caso de que los números sean iguales
también se debe mostrar al usuario.
"""
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))

if n1>n2 and n1>n3:
    print("El mayor es",n1)
elif n2>n1 and n2>n3:
    print("El mayor es",n2)
elif n3>n1 and n3>n2:
    print("El mayor es",n3)
else:
    print("Los numeros son iguales")
