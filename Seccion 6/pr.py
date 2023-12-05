"""
Cree un programa que muestre el promedio de n números, dejándose de solicitar números cuando se
introduzca el cero.
"""

def calcular_promedio():
    numeros = []
    
    while True:
        try:
            numero = float(input("Introduce un número (o 0 para terminar): "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if numero == 0:
            break
        else:
            numeros.append(numero)

    if len(numeros) == 0:
        print("No se introdujeron números. No se puede calcular el promedio.")
    else:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números ingresados es: {promedio}")

if __name__ == "__main__":
    calcular_promedio()
    