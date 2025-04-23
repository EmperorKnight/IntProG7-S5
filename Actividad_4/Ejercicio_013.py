# Menú de operaciones bancarias
# • Ingresar un saldo inicial
# • Mostrar opciones: 1=Vaciar cuenta, 2=Depositar, 3=Retirar.
# • Realizar la acción correspondiente según la opción ingresada.
# • Mostrar nuevo saldo

saldo_inicial = float(input(f"Introduzca el saldo inicial \n-> "))
operacion = int(input(f"Operaciones que disponemos:\n1 = Vaciar cuenta | 2 = Depositar | 3 = Retirar"))

if operacion == 1:
    print("Cuenta vaciada con exito")
elif operacion == 2:
    operacion2 = input("Introduzca la cantidad a depositar")
    print("Deposito exitoso")
elif operacion == 3:
    operacion2 = input("Introduzca la cantidad a retirar")
    print("Retiro exitoso")
else:
    print("Lo sentimos no disponemos de la operacion bancaria que desea realizar")