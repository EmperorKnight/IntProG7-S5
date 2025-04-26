# Presenta un menú con las opciones: sumar, restar, multiplicar o dividir dos números. 
# Elige la opción con un número y realiza la operación.

print("Sumar = 1 | Restar = 2 | Multiplicar = 3 | Dividir = 4")
operaciones = int(input(f"Introduzca la operacion que desea realizar \n-> "))

if operaciones == 1:
    numero1 = int(input(f"Introduzca un numero \n-> "))
    numero2 = int(input(f"Introduzca otro numero \n-> "))
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado:,}")
elif operaciones == 2: 
    numero1 = int(input(f"Introduzca un numero \n-> "))
    numero2 = int(input(f"Introduzca otro numero \n-> "))
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado:,}")
elif operaciones == 3:
    numero1 = int(input(f"Introduzca un numero \n-> "))
    numero2 = int(input(f"Introduzca otro numero \n-> "))
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado:,}")
elif operaciones == 4:
    numero1 = int(input(f"Introduzca un numero \n-> "))
    numero2 = int(input(f"Introduzca otro numero \n-> "))
    if numero1 > numero2:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado:,}")
    else: 
        resultado = numero2 / numero1
        print(f"El resultado de la divisi es: {resultado:,}")
elif operaciones not in [1,2,3,4]:
    print("Lo sentimos, no somos capaces de realizar la operacion que desea")