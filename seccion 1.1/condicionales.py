"""
Programa que muestra condionales en python 3 
Fecha:octubre 20 de 2023
"""
#pedimos nombre, si nombre es maria la saludamos
print ("--------------condiconal doble")
nombre = input("Ingrese nombre: ")
if nombre == "Maria" : 
    print ("Hola maria")
else : 
    print("Usted no es maria")
print ("--------------elif--------")
estrato = int (input ("Ingrese extracto"))
if estrato == 1 :
    print("ud tiene derecho a subsidio completo")
elif estrato == 2 :
    print ("ud tiene derecho a medio subsifio")
else : 
    print("ud no tiene derecho a subsidio")

