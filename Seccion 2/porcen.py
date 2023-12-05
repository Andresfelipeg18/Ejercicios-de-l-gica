"""
Cree un programa qure lea una cantidad e imrpima un procentaje a calcular requerido sobre esa cantidad 
"""
canti= float(input("Ingrese la cantidad: "))
proce = float(input("Ingrese el procentaje: "))

resul= (proce/100) * canti

print ("El porcentaje es: " + str (resul))
