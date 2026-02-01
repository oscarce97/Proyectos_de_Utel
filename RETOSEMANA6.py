# Existen muchísimos casos en los que este tipo de estructuras forman
# parte del día a día, pero no siempre nos damos cuenta de ello y, al no
# conocerlos, no nos percatamos de que están ahí. Así que, para poner en
# práctica lo aprendido, te reto a que escribas un código con las siguientes
# características:
# ●Que solicite una contraseña que inicie con un número,
# ●Que pida ingresar nuevamente la contraseña y verificar que coincida
# con la primera ingresada.
# ●Si se cometen tres errores al ingresar la contraseña, que despliegue
# un mensaje de aviso y cierre el programa.


intentos = 0
contraseña_correcta = "1jkl"

while intentos < 3:
    contraseña = input("Ingresa la contraseña: ")

    if not contraseña[0].isdigit():
        print("La contraseña debe iniciar con un número.")
        intentos += 1
        continue

    if contraseña == contraseña_correcta:
        while intentos < 3:
            confirmacion = input("Ingrese la contraseña nuevamente: ")
            if confirmacion == contraseña_correcta:
                print("Contraseña correcta."
                      "\nFin del programa")
                exit()
            else:
                print("Las contraseñas no coinciden.")
                intentos += 1
    else:
        print("Contraseña incorrecta.")
        intentos += 1

print("Has cometido 3 errores. El programa se cerrará.")
