# Ingresa un día de la semana y verifica si es un día laboral, fin de semana o un día inválido.

dia_laboral = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
fin_semana = ["Sabado","Domingo"]

dia_semana = input(f"Escriba el dia de la semana \n-> ")
dia_semana1 = dia_semana.capitalize()

if dia_semana1 in dia_laboral:
    print("Dia para ir al trabajo")
elif dia_semana1 in fin_semana:
    print("Dia para descansar")
else:
    print("Lo sentimos, no esta registrado este dia")