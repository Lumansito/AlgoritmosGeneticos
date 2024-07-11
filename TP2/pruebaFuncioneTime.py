import time

arreglo = [[[0]for _ in range(1000)]for _ in range(1000)]



def funcion_a_cronometrar():
    for i in range(1000):
        for j in range(1000):
            arreglo[i][j][0] = 1
    print("")  # Ejemplo de una función que toma 2 segundos en ejecutarse

# Guarda el tiempo de inicio
inicio = time.time()

# Llama a la función que quieres medir
funcion_a_cronometrar()

# Calcula el tiempo transcurrido
tiempo_transcurrido = time.time() - inicio

print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")
