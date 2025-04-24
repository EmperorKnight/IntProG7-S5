# Verificación de validez de una fecha
# • Ingresar día, mes, y año.
# • Si el mes es febrero y el día > 29, mostrar error.
# • Si el mes es abril, junio, septiembre o noviembre y el día > 30, mostrar error
# • Si el mes es enero, marzo, mayo, julio, agosto, octubre, diciembre y el día > 31,
# mostrar error

fecha = input(f"Introduzca la fecha en formato dd/mm/aaaa \n-> ")

dia, mes, año = fecha.split("/")
dia1 = int(dia)
mes1 = int(mes)
año1 = int(año)

año2 = año1 % 4

if mes1 == 2 and dia1 > 29 and año2 == 0:
    print("Error, Febrero no tiene mas de 29 dias en un año bisiesto")
elif mes1 == 2 and dia1 > 28 and año2 !=0:
    print("Error, Febrerp no tiene mas de 28 dias en un año no bisiesto")
elif mes1 == 2 and 0 < dia1 <= 29 and año2 == 0:
    print("Todo correcto")
elif mes1 == 2 and 0 < dia1 <= 28 and año2 != 0:
    print("Todo correcto")


if mes1 in [4,6,9,11] and dia1 > 30:
    if mes1 == 4:
        print("Error, Abril no tiene mas de 30 dias")
    elif mes1 == 6:
        print("Error, Junio no tiene mas de 30 dias")
    elif mes1 == 9:
        print("Error, Septiembre no tiene mas de 30 dias")
    elif mes1 == 11:
        print("Error, Noviembre no tiene mas de 30 dias")
elif mes1 in [4,6,9,11] and 0 < dia1 <= 30:
    print("Todo correcto")

if mes1 in [1,3,5,7,8,10,12] and dia1 > 31:
    if mes1 == 1:
        print("Error, Enero no tiene mas de 31 dias")
    elif mes1 == 3:
        print("Error, Marzo no tiene mas de 31 dias")
    elif mes1 == 5:
        print("Error, Mayo no tiene mas de 31 dias")
    elif mes1 == 7:
        print("Error, Julio no tiene mas de 31 dias")
    elif mes1 == 8:
        print("Error, Agosto no tiene mas de 31 dias")
    elif mes1 == 10:
        print("Error, Octubre no tiene mas de 31 dias")
    elif mes1 == 12:
        print("Error, Diciembre no tiene mas de 31 dias")
elif mes1 in [1,3,5,7,8,10,12] and 0 < dia1 <= 31:
    print("Todo correcto")