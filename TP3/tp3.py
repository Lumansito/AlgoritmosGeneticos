import os
import time
import pandas as pd
df = pd.read_excel(io=r'D:\UTN\AlgoritmosGeneticos\TP3\TablaCapitales.xlsx', sheet_name="Sheet1")
df.to_numpy()
print(df)

#asignar columna 0 y fila 0 como etiquetas? o pasarlas a otro array?



#Realizar un programa que cuente con un menú con las siguientes opciones:
#a)Permitir ingresar una provincia y hallar la ruta de distancia mínima que logre unir todas las capitales de provincias 
# de la República Argentina partiendo de dicha capital utilizando la siguiente heurística: 
# “Desde cada ciudad ir a la ciudad más cercana no visitada.”  
# Recordar regresar siempre a la ciudad de partida. Presentar un mapa de la República con el recorrido indicado. 
# Además   indicar la ciudad de partida, el recorrido completo y la longitud del trayecto. 
# El programa deberá permitir seleccionar la capital que el usuario desee ingresar como inicio del recorrido.

#b)Encontrar el recorrido mínimo para visitar todas las capitales de las provincias de la República Argentina 
# siguiendo la heurística mencionada en el punto a. Deberá mostrar como salida el recorrido y la longitud del trayecto.

#c)Hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina, 
# utilizando un algoritmo genético.


os.system('cls')
op = ""
print("_"*90+"\n")
op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()
while op != "A" and op != "B" and op != "C" and op != "S":
    os.system('cls')
    print("_"*90+"\n")
    print("\033[91mOpción no valida\033[0m")
    op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()

while op !="S":
    



    #aca va el codigo de cada opcion
    #hacer funciones para cada uno de los casos
    #if op == "A":
    #   funcionA()
    
    time.sleep(1)






    os.system('cls')
    print("_"*90+"\n")
    print("¿Desea ejecutar otra opción?")
    op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()
    while op != "A" and op != "B" and op != "C" and op != "S":
        os.system('cls')
        print("_"*90+"\n")
        print("\033[91mOpción no valida\033[0m")
        op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()
print("\n\033[91m--- Fin del programa ---\033[0m")