import time
import pandas as pd

df = pd.read_excel(io=r'TablaCapitales.xlsx', sheet_name="Sheet1")
array = df.to_numpy()
print(array)

capitales=array[:,0].copy()
print(capitales)




#from tp3 import array 

visitadas = [0 for _ in range(24)] #arreglo de 0 y 1 que marca por que capital pasó
orden = [0 for _ in range(24)] #arreglo que guarda el numero de la capital visitada en el orden que se visito
posActual=1

def recorreDesde(capInicial):
    global visitadas, orden, posActual, capActual

    print("Arrancamos en: ",capitales[capInicial])

    visitadas[capInicial]=1                    #marca donde arranca
    orden[0]=capInicial
    
    capActual=capInicial
    while sum(visitadas)<24:
      print(sum(visitadas))
      print ("POS ACTUAL: ",posActual)
      print(visitadas)
      print(orden)
      capitalMasCercana(capActual)
    print("Han sido visitadas: ",visitadas)
    print("El orden es: ", orden)


def capitalMasCercana(capActual):
    global visitadas, orden, posActual
    distancias = array[capActual][1:].copy()  #distancias desde donde estoy parado
    
    min=9999

    for i in range (24):                          #recorre cada posicion del arreglo de distancias
        if distancias[i]<min and visitadas[i]==0: #si es la distancia mas corta que no pase
            min=distancias[i]                     #guardo la distancia
            orden[posActual]=i 
            capActual=i                           #pongo el indice de la capital en el arreglo del orden
    posActual+=1                                      #me muevo una posicion en el arreglo de orden                     #actualizo la capital actual a la nueva encontrada (la mas cercana)
    visitadas[capActual]=1                        #
    print("La prox más cercana es: ",capitales[capActual],"a una distancia de: ",min)

recorreDesde(1)

#a)Permitir ingresar una provincia y hallar la ruta de distancia mínima que logre unir todas las capitales de provincias 
# de la República Argentina partiendo de dicha capital utilizando la siguiente heurística: 
# “Desde cada ciudad ir a la ciudad más cercana no visitada.”  
# Recordar regresar siempre a la ciudad de partida. Presentar un mapa de la República con el recorrido indicado. 
# Además   indicar la ciudad de partida, el recorrido completo y la longitud del trayecto. 