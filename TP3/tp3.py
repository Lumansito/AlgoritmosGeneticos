from datetime import datetime
import os
import random
import pandas as pd
from mapa.dibujaMapa import dibujarMapa


#lucho
df = pd.read_excel(io=r'TP3\TablaCapitales.xlsx', sheet_name="Sheet1")
#mati
#df = pd.read_excel(io=r'TablaCapitales.xlsx', sheet_name="Sheet1")

arregloDistancias = df.to_numpy()

capitales=arregloDistancias[:,0].copy() #arreglo con los nombres de las capitales



def recorreDesde(primeraCapital):   #primeraCapital es el indice de la capital de donde arranca
    visitadas[primeraCapital]=1                    #marca como visitada donde arranca
    orden[0]=primeraCapital                       #pone en la primera posicion del arreglo de orden la capital de donde arranca
    capActual=primeraCapital                    #pone la capital de donde arranca como la capital actual
    
    #print("Han sido visitadas: ",visitadas)
    #print("El orden es: ", orden)
    while posActual<24:                 #mientras no haya pasado por todas las capitales
      capActual= capitalMasCercana(capActual)          #busca la capital mas cercana a la actual
    print ("\nUltima ciudad visitada : ",capActual,"-",capitales[capActual])
    print("\nHan sido visitadas: ",visitadas)
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
    #print("\n Arranqué en (",capActual,"-", capitales[capActual],") y voy a (",proximaCapital,"-",capitales[proximaCapital],") a una distancia de: ",minimaDistancia)
    #print("Han sido visitadas: ",visitadas)
    #print("El orden es: ", orden) 
    return proximaCapital


def calcularDistancia(orden):
    distancia = 0
    for i in range(23):
        distancia += arregloDistancias[orden[i]][orden[i+1]+1]
        #print("Distancia desde ",capitales[orden[i]]," hasta ",capitales[orden[i+1]],": ",arregloDistancias[orden[i]][orden[i+1]+1])
        #print("Distancia acumulada: ",distancia)
    #print("Distancia desde ",capitales[orden[23]]," hasta ",capitales[orden[0]],": ",arregloDistancias[orden[23]][orden[0]+1])
    distancia+=(arregloDistancias[orden[0]][orden[23]+1])
    return distancia


#ALGORITMO GENETICO
numGenes = 24 #uno por cada capital
numIndividuos = 50 
probCrossover = 0.75
probMutacion = 0.1
ciclos = 10


def algoritmoGenetico():
    inicializarValoresCorridas()
    individuos = inicializarPoblacion()
    print(individuos) 
    
    valObj = [0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
    valFitness = [0 for i in range(numIndividuos)] #Para guaradar los valores del porcentaje que brinda la fun fitness para cada indiviuo

    for iteracion in range(ciclos):
        print("\n\033[91m_______Ciclo ",iteracion+1,"_______\033[0m")
        
        #calculo del valor objetivo
        for i in range(numIndividuos):
            valObj[i]=calcularDistancia(individuos[i]) #le paso un orden de recorrido
        #print("\n\033[91mLas distancias para cada individuo son \033[0m\n",valObj)
        print("\n\033[92mAverage distance for this cycle:\033[0m", sum(valObj) / len(valObj))
        
        #calculo del valor fitness
        totalObjetivo = sum(valObj)
        for i in range(numIndividuos):
            valFitness[i]= round(1-(valObj[i]/totalObjetivo), 5) #ver que onda TODO
           
        #print("\n\033[91mEl valor fitness es \033[0m\n",valFitness)
        #print("\n\033[92mAverage fitness for this cycle:\033[0m", sum(valFitness) / len(valFitness))
        
        guardarDatosPorCorrida(iteracion, totalObjetivo, valObj, individuos)

        #torneo
        individuos=torneo(individuos,valFitness)
        #print("\n\033[91mDESPUES DE TORNEO\033[0m")
        #for i in range(numIndividuos):
        #    print(individuos[i])

        #crossover
        individuos=crossoverCiclico(individuos)
        #print("\n\033[91mDESPUES DE CROSSOVER\033[0m")
        #for i in range(numIndividuos):
        #    print(individuos[i])
        
        #mutacion

        muta = random.randint(1,100)
        if muta <= 50:
            individuos=mutacionSwap(individuos) 
        else:
            individuos=mutacionInversion(individuos)

        #individuos=mutacionSwap(individuos)
        #individuos=mutacionAdjointSwap(individuos) #pesimos resultados wtf
        #individuos=mutacionInversion(individuos)
        
        #print("\n\033[91mDESPUES DE MUTACION\033[0m")
        #for i in range(numIndividuos):
        #    print(individuos[i])
    realizarTabla()

def crossoverCiclico(individuos):
    indice = 0
    for j in range(numIndividuos//2):
        aux=random.randint(1,100)
        if(aux<=probCrossover*100):
            padre1= individuos[indice].copy()
            padre2= individuos[indice+1].copy()
            
            hijo1=[-1 for _ in range(numGenes)]
            hijo2=[-1 for _ in range(numGenes)]

            hijo1[0]=padre1[0] #toma el primer gen del primer padre
            hijo2[0]=padre2[0]  #toma el primer gen del segundo padre

            indPadre=0
            aux=-1

            #print("\nINICIO CROSSOVER\npadre1: ",padre1,"\npadre2: ",padre2)
            while padre1[0]!=aux:

                indPadre=padre1.index(padre2[indPadre]) #obtengo la posicion del (contenido del padre 2) en el padre 1
                
                hijo1[indPadre]=padre1[indPadre] #asigno el contenido del padre 1 en la posicion actual en el hijo 1

                hijo2[indPadre]=padre2[indPadre] #asigno el contenido del padre 2 en la posicion actual en el hijo 2

                aux=padre2[indPadre]
                #print("mientras crossover ")
                #print(hijo1)
                #print(hijo2)
            #print("\n\033[91mfin del crossover\033[0m")
            #print(hijo1)
            #print(hijo2)

            for i in range(numGenes):
                if hijo1[i]==-1:
                    hijo1[i]=padre2[i]
                    hijo2[i]=padre1[i]
            #print("\n\033[91mdespues de rellenar\033[0m")
            #print(hijo1)
            #print(hijo2)
            individuos[indice]= hijo1.copy()
            individuos[indice+1]= hijo2.copy()
        indice+=2
    return individuos

def torneo(individuos,valFitness):

    N = 8  #cantidad de individuos a participar de cada torneo 
    hijos = [[0 for _ in range(numGenes)]for _ in range(numIndividuos)]
    
    for j in range (numIndividuos):
        candidatos = [0 for i in range(N)] #arreglo de indices de los 4 individuos a examinar
        for i in range(N):
            candidatos[i]=random.randint(0,numIndividuos-1) #Llenar el arreglo de cantidatos con 4 indices al azar
        valorMayor = 0 #valor fitness del mayor individuo de los 4
        indiceMayor=0
        for i in range(N):
            if(valFitness[candidatos[i]] > valorMayor):
                valorMayor = valFitness[candidatos[i]]
                indiceMayor = candidatos[i]
        hijos[j]=individuos[indiceMayor].copy()  #selecciona al mejor individuo de los 4 y lo guarda en hijos
    return hijos

def inicializarPoblacion(): #Recorremos el arreglo y lo cargamos con una ruta al azar
    individuos=[[0 for i in range(numGenes)] for j in range(numIndividuos)]
    for i in range(numIndividuos): #Recorremos los 50 individuos
        individuos[i] = random.sample(range(numGenes), numGenes)  # Generamos una lista de números únicos del 0 al 23
    return individuos

def mutacionSwap(individuos):
    for i in range(numIndividuos):
        aux=random.randint(1,100)
        if(aux<=probMutacion*100):
            pos1=random.randint(0,numGenes-1)
            pos2=random.randint(0,numGenes-1)
            while pos1==pos2:
                pos2=random.randint(0,numGenes-1)
            aux=individuos[i][pos1]
            individuos[i][pos1]=individuos[i][pos2]
            individuos[i][pos2]=aux
    return individuos

def mutacionAdjointSwap(individuos):
    for i in range(numIndividuos):
        aux=random.randint(1,100)
        if(aux<=probMutacion*100):
            pos1=random.randint(0,numGenes-1)
            if pos1==23:
                pos2=22
            else:
                pos2=pos1+1
            aux=individuos[i][pos1]
            individuos[i][pos1]=individuos[i][pos2]
            individuos[i][pos2]=aux
    return individuos

def mutacionInversion(individuos):
    for i in range(numIndividuos):
        aux=random.randint(1,100)
        if(aux<=probMutacion*100):
            pos1=random.randint(0,numGenes-1)
            pos2=random.randint(0,numGenes-1)
            while pos1==pos2:
                pos2=random.randint(0,numGenes-1)
            if pos1>pos2:
                aux=pos1
                pos1=pos2
                pos2=aux
            while pos1<pos2:
                aux=individuos[i][pos1]
                individuos[i][pos1]=individuos[i][pos2]
                individuos[i][pos2]=aux
                pos1+=1
                pos2-=1
    return individuos

#guardar valores por ciclo
valorMenorGlobal = 99999
valorMayorGlobal = 0
menorGlobal = [0]*numGenes
mayorGlobal = [0]*numGenes

def inicializarValoresCorridas():
    global minimoFO, maximoFO, cromosomasMaximos, cromosomasMinimos, promedioValObjPorCorrida, acumCorridas
    acumCorridas = 0
    minimoFO = [0 for _ in range(ciclos)]
    maximoFO = [0 for _ in range(ciclos)]
    cromosomasMaximos = [0 for _ in range(ciclos)]
    cromosomasMinimos = [0 for _ in range(ciclos)]
    promedioValObjPorCorrida = [0 for _ in range(ciclos)]

def guardarDatosPorCorrida(iteracion, totalObjetivo, valObj, individuos):
    global menorGlobal, mayorGlobal, valorMayorGlobal, valorMenorGlobal, acumCorridas,maximoFO,minimoFO,cromosomasMaximos,cromosomasMinimos, promedioValObjPorCorrida
    valorMayor = 0
    valorMenor = 99999999
    mayor = [0]*numGenes
    menor = [0]*numGenes
    promedioValObjPorCorrida[acumCorridas]= totalObjetivo/numIndividuos #guarda el prom de la FO de la generacion
    acumCorridas +=1
    
    for i in range(numIndividuos):
        aux = valObj[i]
        if(aux>valorMayor):
            valorMayor = aux
            mayor = individuos[i].copy()
        if(aux<valorMenor):
            valorMenor = aux
            menor = individuos[i].copy()  
        if(aux > valorMayorGlobal):
            valorMayorGlobal = aux
            mayorGlobal = individuos[i].copy()
        if(aux < valorMenorGlobal):
            valorMenorGlobal = aux
            menorGlobal = individuos[i].copy()

    maximoFO[iteracion] = valorMayor
    minimoFO[iteracion] = valorMenor
    cromosomasMaximos[iteracion] = mayor
    cromosomasMinimos[iteracion] = menor

def realizarTabla():    
    global individuos,valObj,porcFitness
    datos_tabla = {
        "Generación" : [i+1 for i in range(ciclos)],
        "Mínimo FO": minimoFO,
        "Máximo FO": maximoFO,
        "Cromosoma Máximo": cromosomasMaximos,
        "Cromosoma Mínimo": cromosomasMinimos,
        "Promedio": promedioValObjPorCorrida
    }
    current_time = datetime.now().strftime("%H-%M-%S") #para no tener que borrar el excel cada vez
    df_individuos = pd.DataFrame(datos_tabla)
    
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # Construct the file path
    file_path = os.path.join(current_dir, f"TablaAG_{current_time}.xlsx")
    
    with pd.ExcelWriter(file_path) as writer:
        df_individuos.to_excel(writer, sheet_name = 'Individuos', index = False)

















#MENU
os.system('cls')
op = ""
print("_"*90+"\n")
op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()
while op != "A" and op != "B" and op != "C" and op != "S":
    print("_"*90+"\n")
    print("\033[91mOpción no valida\033[0m")
    op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()

while op !="S":
    #declaro variables para opciones A y B
    visitadas = [0 for _ in range(24)] #arreglo de 0 y 1 que marca por que capital pasó
    orden = [0 for _ in range(24)] #arreglo que guarda el numero de la capital visitada en el orden que se visito
    posActual=1

    if op == "A":
       for i in range(24): 
           print(i, capitales[i])
       puntoPartida=int(input("Ingrese la capital deseada: ")) #VALIDAR
       print ("\nCiudad de partida : ",puntoPartida,"-",capitales[puntoPartida])
       orden=recorreDesde(puntoPartida)
       print("\nEl orden es: ", orden)
       distancia=calcularDistancia(orden)
       print("\nDistancia total desde ",capitales[orden[0]],": ",distancia)
       dibujarMapa(orden)


    if op == "B":
       min=99999999
       for i in range(24):
            print ("\nCiudad de partida : ",i,"-",capitales[i])
            orden=recorreDesde(i)
            print("\nEl orden es: ", orden)
            distanciaTotal=calcularDistancia(orden) 
            print("\nDistancia total desde ",capitales[orden[0]],": ",distanciaTotal)
            if distanciaTotal<min:
               indiceMin=i
               min=distanciaTotal
               ordenMin=orden
               print("\033[91m\n\nNUEVO MENOR########################################################\033[0m\n", capitales[indiceMin], " - ", min)
            
            visitadas = [0 for _ in range(24)] #reseteo
            orden = [0 for _ in range(24)] #reseteo
            posActual=1 #reseteo
            print("____________FIN recorrido ",i," _____________\n\n")
       print("\nEl recorrido es menor arrancando en ",capitales[indiceMin],". La distancia es: ",min )
       dibujarMapa(ordenMin)

    if op == "C":
        algoritmoGenetico()

    print("_"*90+"\n")
    print("¿Desea ejecutar otra opción?")
    op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()
    while op != "A" and op != "B" and op != "C" and op != "S":
        print("_"*90+"\n")
        print("\033[91mOpción no valida\033[0m")
        op = input("   a) Calcular recorrido con heurística desde un lugar en concreto\n   b) Recorrido mas corto con heurística\n   c) Recorrido mas corto con algoritmo genético\n   s) Salir\nIngrese la opción deseada: ").upper()
print("\n\033[91m--- Fin del programa ---\033[0m")


