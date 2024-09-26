import os
import time
import pandas as pd


df = pd.read_excel(io=r'TP3\TablaCapitales.xlsx', sheet_name="Sheet1")
array = df.to_numpy()

print(array)

capitales=array[0]


def distanciaParaRecorrido(arregloDeRecorridos):
    distancia = 0
    for i in range(len(arregloDeRecorridos)-1):
        distancia += array[arregloDeRecorridos[i]][arregloDeRecorridos[i+1]+1]
    return distancia



'''
os.system('cls')
op = ""
print("_"*90+"\n")
op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()
while op != "A" and op != "B" and op != "C" and op != "S":
    #os.system('cls')
    print("_"*90+"\n")
    print("\033[91mOpción no valida\033[0m")
    op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()

while op !="S":
    
    #if op == "A":
    #   for i in range(23): 
    #       print(i, capitales[i])
    #   cap=input("Ingrese la capital deseada: ") #VALIDAR
    #   distancia, arreglo =funcionA(cap) #QUE ESTA EN apartadoA.py

    #if op == "B":
    #   min=999999
    #   for i in range(23): 
    #       distancia, arreglo =funcionA(i) #QUE ESTA EN apartadoA.py, debería retornar el arreglo del orden como minimo 
    #       if distancia<min:
    #           indiceMin=i
    #           min=distancia
    #   print("El recorrido es menor arrancando en ",capitales[indiceMin],". La distancia es: ",distancia )

    #if op == "C":
    #   AG



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


'''


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