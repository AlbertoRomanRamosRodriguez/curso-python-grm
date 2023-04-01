import random
import time

trayectoria = []
temperaturas = []

obtener_temperatura = lambda: round(random.uniform(25, 45), 2)

def obtener_coordenadas():
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    return (x, y)


while True:
    x, y = obtener_coordenadas()  # Función para obtener las coordenadas actuales
    temperatura = obtener_temperatura() # Función para obtener la temperatura actual
    trayectoria.append((x, y))   # Agregar las coordenadas actuales a la lista "trayectoria"
    temperaturas.append(temperatura) # Agregar la temperatura actual a la lista "temperaturas"
    if 0 <= x <= 34 and 0 <= y <= 45:
        print("El robot está dentro de la caja en la posición:", (x, y), "\ny la temperatura es:", temperatura)
        if temperatura > 40:
            print("¡ALERTA! Temperatura demasiado alta.")
    else:
        print("El robot está fuera de la caja en la posición:", (x, y), "\nLa temperatura es:", temperatura)
    if len(temperaturas) > 10:
        print("Últimas 10 temperaturas medidas:", temperaturas[-10:])
    time.sleep(1)


################################ TAREA 1 ####################################

### NO DECOMENTAREAR LAS LÍNEAS DE LA ORDEN. Responder en la sección siguiente o en el Jupyter Notebook `clase1.ipynb`

## Tarea

# Hacer un agrupamiento de los datos de la manera

# 1. Lista de diccionarios

    #
    # [
    #   {
    #     'x': <posicion en x>
    #     'y': <posicion en y>
    #     'temp': <temperatura>
    #   }
    # ]

    # Por ejemplo:

    # [
    #   {
    #     'x': 5
    #     'y': 17
    #     'temp': 34
    #   },{
    #     'x': 6
    #     'y': 18
    #     'temp': 35
    #   },{
    #     'x': 9
    #     'y': 19
    #     'temp': 36
    #   }
    # ]


# 2. Lista de tuplas

    #
    # [
    #   (<posx>, <posy>, <temp>)
    # ]
    # Por ejemplo:
    #
    # [
    #   (5, 17, 34),
    #   (6, 18, 35),
    #   (9, 19, 36)
    # ]


## Plus
# Con las variables **temperatura** y **trayectorias** elaborar un gráfico en 3D 
# que sirva para mostrar las temperaturas en cada punto de la trayectoria.


############################## RESPUESTA A LA TAREA AQUÍ #######################################