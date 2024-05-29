import random
import pandas as pd
import os
import time


def inicializarPoblacion(): #Recorremos el arreglo y lo cargamos con valores al azar
    global individuos
    
    for i in range(numIndividuos):
        for j in range(numGenes):
           individuos[i][j]= random.randint(0,1)


def funcionObjetivo(x): # segun enunciado
    valor= ( (x / (2 ** 30 - 1)) ** 2)
    
    return valor


def calculoObjetivo():
    totalObj = 0  
    
    for i in range(numIndividuos):  #para cada individuo
        binario = ''.join(map(str,individuos[i])) #Convertir el arreglo de digitos a binario
        numDecimal = int(binario, 2) #Convertir el binario a decimal
        valObj[i] = funcionObjetivo(numDecimal) #guarda los valores de la FO de cada individuo respetando su posicion
        totalObj += valObj[i] #acumula la sumatoria de valores de FO

    return totalObj #sumatoria de la funcion objetivo de la generacion


def funcionFitness():     
    total = calculoObjetivo()
    
    for i in range(numIndividuos):
        porcFitness[i]=valObj[i]/total #Calcula el porcentaje de fitness de cada individuo 


def guardarElitismo(n):    #Selecciona los n mejores individuos del arreglo individuos
    global elite
    elite = [[] for i in range(n)]
    mayores = [-1 for _ in range(n)]
    indices = [-1 for _ in range (n)]
    
    for j in range(n):
        for i in range(numIndividuos):
            if(valObj[i]>mayores[j] and not (i in indices)):
                mayores[j]=valObj[i]
                indices[j]=i
    for i in range(n):
        elite[i] = individuos[indices[i]].copy()
    
    
def pegarElitismo(n):
    for i in range(n): 
        individuos[i] = elite[i]


def ruleta():
    global individuos
    hijos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] #para guardar los hijos
    porcentajes = [0 for i in range(1000)]  #inicializamos el arreglo de la ruleta
    indAct = 0 #para llevar la cuenta de las posiciones que se van llenando
    
    for i in range(numIndividuos): 
        fit = int(porcFitness[i]*1000)
        for j in range(fit):
            porcentajes[indAct+j] = i
        indAct = indAct + fit
    for i in range(numIndividuos): #numIndividuos veces se hace la ruleta para llenar el resto
        if(indAct == 1000):   #para evitar que el arreglo porcetajes se exceda del limite
            indAct = 999
        num = random.randint(0,indAct) #para no usar 1000 y agregarle posibilidades al ind 0 debido al truncamiento
        aux = porcentajes[num]
        hijos [i] = individuos[aux].copy() #paso por valor a un array hijos los ganadores
    individuos = hijos


def torneo():
    global individuos
    N = 4  #cantidad de individuos a participar de cada torneo segun enunciado
    hijos = [[0 for _ in range(numGenes)]for _ in range(numIndividuos)]
    
    for j in range (numIndividuos):
        candidatos = [0 for i in range(N)] #arreglo de indices de los 4 individuos a examinar
        for i in range(N):
            candidatos[i]=random.randint(0,numIndividuos-1) #Llenar el arreglo de cantidatos con 4 indices al azar
        mayor = 0 #val FO del mayor individuo de los 4
        indCandidatoFinal=0
        for i in range(N):
            if(valObj[candidatos[i]] > mayor):
                mayor = valObj[candidatos[i]]
                indCandidatoFinal = candidatos[i]
        hijos[j]=individuos[indCandidatoFinal].copy()  #selecciona al mejor individuo de los 4 y lo guarda en hijos
    individuos = hijos
        

def guardarDatosPorCorrida(numCorrida):
    global menorGlobal, mayorGlobal, valorMayorGlobal, valorMenorGlobal, acumCorridas,maximoFo,minimoFo,cromosomasMaximos,cromosomasMinimos, promedioValObjPorCorrida
    valorMayor = 0
    valorMenor = 9999
    mayor = [0]*numGenes
    menor = [0]*numGenes
    total = calculoObjetivo() #se obtiene la sumatoria de FO de la generacion
    promedioValObjPorCorrida[acumCorridas]= total/numIndividuos #guarda el prom de la FO de la generacion
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

    maximoFo[numCorrida] = valorMayor
    minimoFo[numCorrida] = valorMenor
    cromosomasMaximos[numCorrida] = mayor
    cromosomasMinimos[numCorrida] = menor


def crossover():
   ind = 0
   for j in range(numIndividuos//2):
        aux=random.randint(1,100)
        if(aux<=probCrossover*100):
            corte = random.randint(1,numGenes-1) #punto de corte
            for i in range(corte,numGenes):                     
                aux2 = individuos[ind][i]
                individuos[ind][i] = individuos[ind+1][i]
                individuos[ind+1][i] = aux2
        ind+=2


def mutacionBinaria():
    for i in range(numIndividuos):
        if(random.randint(0,100)<=probMutacion*100):
            posicion = random.randint(0,numGenes-1)
            if individuos[i][posicion] == 1:
                individuos[i][posicion] = 0
            else:
                individuos[i][posicion] = 1


def nombrarArchivo(op,corridas):
    if op == "R":
        return "Ruleta_" + str(corridas)+".xlsx"
    elif op == "T":
        return "Torneo_" + str(corridas)+".xlsx"
    elif op == "RE":
        return "RuletaConElitismo_" + str(corridas)+".xlsx"


def realizarTabla():
    global individuos,valObj,porcFitness
    datos_tabla = {
        "Generación" : [i+1 for i in range(corridas)],
        "Mínimo FO": minimoFo,
        "Máximo FO": maximoFo,
        "Cromosoma Máximo(binario)":cromosomasMaximos,
        "Cromosoma Mínimo(binario)": cromosomasMinimos,
        "Promedio":promedioValObjPorCorrida
    }
    df_individuos = pd.DataFrame(datos_tabla)
    with pd.ExcelWriter(nombreArchivoExcel) as writer:
        df_individuos.to_excel(writer, sheet_name = 'Individuos', index = False)


#PROGRAMA PRINCIPAL
 

global numGenes,numIndividuos, individuos, valObj, porcFitness,probCrossover, probMutacion, valorMayorGlobal, valorMenorGlobal, menorGlobal, mayorGlobal, corridas, promedioValObjPorCorrida, nombreArchivoExcel
numGenes = 30 #Estan definidos por el enunciado, pero se puede pedir al usuario
numIndividuos = 10
probCrossover = 0.75
probMutacion = 0.05
valorMenorGlobal = 99999
valorMayorGlobal = 0
menorGlobal = [0]*numGenes
mayorGlobal = [0]*numGenes
corridas = 0 #Este valor es modificado en la ejecucion

#Definimos el arreglo de individuos
individuos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] 
valObj = [0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
porcFitness = [0 for i in range(numIndividuos)] #Para guaradar los valores del porcentaje que brinda la fun fitness para cada indiviuo


#Incializar los valores que dependen de las corridas
def inicializarValoresCorridas():
    global minimoFo, maximoFo, cromosomasMaximos, cromosomasMinimos, promedioValObjPorCorrida, corridas, acumCorridas
    
    acumCorridas = 0
    minimoFo = [0 for _ in range(corridas)]
    maximoFo = [0 for _ in range(corridas)]
    cromosomasMaximos = [0 for _ in range(corridas)]
    cromosomasMinimos = [0 for _ in range(corridas)]
    promedioValObjPorCorrida = [0 for _ in range(corridas)]


op = ""
print("_"*90)
op = input("   R - Ruleta\n   T - Torneo\n   RE - Ruleta con Elitismo\n   F - Salir\nIngrese el método de selección deseado: ").upper()
while op.upper() != "R" and op.upper() != "T" and op.upper() != "RE" and op.upper() != "F":
    print("Opcion no valida")
    op = input("   R - Ruleta\n   T - Torneo\n   RE - Ruleta con Elitismo\n   F - Salir\nIngrese el método de selección deseado: ").upper()

while op.upper() !="F":
    corridas = int(input("Ingrese el numero de corridas que desea Realizar: "))
    nombreArchivoExcel = nombrarArchivo(op,corridas)
    current_directory = os.getcwd()
    time.sleep(1)
    print("\nLos resultados se encuentran en: \033[92m",current_directory,"\033[0m\nBajo el nombre de: \033[92m",nombreArchivoExcel+"\033[0m")
    inicializarValoresCorridas()
    inicializarPoblacion()
    for i in range(corridas):
        funcionFitness()
        guardarDatosPorCorrida(i)
        if (op == "R"):
            ruleta()
        elif ( op == "T"):
            torneo()
        elif (op == "RE"):
            guardarElitismo(2)
            ruleta()
        crossover()
        mutacionBinaria()
        if (op == "RE"):
            pegarElitismo(2)
    realizarTabla()
    time.sleep(4)
    print("_"*90+"\n")
    print("Desea realizar una nueva corrida?")
    op = input("   R - Ruleta\n   T - Torneo\n   RE - Ruleta con Elitismo\n   F - Salir\nIngrese el método de selección deseado: ").upper()
    while op.upper() != "R" and op.upper() != "T" and op.upper() != "RE" and op.upper() != "F":
        print("Opción no valida")
        op = input("   R - Ruleta\n   T - Torneo\n   RE - Ruleta con Elitismo\n   F - Salir\nIngrese el método de selección deseado: ").upper()
print("\n--- Fin del programa ---")