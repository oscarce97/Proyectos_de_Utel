# Aplicando lo aprendido,
# te reto a que realices, por tu cuenta, un programa con las siguientes
# características:
# 1. Que solicite al usuario el año actual y un año cualquiera.
# 2. Que despliegue en la pantalla cuántos años han pasado desde el año
# ingresado hasta el actual o cuántos años faltan para llegar a ese año. Ten
# en cuenta que si solo falta o ha pasado un año, debe mostrar un mensaje
# adecuado.
# 3. Que notifique si se ha ingresado dos veces el mismo año.

actual1 = int(input(" Ingresa el año actual: "))
calcular2 = int(input("Ingresa el año a cualcular: "))

if actual1 > calcular2:
    resp1 = actual1 - calcular2
    if resp1 > 1:
        print(" Han pasado {} años desde el {}.".format(resp1, calcular2))
    else:
        print("Ha pasado un año desde el {}.".format(calcular2))
        exit()

elif actual1 < calcular2:
    resp2 = calcular2 - actual1
    if resp2 > 1:
        print("Faltan {} años para el año  {}.".format(resp2, calcular2))

    else:
        print("Falta 1 año  para el año  {}.".format(calcular2))
        exit()

elif actual1 == calcular2:
    print("Has introducido el mismo año que el actual.")
