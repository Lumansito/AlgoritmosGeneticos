import random


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
        print(valObj[i] ,  ' indice: ' , i)
        totalObj += valObj[i] #acumula la sumatoria de valor obj
    
    print("###########")
    print(totalObj)
    print("######")
    return totalObj
        
def funcionFitness():
    suma = 0
    total = calculoObjetivo()
    for i in range(numIndividuos):
        porcFitness[i]=valObj[i]/total
        suma += porcFitness[i]
        
    print(porcFitness)

def ruleta():
    global individuos

    hijos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] #para guardar los hijos
    porcentajes =[0 for i in range(1000)] #inicializamos el arreglo de los individuos
    indAct = 0                            #probar con 10 000 para individuos con muy poco fitness
    for i in range(numIndividuos): 
        fit = int(porcFitness[i]*1000) 
        for j in range(fit):
            porcentajes[indAct+j] = i
        indAct = indAct + fit
    print(indAct)
    #print(porcentajes)
    for i in range(numIndividuos):
        num = random.randint(0,indAct) #para no usar 1000 y agregarle posibilidades al ind 0 debido al truncamiento, el arreglo rara vez llega a completar las 1000 posiciones desiganadas
        aux = porcentajes[num]
        hijos [i] = individuos[aux] #paso a un array hijos los ganadores
        print("Gano el individuo: ",aux," ", individuos[aux])
    individuos = hijos


def crossover():
   ind=0
   for j in range(5):
        print("entro")
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
            
            print("mutuacuin en ",i, "gen", posicion )
            print(individuos[i])
            if individuos[i][posicion] == 1:
                individuos[i][posicion] = 0
            else:
                individuos[i][posicion] = 1
            print(individuos[i])

#PROGRAMA PRINCIPAL
#preguntar el numero de individuos y con cuantos genes 

global numGenes,numIndividuos, individuos, valObj, porcFitness,probCrossover, probMutacion
numGenes = 30
numIndividuos = 10
probCrossover=0.75
probMutacion=0.01
#Definimos el arreglo de individuos
individuos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] 
valObj=[0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
porcFitness=[0 for i in range(numIndividuos)] #Para guaradar los valores del porcentaje que brinda la fun fitness para cada indiviuo

#OPCION A:
#inicializar -> funcion objetivo -> funcion fitness -> seleccion (ruleta) -> crossover (1 punto) -> mutacion 



#Ejecución
inicializarPoblacion()
for i in range(10):
    print("-----------------",i,"-------------------------")
    print(individuos)
    funcionFitness()
    ruleta()
    crossover()
    mutacionBinaria()


    