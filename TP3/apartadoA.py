import pandas as pd

df = pd.read_excel(io=r'TP3\TablaCapitales.xlsx', sheet_name="Sheet1")
array = df.to_numpy()
print(array)

capitales=array[0]




#from tp3 import array 

visitadas = [0 for _ in range(23)] #arreglo de 0 y 1 que marca por que capital pasó
orden = [0 for _ in range(23)] #arreglo que guarda el numero de la capital visitada en el orden que se visito
posActual=1

def recorreDesde(capInicial):
    global visitadas, orden, posActual, capActual

    print("Arrancamos en: ",capitales[capInicial])

    
    
    visitadas[capInicial]=1                    #marca donde arranca
    orden[0]=capInicial
    
    capActual=capInicial
    while sum(visitadas)<24:
      print ("POS ACTUAL: ",posActual)
      capitalMasCercana(capActual)
    print("Han sido visitadas: ",visitadas)
    print("El orden es: ", orden)


def capitalMasCercana(capActual):
    global visitadas, orden, posActual
    distancias = array[capActual][1:].copy()  #distancias desde donde estoy parado
    print("las distancias son: ", distancias)
    
    min=9999

    for i in range (23):                          #recorre cada posicion del arreglo de distancias
        if distancias[i]<min and visitadas[i+1]!=1: #si es la distancia mas corta que no pase
            min=distancias[i]                     #guardo la distancia
            orden[posActual]=i 
            capActual=i                           #pongo el indice de la capital en el arreglo del orden
    posActual+=1                                      #me muevo una posicion en el arreglo de orden                     #actualizo la capital actual a la nueva encontrada (la mas cercana)
    visitadas[capActual]=1                        #
    print("La prox más cercana es: ",capitales[capActual])

recorreDesde(3)

#a)Permitir ingresar una provincia y hallar la ruta de distancia mínima que logre unir todas las capitales de provincias 
# de la República Argentina partiendo de dicha capital utilizando la siguiente heurística: 
# “Desde cada ciudad ir a la ciudad más cercana no visitada.”  
# Recordar regresar siempre a la ciudad de partida. Presentar un mapa de la República con el recorrido indicado. 
# Además   indicar la ciudad de partida, el recorrido completo y la longitud del trayecto. 