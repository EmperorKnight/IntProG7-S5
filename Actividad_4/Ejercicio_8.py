# Verificación de inicio de sesión
# • Ingresar nombre de usuario y clave.
# • Si el usuario es “admin” y la clave “1234admin”, permitir acceso.
# • Si no, denegar.

usuario_guardado = ["admin"]
clave_guardada = ["1234admin"]

usuario_confirmacion = input(f"Introduzca su usuario \n-> ")
clave_confirmacion = input(f"Introduzca su clave \n-> ")

if usuario_confirmacion in usuario_guardado and clave_confirmacion in clave_guardada:
    print(f"Bienvenido {usuario_confirmacion}")
else:
    print(f"No tienes permiso para entrar a este espacio virtual")
