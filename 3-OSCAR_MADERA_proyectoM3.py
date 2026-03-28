# Las características de tu programa:
# 1. Será la simulación de una máquina de Galton de 3000 canicas.
# 2. En total tendrá 12 niveles de obstáculos -deberás decidir si va a caer a
# un lado o al otro 12 veces.
# 3. El resultado final será un histograma que represente la cantidad de
# canicas en cada contenedor, como el siguiente -No olvides colocar
# nombre a los ejes y un título al gráfico.
# 4. Deberás emplear dos funciones, una para calcular los resultados de las
# canicas y la segunda para la graficación del histograma.

# Empezamos importando random (para numeros al azar) y matplotlib.pyplot(para la creacion de graficos).
import random
import matplotlib.pyplot as plt

# creamos la funcion para calcular los resultados de las canicas.


def simular_galton(canicas, niveles):
    """
    Calcula los resultados de las canicas.
    Cada canica decide las veces si cae a la izquierda = 0 o derecha= 1.
    """
    contenedores = [0] * (niveles + 1)
# _ como variable por que no nos importa saber si es la primera canica o la  ultima
    for _ in range(canicas):
        posicion = 0
        for _ in range(niveles):
            # Decisión aleatoria: 0 para izquierda, 1 para derecha
            paso = random.randint(0, 1)
            posicion += paso
        # Se suma la canica al contenedor final correspondiente
        contenedores[posicion] += 1

    return contenedores

# creamos la segunda funcion para hacer el grafico.


def graficar_histograma(contenedores):
    """
    Genera el gráfico de barras que representa la distribución de las canicas.
    """
    # Definicion de los niveles (eje X)
    x = list(range(len(contenedores)))

    plt.bar(x, contenedores, color='green', edgecolor='black')

    # Etiquetas y título
    plt.title('Simulación de Máquina de Galton.')
    plt.xlabel('Distribución de canicas')
    plt.ylabel('Cantidad de Canicas')

# mostramos grafico
    plt.show()


#  Ejecución del programa
CANTIDADCANICAS = 3000
# niveles de obstaculos
NIVELES = 12
# Calculamos resultado
resultados = simular_galton(CANTIDADCANICAS, NIVELES)  # niveles de obstaculos
# Graficamos
graficar_histograma(resultados)
