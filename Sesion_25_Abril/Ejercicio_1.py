# Escribe un programa que solicite al usuario su edad y determine si es un niño, 
# adolescente, adulto o adulto mayor.

edad = int(input(f"Introduzca su edad \n-> "))

if edad < 0:
    print("¿Edad negativa?, ¿De verdad?")

if 0 < edad < 12:
    print("Usted es un niño")
elif 12 <= edad <= 18:
    print("Usted es un adolescente")
elif 18 < edad <= 65:
    print("Usted es un adulto")
elif 65 < edad <= 130:
    print("Usted es un adulto mayor")