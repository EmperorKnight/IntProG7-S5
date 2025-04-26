# Pide una letra de calificación (A, B, C, D, F) y muestra el significado según el sistema estadounidense.

calificacion_estadounidense = input(f"Introduzca la nota segun el sistema estadounidense (A, B, C, D, F) \n-> ")

calificacion_estadounidense1 = calificacion_estadounidense.upper()

if calificacion_estadounidense1 == "A":
    print("Usualmente usado para indicar un trabajo sobresaliente (90-100%)")
elif calificacion_estadounidense1 == "B":
    print("Usualmente usado para indicar un buen trabajo (80-89%)")
elif calificacion_estadounidense1 == "C":
    print("Usualmente usado para indicar un trabajo aceptable (70-79%)")
elif calificacion_estadounidense1 == "D":
    print("Usualmente usado para indicar un trabajo deficiente osea que no pasa la clase (60-69%)")
elif calificacion_estadounidense1 == "F":
    print("Usualmente usado para indicar que reprobo (0-59%)")