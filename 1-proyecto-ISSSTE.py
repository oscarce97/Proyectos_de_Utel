# Crear un programa que pida al usuario su nombre, apellido paterno, apellido materno, edad, peso y estatura,
# desplegarlos en pantalla junto con su Índice de Masa Corporal (IMC).
print('CALCULADORA DE IMC '
      '\n'
      '\nIntroduce tus datos correctamente para obtener el indice de masa corporal'
      '\n')
while True:
    Nombre = input("Cual es tu nombre? ")
    ApellidoP = input("Cual es tu Apellido Paterno? ")
    ApellidoM = input("Cual es tu Apellido Materno? ")
    if Nombre.isalpha() and ApellidoM.isalpha() and ApellidoP.isalpha():

        print("Nombre guardado...")
        break
    else:
        print('No agregaste un nombre o apellido.')

while True:
    Edad = input("Cual es tu edad?   ")
    Peso = input("Cual es tu peso?  ")
    Estatura = input("Cual es tu estatura?  ")

    if Edad.isalpha() or Peso.isalpha() or Estatura.isalpha() or Edad == "" or Peso == "" or Estatura == "":
        print("No ingresaste numeros")

    else:
        Estatura2 = float(Estatura)
        Peso2 = float(Peso)
        print("Entrada no válida (posiblemente mezcla de números y letras o símbolos).")
        print("\nDatos guardados.. "
              "\n"
              "\nAqui tus datos"
              "\n")

        print("Nombre: " + Nombre + " " + ApellidoP + " " + ApellidoM)
        print("Edad: %s" % (Edad))
        print("Peso: %s" % (Peso2))
        print("Estatura: %s" % (Estatura))
        imc = (Peso2/Estatura2**2)
        print("El IMC es: {}".format(imc))

        break
