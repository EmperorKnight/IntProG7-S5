# Validar edad mínima para votar
# • Ingresar la edad de una persona.
# • Si la edad es mayor o igual a 18, mostrar "Puede votar".

edad = int(input(f" \nIntroduzca su edad actual \n-> "))

if edad >= 18:
    print("Puede votar")
else:
    print("No tiene edad para votar")