"""
Cree un programa que lea un número entre 1 y 15 y muestre si éste es primo o no
"""
pr2=2
pr3=3
pr5=5
pr7=7
pr=11
pr13=13
print("Elija un numero del 1 al 15")
n1 = int(input("Ingrese el numero: "))
if n1>15 or n1<1:
    print("¡ERROR! - elije un numero correcto")
elif n1==pr2 or n1==pr3 or n1==pr5 or n1==pr7 or n1==pr or n1==pr13:
    print(str(n1)+" Es Primo")
else:
    print(str(n1)+" No es primo")
