"""
Cree un programa que calcule la suma de los cuadrados de los números entre 1 y n
SECCIÓN

"""



def suma_cuadrados(n):
    suma = 0

    for i in range(1, n + 1):
        suma += i**2

    return suma

if __name__ == "__main__":
    try:
        n = int(input("Introduce un número entero n: "))
    except ValueError:
        print("Por favor, introduce un número entero válido.")
    else:
        resultado = suma_cuadrados(n)
        print(f"La suma de los cuadrados de los números entre 1 y {n} es: {resultado}")
