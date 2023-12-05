"""
cree un programa que lea dos numeros y muestre su producto, su cociente , su modulo, su suma y su resta 
"""
num1 = float (input ("Ingrese el primer numero: "))
num2 = float (input ("Ingrese el primer numero: "))
producto= num1 * num2
cociente= num1 / num2
# se puede sacar tambien con abs (n1-n2)
modulo= num1 % num2 
suma= num1 + num2
resta= num1 - num2
print ("Su pruducto es:" + str (producto))
print ("Su cociente es:" + str (cociente))
print ("Su modulo es:" + str (modulo))
print ("Su suma es:" + str (suma))
print ("Su resta es:" + str (resta))
