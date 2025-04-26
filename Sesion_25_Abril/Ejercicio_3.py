# Pide al usuario tres números y determina cuál es el mayor, el menor o si todos son iguales.

primer_numero =int(input(f"Introduzca un numero \n-> "))
segundo_numero = int(input(f"Introduzca un segundo numero \n-> "))
tercer_numero = int(input(f"Introduzca un tercer numero \n-> "))

if primer_numero == segundo_numero and segundo_numero == tercer_numero:
    print("Son iguales")
elif primer_numero > segundo_numero and primer_numero > tercer_numero:
    print("El mayor es ", primer_numero)
    if segundo_numero < tercer_numero:
        print("El numero menor es ", segundo_numero)
    else: 
        print("El numero menor es ", tercer_numero)
elif tercer_numero > primer_numero and tercer_numero > segundo_numero: 
    print("El mayor es ", tercer_numero)
    if primer_numero < segundo_numero:
        print("El menor es ",primer_numero)
    else: 
        print("El menor es ",segundo_numero)
elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
    print("El mayor es ",segundo_numero)
    if primer_numero < tercer_numero:
        print("El menor es ", primer_numero)
    else:
        print("El menor es ", tercer_numero)
else:
    print("ERROR")
