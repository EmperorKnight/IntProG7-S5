# Ingresa una temperatura en grados Celsius y clasifica el clima como 
# “frío”, “templado”, “cálido” o “muy caluroso”.

temperatura = float(input(f"Introduzca la temperatura en grados celsius \n-> °C "))

if temperatura < 10:
    print("Actualmente hace frio")
elif 10 <= temperatura < 20:
    print("Actualmente esta templado el clima")
elif 20 <= temperatura < 25:
    print("Actualmente el clima esta calido")
elif temperatura >= 25:
    print("Actualmente hace mucho calor")