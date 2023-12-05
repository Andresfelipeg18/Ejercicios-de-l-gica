"""
ciclo for, lo usamos cuando sabemos el numero de repeticiones (interaciones) que se van a ejecutar
"""
#imprimir los numeros del 0 al 100
#aca la i es la variable del cilo




print("------0 a 100----")
for i in range (101) :
    print(i)
#imprimir los numeros del 123 al 670
#aca la i es la variable del cilo
print("------123 a 670----")
for p in range (123,671) :
    print(p)

#imprimir los numeros del 100 al 1 de forma descendente 
print("------100 a 1----")
for p in range (100,0, -1) :
    print(p)

#imprimir los numeros de 0 a n
print("------0 a n----")
n=int(input("ingrese limite superior "))
for p in range (0,n+1):
    print(p)

#recorrido de cademas 
print("------cadena - recorrido----")
nombre= "Colombia"
for letra in nombre:
    print (letra) 

#lectura de caracteres de una cadena 
print("------lectura de cadenas----")
aula = "Audivisuales 02"
print(aula[0])
print(aula[6])