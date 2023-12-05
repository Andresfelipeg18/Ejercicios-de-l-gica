"""
cree un programa que lea el monto de un prestamo y el plazo en meses, y muestre al usuario el valor las cuotas 
mensuales pagando un interes fijo del 2.7% menssual.
"""
# Definir variables y valores
prestamo = float(input("Ingrese el prestamo a financiar: "))
plazo= int (input("Ingrese los meses del plazo: "))
intereses= (0.027) 
total = prestamo*intereses
cuotas = plazo * total
cuotas1 = prestamo + cuotas
total2 = cuotas1 / plazo 
print ("El valor del prestamo es:  " + str (prestamo))
print ("El valor del interes por mes  es:  " + str (total))
print ("El valor total de interes:   " + str (cuotas))
print ("El valor total a pagar es:  " + str (cuotas1))
print ("El valor de cuota mensual es: " + str (total2))
