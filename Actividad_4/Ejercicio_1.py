# Verificar si un número está dentro de un rango válido
# • Ingresar un número.
# • Si el número está entre 100 y 999 inclusive, mostrar “Número válido”.

rango_inicial = int(input(f" \nIntroduzca el rango inicial \n-> "))
rango_final = int(input(f"Introduzca el rango final \n-> "))

if rango_inicial < rango_final:
    numero = int(input(f"Introduzca un numero \n-> "))
    if numero >= rango_inicial and numero<=rango_final:
        print(f"Dentro del rango establecido\n ")
    else:
        print(f"Numero fuera del rango\n ")
else: 
    print("No es posible este rango")