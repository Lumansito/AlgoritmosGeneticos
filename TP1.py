import random
import matplotlib.pyplot as plt
import time



def inicializarPoblacion():
    #Recorremos el arreglo y lo cargamos con valores Random
    for i in range(numIndividuos):
        for j in range(numGenes):
            individuos[i][j]= random.randint(0,1)

    
def funcionObjetivo(x):
    
    valor= ( (x / (2 ** 30 - 1)) ** 2)
    return valor



def calculoObjetivo():
    
    totalObj = 0  #total de la funcion objetivo
    for i in range(numIndividuos):  #para cada individuo
        binario = ''.join(map(str,individuos[i])) #Convertir el arreglo de digitos binarios en un valor decimal
        numDecimal = int(binario, 2)    
        valObj[i] = funcionObjetivo(numDecimal) #guarda los valores de la func obj de cada indiv
        #print(valObj[i] ,  ' indice: ' , i)
        totalObj += valObj[i] #acumula la sumatoria de valor obj
    
   
    #print("###########")
    #print(totalObj)
    #print("######")
    return totalObj
        
def funcionFitness():
    suma = 0
    total = calculoObjetivo()
    for i in range(numIndividuos):
        porcFitness[i]=valObj[i]/total
        suma += porcFitness[i]
    #print("PORCENTAJE FITNES")
    #print(porcFitness)

def elitismo():
    print("\033[91m ELITISMO################# \033[0m")
    print("ANTES",individuos)
    individuos_ordenados = sorted(individuos,reverse=True)
    print("ORDENADOS",individuos_ordenados)
    for i in range(2):
        print(individuos_ordenados[i])
    
    
    

def ruleta() :
    global individuos

    hijos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] #para guardar los hijos
    porcentajes =[0 for i in range(1000)] #inicializamos el arreglo de los individuos
    indAct = 0                            #probar con 10 000 para individuos con muy poco fitness
    for i in range(numIndividuos): 
        fit = int(porcFitness[i]*1000)
        for j in range(fit):
            porcentajes[indAct+j] = i
        indAct = indAct + fit
    #print(indAct)
    #print(porcentajes)
    #for i in range (X):
        #pasa derecho los X con mejor fitness

    for i in range(numIndividuos): #numIndividuos-X veces se hace la ruleta para llenar el resto
        if(indAct==1000):   #Sino existia la posibilidad de que el arreglo porcetajes se exeda del limite.
            indAct=999
        num = random.randint(0,indAct)#para no usar 1000 y agregarle posibilidades al ind 0 debido al truncamiento, el arreglo rara vez llega a completar las 1000 posiciones desiganadas
        
        aux = porcentajes[num]
        hijos [i] = individuos[aux].copy() #paso a un array hijos los ganadores
        #print("Gano el individuo: ",aux," ", individuos[aux])
    individuos = hijos

def torneo():
    global individuos
    N = 4
    hijos = [[0 for _ in range(numGenes)]for _ in range(numIndividuos)]
    for j in range (numIndividuos):
        candidatos = [0 for i in range(N)] #arreglo de indices de los 4 individuos a examinar
        for i in range(N):
            candidatos[i]=random.randint(0,numIndividuos-1) #Llenar el arreglo de cantidatos con 4 indices al azar
        mayor = 0 #val FO del mayor indiciduo de los 4
        indCandidatoFinal=0
        for i in range(N):
            if(valObj[candidatos[i]] > mayor):
                mayor = valObj[candidatos[i]]
                indCandidatoFinal = candidatos[i]

        hijos[j]=individuos[indCandidatoFinal].copy()  #Para que pase el valor y no el parametro del arreglo
        
    individuos = hijos

def mostrarDatosPorCorrida():
    global menorGlobal, mayorGlobal, valorMayorGlobal, valorMenorGlobal, acumCorridas
    valorMayor=0
    valorMenor=9999
    mayor = [0]*numGenes
    menor = [0]*numGenes
    total = calculoObjetivo() #se obtiene la sumatoria de FO de la generacion
    promedioValObjPorCorrida[acumCorridas]= total/numIndividuos #guarda el prom de la FO de la generacion
    acumCorridas +=1
    
    print("El promedio de la gen ",acumCorridas-1 ," es: ", total/ numIndividuos) 
    for i in range(numIndividuos):
        aux = valObj[i]
        if(aux>valorMayor):
            valorMayor = aux
            mayor = individuos[i].copy()
        if(aux<valorMenor):
            valorMenor = aux
            menor = individuos[i].copy()
        
        
        print('individuo actual: ',aux, individuos[i])
        print('mayor',valorMayorGlobal , mayorGlobal)
        print('Menor',valorMenorGlobal, menorGlobal)
        print(" ")

        
        if(aux > valorMayorGlobal):
            
            valorMayorGlobal = aux
            mayorGlobal = individuos[i].copy()
           

        if(aux < valorMenorGlobal):
            
            valorMenorGlobal = aux
            menorGlobal = individuos[i].copy()
           


    
    print("El valor maximo es: ", valorMayor , "y su representacion binaria del individuo es: ",mayor)
    print("El valor menor es: ", valorMenor , "y su representacion binaria del individuo es: ",menor)
     

def mostrarDatosGlobal():
    global valorMayorGlobal, valorMenorGlobal, mayorGlobal, menorGlobal

    print("El valor máximo de todas las corridas fue: ", valorMayorGlobal, "y el individuo es: ", mayorGlobal)
    print("El valor mínimo de todas las corridas fue: ", valorMenorGlobal, "y el individuo es: ", menorGlobal)




def crossover():
   ind = 0
   for j in range(numIndividuos//2):
        
        aux=random.randint(1,100)
        if(aux<=probCrossover*100):
            corte = random.randint(1,numGenes-1) #punto de corte
           # print(corte)
            #print("antes......")
            #print(individuos[ind],ind)
            #print(individuos[ind+1], ind+1)
            for i in range(corte,numGenes):                     
                aux2 = individuos[ind][i]
                individuos[ind][i] = individuos[ind+1][i]
                individuos[ind+1][i] = aux2
            #print("despues.....")
            #print(individuos[ind],ind)
            #print(individuos[ind+1], ind+1)
        ind+=2

def mutacionBinaria():
    for i in range(numIndividuos):
        if(random.randint(0,100)<=probMutacion*100):
            
            posicion = random.randint(0,numGenes-1)
            print("\033[91mMUTACION en individuo \033[0m", i," en pos ", posicion)
            #print("mutuacuin en ",i, "gen", posicion )
            #print(individuos[i])
            if individuos[i][posicion] == 1:
                individuos[i][posicion] = 0
            else:
                individuos[i][posicion] = 1
            #print(individuos[i])


def dibujarGrafico():

    numCorridas=[0 for _ in range(corridas)]
    for i in range(corridas):
        numCorridas[i] = i+1
        

    # Crear el gráfico de líneas
    plt.plot(numCorridas, promedioValObjPorCorrida)

    # Personalización
    plt.title('Gráfico de Líneas')
    plt.xlabel('Numero de corridas')
    plt.ylabel('Eje Y')

    # Mostrar el gráfico
    plt.show()






#PROGRAMA PRINCIPAL
#preguntar el numero de individuos y con cuantos genes 

global numGenes,numIndividuos, individuos, valObj, porcFitness,probCrossover, probMutacion, valorMayorGlobal, valorMenorGlobal, menorGlobal, mayorGlobal, corridas, promedioValObjPorCorrida, acumCorridas
numGenes = 30
numIndividuos = 10
probCrossover=0.75
probMutacion=0.05
valorMenorGlobal = 99999
valorMayorGlobal = 0
menorGlobal= [0]*30
mayorGlobal = [0]*30
corridas = 50

acumCorridas =0
#Definimos el arreglo de individuos
individuos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] 
valObj=[0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
porcFitness=[0 for i in range(numIndividuos)] #Para guaradar los valores del porcentaje que brinda la fun fitness para cada indiviuo

#para graficos
promedioValObjPorCorrida = [0 for _ in range(corridas)]

#OPCION A:
#inicializar -> funcion objetivo -> funcion fitness -> seleccion (ruleta) -> crossover (1 punto) -> mutacion 

#OPCION B:
#inicializar -> funcion objetivo -> funcion fitness -> seleccion (torneo) -> crossover (1 punto) -> mutacion
#TORNEO = 10 veces (se seleccionan 4 individuos al azar y pasa el que mejor fitness tiene)

#OPCION C:
#inicializar -> funcion objetivo -> funcion fitness -> elitismo (pasan 2 derecho)-> 
#seleccion (ruleta entre los 10, para seleccionar los 8 restantes) -> crossover (1 punto) -> mutacion 



#Ejecución Opcion A
inicializarPoblacion()
op = "R"
for i in range(corridas):
    print("-----------------",i,"-------------------------")
    print("PREVIO DE LAS MUTACIONES")
    print(individuos)
    funcionFitness()
    
    if (op == "R"):
        ruleta()
    elif ( op == "T"):
        torneo()
    elif (op == "RE"):
        print("Ruleta con elitismo")
    elitismo()
    crossover()
    mutacionBinaria()
    print("DESPUES DE LAS MUTACIONES")
    print(individuos)
    mostrarDatosPorCorrida()
    
mostrarDatosGlobal()
dibujarGrafico()