# Verificar si un número es par y es positivo
# • Ingresar un número.
# • Si es mayor que 0, mostrar "El número es positivo".
# • Si es divisible por 2, mostrar “El número es par”

numero = int(input(f"Introduzca un numero random \n-> "))

num_par = numero % 2

if numero > 0 and num_par == 0:
    print("El numero que introdujo es positivo y es un numero par")
elif numero < 0 and num_par == 0:
    print("El numero que introdujo es negativo y es un numero par")
elif numero > 0 and num_par != 0:
    print("El numero que introdujo es positivo y es un numero inpar")
elif numero < 0 and num_par != 0:
    print("El numero que introdujo es negativo y es un numero inpar")
