# Cálculo de promedio de calificaciones

primera_calificacion = int(input(f"Introduzca la primera calificación \n-> "))
segunda_calificacion = int(input(f"Introduzca la segunda calificación \n-> "))
tercera_calificacion = int(input(f"Introduzca la tercera calificación \n-> "))

promedio = (primera_calificacion + segunda_calificacion + tercera_calificacion) // 3

print(f"Las calificaciones son \n1){primera_calificacion} \n2){segunda_calificacion} \n3){tercera_calificacion} \nEl promedio es de {promedio}%")