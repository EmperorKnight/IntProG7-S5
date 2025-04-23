# Encontrar el mayor de tres números
# • Ingresar el primer número
# • Ingresar el segundo número
# • Ingresar el tercer número
# • Si el primero es mayor o igual que el segundo, comparar el primero con el tercero
# • Si el primero es menor que el segundo, compara el segundo con el tercero
# • Si los tres son iguales, mostrar “Los números son iguales”

primer_numero = int(input(f"Introduzca el primer numero \n-> "))
segundo_numero = int(input(f"Introduzca el segundo numero \n-> "))
tercer_numero = int(input(f"Introduzca el tercer numero \n-> "))

if primer_numero > segundo_numero:
    uno = primer_numero > tercer_numero
    if uno == True:
        print("El primer numero es el mayor entre los tres")
    else:
        print("El tercer numero es el mayor entre los tres")
elif primer_numero < segundo_numero:
    uno = segundo_numero > tercer_numero
    if uno == True:
        print("El segundo numero es el mayor entre los tres")
    else:
        print("El tercer numero es el mayor entre los tres")
elif primer_numero == segundo_numero == tercer_numero:
    print("Los tres numero son iguales")
