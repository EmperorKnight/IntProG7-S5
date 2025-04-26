# Solicita un número y determina si es par, impar o si es cero.

numero = float(input(f"Introduzca un numero \n-> "))

if numero != 0:
    num_par = numero % 2
    if num_par == 0:
        print("El numero que introdujo es par")
    else:
        print("El numero es impar")
else:
    print("El numero es 0")