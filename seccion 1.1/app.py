"""
Aplicacion que provee un interfaz al usuario 
para ejecutar operaciones basicas entre dos numeros
Autor: German Angarita
Fecha: octubre 6 de 2023
"""

#pedimos la opcion para saber que operacion quiere hacer el usuario
opcion = input("Para sumar ingrese 1 para restar in¿grese 2 para multiplicar ingrese 3 y para dividir ingrese 4: ")
#pedimos los numeros 
numero1 = int(input("ingrese numero 1: "))
numero2 = int(input("ingrese numero 2: "))
#si la opcion es 1... sumamos 
if opcion=="1": 
    operacion = numero1 + numero2 
#si la opcion es 2... restamos 
if opcion=="2": 
    operacion = numero1 - numero2
#si la opcion es 3... multiplicamos 
if opcion=="3": 
    operacion = numero1 * numero2
#si la opcion es 4... Dividimos
if opcion=="4": 
    operacion = numero1 / numero2 
print("Resultado es :"  + str (operacion))
