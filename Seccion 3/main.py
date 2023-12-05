"""
programa que muestre el manejo operadores logicos 
"""
#los operadores logicos son : and,  or , not

producto = input ("Ingrese el producto")

if producto == "lentejas" or producto == "Arroz" or producto== "crema" or producto == "vino": 

    if producto == "lentejas" or producto == "Arroz" : 

        print ("No paga IVA")

    else: 
        print("PAGA IVA")
else: 
    print("Ingrese un  producto valido ")

print("------ estrato y edad " )
#un usuaruo tiene derecho a un subsidio si es amyor de edad y tiene un estrato mayor a 3
estrato = int (input ("Ingrese estrato"))
edad = int (input (" Ingrese edad "))
if estrato < 3 and edad >=18:
    print ("Derecho al subsidio")
else: 
    print ("No tiene derecho al subsidio")

print("------nor nome----")
empezada =  None# SE USA PARA INDICAR QUE UNA VARIABLE NO POSEE UN VALOR FUNCIONAL 
if empezada is not None:
    print ("La variable tiene un dato tipado")
else:
    print ("la variable no tiene valor asignado")
print ("------ not true-----")
soltero = True
print (not soltero)
habilitado= False
print(not habilitado)

