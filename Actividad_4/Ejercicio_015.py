# Simulador de sistema de puntuación de conducta
# • Ingresar puntos (0 a 10).
# • Mostrar: “Excelente” si el número está entre 9 y 10, “Bueno” si el número está entre 7
# y 8, “Regular” si el número está entre 5 y 6, “Deficiente” si el número es < 5.
# • Si el valor es negativo o mayor a 10, mostrar error.

puntos = int(input(f"Introduzca los puntos de conducta de la persona \n-> "))

if puntos == 9 or puntos == 10:
    print("Excelente conducta")
elif puntos == 8 or puntos == 7:
    print("Conducta buena")
elif puntos == 6 or puntos == 5:
    print("Conducta regular")
elif 5 > puntos >= 0:
    print("Conducta deficiente")
elif puntos < 0 or puntos > 10:
    print("Error")
