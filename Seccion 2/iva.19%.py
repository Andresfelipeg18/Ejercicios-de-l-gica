"""
Cree un programa que tome el precio e imprima su precio final al consumidor con IVA de 19%
"""

iva = 0.19
nombre_prod = input ("Ingrese el nombre del producto: ")
precio_sin_iva= float(input("Ingrese el precio producto: "))

ipc= precio_sin_iva*iva
Total_devengado= precio_sin_iva+ipc

print ("El valor  iva es: " + str (ipc))
print ("El valor a pagar producto es : " + str (precio_sin_iva))
print ("El valor a pagar con iva es: " + str (Total_devengado))

