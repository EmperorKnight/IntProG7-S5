#  Detectar si un usuario está inactivo por más de 30 días
# • Ingresar fecha de último inicio de sesión.
# • Calcular los días transcurridos.
# • Si son más de 30, mostrar “Cuenta inactiva”.

from datetime import datetime

hoy = datetime.now()

ultima_sesion = input(f" \nIntroduzca la fecha de su ultima sesión en formato dd/mm/aaaa \n-> ")
ultima_sesion = datetime.strptime(ultima_sesion,"%d/%m/%Y")

contar_dias = (hoy - ultima_sesion).days

if contar_dias > 30:
    print(f"Cuenta inactiva\n ")
else:
    print(f"Cuenta activa\n ")