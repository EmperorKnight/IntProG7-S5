# Evaluar si un estudiante aprueba o reprueba
# • Ingresar una calificación.
# • Si es mayor o igual a 70, mostrar "Aprobado"; de lo contrario, "Reprobado"

calificacion = int(input(f"Ingrese la calificación de un estudiante \n-> "))

if calificacion >= 70 and calificacion <= 100:
    print("El estudiante aprobo")
elif calificacion > 100:
        print("Lo sentimos no podemos denominar esta nota")
else:
    print("El estudiante reprobo")