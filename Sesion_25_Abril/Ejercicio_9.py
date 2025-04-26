# Pide la edad del usuario y muestra si puede entrar a una película: infantil (0–12), 
# adolescente (13–17), adulto (18+).

edad = int(input(f"Introduzca su edad para verificar que pelicula puede ver \n-> "))

if 0 <= edad <= 12:
    print("Usted puede ver peliculas infantiles")
elif 13 <= edad <= 17:
    print("Usted puede ver pelicula para adolescentes")
elif edad >= 18:
    print("Usted puede ver pelicula para adultos")
else: 
    print("No hay forma que tenga esa edad")