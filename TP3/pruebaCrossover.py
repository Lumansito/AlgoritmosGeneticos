#ALGORITMO GENETICO
import os
import random
import pandas as pd

#lucho
df = pd.read_excel(io=r'TP3\TablaCapitales.xlsx', sheet_name="Sheet1")
#mati
#df = pd.read_excel(io=r'TablaCapitales.xlsx', sheet_name="Sheet1")

arregloDistancias = df.to_numpy()

capitales=arregloDistancias[:,0].copy() #arreglo con los nombres de las capitales

numGenes = 24 #uno por cada capital
numIndividuos = 6 #CAMBIAR------------------------------------------> 50 
probCrossover = 0.5
probMutacion = 0.05


def calcularDistancia(orden):
    distancia = 0
    for i in range(23):
        distancia += arregloDistancias[orden[i]][orden[i+1]+1]
    distancia+=(arregloDistancias[orden[0]][orden[23]+1])
    return distancia


def algoritmoGenetico():
    os.system('cls')
    individuos = inicializarPoblacion()
    
    print("\n\033[91mPoblacion inicial\033[0m")
    for i in range(numIndividuos):
        print(individuos[i])
    
    valObj = [0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
    for i in range(numIndividuos):
        valObj[i]=calcularDistancia(individuos[i]) #le paso un orden de recorrido
    print("\n\033[91mLas distancias para cada individuo son \033[0m\n",valObj)
    valFitness = [0 for i in range(numIndividuos)] #Para guaradar los valores del porcentaje que brinda la fun fitness para cada indiviuo
    totalObjetivo = sum(valObj)
    
    for i in range(numIndividuos):
        valFitness[i]= round(1-(valObj[i]/totalObjetivo), 5) #ver que onda TODO
    print("\n\033[91mEl valor fitness es \033[0m\n",valFitness)
    
    individuos=torneo(individuos,valFitness)

    print("\n\033[91mDESPUES DE TORNEO\033[0m")
    for i in range(numIndividuos):
        print(individuos[i])

    individuos=crossoverCiclico(individuos)
    print("\n\033[91mDESPUES DE CROSSOVER\033[0m")
    for i in range(numIndividuos):
        print(individuos[i])

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
            puntoInicio=padre1[0]
            #print("\nINICIO CROSSOVER\npadre1: ",padre1,"\npadre2: ",padre2)
            while puntoInicio!=aux:

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
    #print(individuos)
    return individuos




def torneo(individuos,valFitness):

    N = 2  #cantidad de individuos a participar de cada torneo 
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

algoritmoGenetico()