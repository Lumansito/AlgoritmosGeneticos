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
numIndividuos = 10 #CAMBIAR------------------------------------------> 50 
probCrossover = 0.75
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
    #individuos=crossoverCiclico(individuos)
    

def crossoverCiclico(individuos):
    indice = 0
    for j in range(numIndividuos//2):
        aux=random.randint(1,100)
        if(aux<=probCrossover*100):
            padre1= individuos[indice].copy()
            padre2= individuos[indice+1].copy()
            
            hijo1=[0 for _ in range(numGenes)]
            hijo2=[0 for _ in range(numGenes)]
            
            indH1=0
            indH2=0
            indP1=0
            indP2=0

            puntoInicio=padre1[0]
            puntoFinal=-1

            hijo1[indH1]=padre1[indP1] #toma el primer gen del primer padre
            indH1+=1
            
            hijo2[0]=padre2[0]
            indH2+=1

            while puntoInicio!=puntoFinal:
                contenidoPadre2=padre2[indP2] #1 
                
                
                indP1=padre2.index(contenidoPadre2) #busco el 1 en el primer arreglo
                
              
        indice+=2
    return




def torneo(individuos,valFitness):

    N = 4  #cantidad de individuos a participar de cada torneo 
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