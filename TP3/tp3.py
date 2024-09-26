import os
import time
import pandas as pd


df = pd.read_excel(io=r'TP3\TablaCapitales.xlsx', sheet_name="Sheet1")
arregloDistancias = df.to_numpy()

capitales=arregloDistancias[:,0].copy() #arreglo con los nombres de las capitales

'''
def distanciaParaRecorrido(arregloDeRecorridos):
    distancia = 0
    for i in range(len(arregloDeRecorridos)-1):
        distancia += arregloDistancias[arregloDeRecorridos[i]][arregloDeRecorridos[i+1]+1]
    return distancia
'''

#APARTADO A


def recorreDesde(primeraCapital):   #primeraCapital es el indice de la capital de donde arranca
    visitadas[primeraCapital]=1                    #marca como visitada donde arranca
    orden[0]=primeraCapital                       #pone en la primera posicion del arreglo de orden la capital de donde arranca
    capActual=primeraCapital                     #pone la capital de donde arranca como la capital actual
    print ("\n\nCiudad de partida : ",capActual,"-",capitales[capActual])
    print("Han sido visitadas: ",visitadas)
    print("El orden es: ", orden)
    while posActual<24:                 #mientras no haya pasado por todas las capitales
      capActual= capitalMasCercana(capActual)          #busca la capital mas cercana a la actual
    print("\n\n_____FIN_____")
    print ("Ultima ciudad visitada : ",capActual,"-",capitales[capActual])
    print("Han sido visitadas: ",visitadas)
    print("El orden es: ", orden)
    return orden


def capitalMasCercana(capActual):
    global posActual #arranca en 1
    distancias = arregloDistancias[capActual][1:].copy()  #distancias desde donde estoy parado
    minimaDistancia=9999
    for i in range (24):                          #recorre cada posicion del arreglo de distancias
        if distancias[i]<minimaDistancia and visitadas[i]==0: #si es la distancia mas corta que no pase
            minimaDistancia=distancias[i]                     #guardo la distancia
            proximaCapital=i
    orden[posActual]=proximaCapital                           #pongo el indice de la capital en el arreglo del orden
    posActual+=1                                      #me muevo una posicion en el arreglo de orden y la dejo lista para la prox iteracion                     
    visitadas[proximaCapital]=1
    print("\n Arranqué en (",capActual,"-", capitales[capActual],") y voy a (",proximaCapital,"-",capitales[proximaCapital],") a una distancia de: ",minimaDistancia)
    print("Han sido visitadas: ",visitadas)
    print("El orden es: ", orden) 
    return proximaCapital





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
    #declaro variables / las reinicio
    visitadas = [0 for _ in range(24)] #arreglo de 0 y 1 que marca por que capital pasó
    orden = [0 for _ in range(24)] #arreglo que guarda el numero de la capital visitada en el orden que se visito
    posActual=1

    if op == "A":
       for i in range(24): 
           print(i, capitales[i])
       cap=int(input("Ingrese la capital deseada: ")) #VALIDAR
       recorreDesde(cap)

    #if op == "B":
    #   min=999999
    #   for i in range(24): 
    #       distancia, arreglo =funcionA(i) #QUE ESTA EN apartadoA.py, debería retornar el arreglo del orden como minimo 
    #       if distancia<min:
    #           indiceMin=i
    #           min=distancia
    #   print("El recorrido es menor arrancando en ",capitales[indiceMin],". La distancia es: ",distancia )

    #if op == "C":
    #   AG



    #os.system('cls')
    print("_"*90+"\n")
    print("¿Desea ejecutar otra opción?")
    op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()
    while op != "A" and op != "B" and op != "C" and op != "S":
        os.system('cls')
        print("_"*90+"\n")
        print("\033[91mOpción no valida\033[0m")
        op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()
print("\n\033[91m--- Fin del programa ---\033[0m")





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