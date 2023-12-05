"""
Cree un programa que lea los tres ángulos internos de un triángulo y muestre si los ángulos corresponden a un
triángulo o no.
"""
angulo1=int(input("Ingrese angulo 1: "))
angulo2=int(input("Ingrese angulo 2: "))
angulo3=int(input("Ingrese angulo 3: "))
triangulo=angulo1+angulo2+angulo3
if triangulo==180:
    print("Corresponde a un triangulo")
else:
    print("No corresponde a un triangulo")

