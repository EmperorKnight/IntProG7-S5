# Categorización de edad
# • Ingresar edad.
# • Categorizar como: Niño (0–11), Adolescente (12–17), Adulto (18–64), Adulto mayor
# (65+)

edad = int(input(f"Introduzca su edad \n-> "))

if 0 <= edad <= 11:
    print("Usted es un niño")
elif 12 <= edad <= 17:
    print("Usted es un adolescente")
elif 18 <= edad <= 64:
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor")