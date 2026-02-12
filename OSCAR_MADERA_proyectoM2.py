# Crear un programa para identificar la longitud de una palabra ingresada. La
# palabra correcta debe tener entre cuatro y ocho letras. toma en cuenta las
# siguientes consideraciones:
# ● Si la longitud de la palabra se encuentra en el rango de cuatro a ocho
# letras, se debe imprimir un mensaje que indique que la palabra es
# correcta.
# ● Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga:
# “Hacen falta letras. Solo tiene N letras” (siendo N el número de letras de
# la palabra).
# ● Si la palabra tiene más de 8 letras debe indicar un mensaje que diga:
# “Sobran letras. Tiene N letras” (siendo N el número de letras de la
# palabra).


# usamos el while para entrar en un ciclo con la preguta que es lo que queremos hacer mientras sea verdadero
# lo seguira preguntando.
while True:
    # la variable opc lo utlilizamos para ingresar una opc
    opc = int(input('\n¿Que es lo que quieres hacer ?'
                    '\n1. La longitud de la palabra.'
                    '\n2. Coordenadas.'
                    '\n3. Salir.'
                    '\nRespuesta: '))
# si la opcion es la 1 , entrara aqui, como esta dentro del while, cada que ingresemos la palabra
# nos dara una respuesta y nos volvera a preguntar que queremos hacer.
    if opc == 1:
        palabra = input("\nIngrese una palabra de entre 4 y 8 letras: ")
        contador = 0

        for letra in palabra:
            contador += 1

        if contador > 8:
            print("\nLa palabra tiene letras de mas.")
            print("La palabra tiene", contador, "letras")

        elif contador < 4:
            print("\nHacen falta letras")
            print("La palabra tiene", contador, "letras")

        else:
            print("\nLa palabra es correcta")
            print("La palabra tiene", contador, "letras")


# Crear un programa que en base a 2 números de entrada, coordenadas,
# identifique en cuál de los 4 cuadrantes se encuentra el punto. El programa
# debe verificar que ninguna coordenada sea 0. Por ejemplo
# Ingrese X: 4
# Ingrese Y: -5
# El punto se encuentra en el cuadrante IV
# (X,Y): (+,+) => Cuad. I; (-,+) => Cuad. II; (-,-) => Cuad. III; (+,-) => Cuad. IV


# si la opcion es la 2, entrara aqui para el programa de las coordenadas, ingresaremos 2 numeros
# y nos dara la respuesta del cuadrante en el que estamos, despues de dar la respuesta
# preguntara nuevamente ¿Que es lo que queremos hacer?.
    elif opc == 2:
        coordenada1 = int(input('\nIngrese la primera coordenadas (X)'))
        coordenada2 = int(input('Ingrese la segunda coordenada (Y)'))

        if coordenada1 == 0 or coordenada2 == 0:
            print('\n0 no esta permitido')
        elif coordenada1 > 0 and coordenada2 > 0:
            print('\nEstas en el cuadrante I')

        elif coordenada1 < 0 and coordenada2 > 0:
            print('\nEsta en el segundo cuadrante II')

        elif coordenada1 < 0 and coordenada2 < 0:
            print('\nEstas en el cuadrante III')

        elif coordenada1 > 0 and coordenada2 < 0:
            print('\nEstas en el cuadrante IV')

        else:
            print("\nNo agregaste un numero")

# esta opcion la agregamos para en caso de no querer continuar con el programa poder cerrarlo.
    elif opc == 3:
        print("\nGracias por usar el programa")
        exit()

# este else lo utilizamos para dejar un mensaje de error en caso de no ingresar una opcion valida,
# al estar dentro del ciclo while , no cierra el programa y podemos volver a la seleccion.
    else:
        print('\nNo existe esa opcion., Intente con otra')
