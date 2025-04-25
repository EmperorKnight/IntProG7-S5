# Solicita una calificación numérica entre 0 y 100 y muestra si es "Reprobado", "Regular", "Bueno 80-89", 
# "Muy bueno90-95" o "Excelente96-100".

calificacion = int(input(f"Ingrese la calificación de un estudiante \n-> "))

if 0 <= calificacion < 70:
    print("Usted a reprobado")
elif 70 <= calificacion <= 79:
    print("Regular")
elif 80 <= calificacion <= 89:
    print("Buenas Notas")
elif 90 <= calificacion <= 95:
    print("Muy Buenas Notas")
elif 96 <= calificacion <= 100:
    print("Excelente Notas")
else:
    print("No es posible esta nota")