"""
Cree un programa que tome el valor de un producto e imprima su precio final si este tiene siempre un descuento del 10$
"""
desc= 0.10
nombre_prod = input ("Ingrese el nombre del producto: ")
precio= float(input("Ingrese el precio producto: "))

des1=precio*desc
total_devengando= precio-des1

print ("El valor  descuento es: " + str (des1))
print ("El valor a pagar producto es : " + str (precio))
print ("El valor a pagar con descuento es: " + str (total_devengando))