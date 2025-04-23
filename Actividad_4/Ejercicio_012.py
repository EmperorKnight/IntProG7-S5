# Detección de condiciones extremas en servidor
# • Ingresar temperatura y uso de CPU.
# • Si la temperatura > 80 °C o el CPU > 95%, iniciar protocolo de emergencia.

temperatura = float(input(f"Introduzca la temperatura de su dispositivo \n-> °C"))
CPU = input(f"Introduzca el uso del CPU \n-> ")
CPU = int()

if temperatura > 80 or CPU > 95:
    print("Protocolo de emergencia inciado")
else:
    print("Todo correcto")