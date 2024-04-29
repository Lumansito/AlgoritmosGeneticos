import random

def inicializarPoblacion(numIndividuos, numGenes):
    
    #Definimos el arreglo de individuos
    individuos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] 

    #Recorremos el arreglo y lo cargamos con valores Random
    for i in range(numIndividuos):
        for j in range(numGenes):
            individuos[i][j]= random.randint(0,1)
    print(individuos[0])
    calculoObjetivo(individuos, numIndividuos)
    
def funcionObjetivo(x):
    
    valor= ( (x / (2 ** 30 - 1)) ** 2)
    print(valor)
    return valor

def  calculoObjetivo(individuos, numIndividuos):
    valObj=[0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
    totalObj = 0  #total de la funcion objetivo
    for i in range(numIndividuos):  #para cada individuo
        binario = ''.join(map(str,individuos[i])) #Convertir el arreglo de digitos binarios en un valor decimal
        numDecimal = int(binario, 2)    
        print(numDecimal)
        valObj[i] = funcionObjetivo(numDecimal)
        totalObj += valObj[i]
    
    print(valObj)
    print(totalObj)
        
def funcionFitness():
        

    

inicializarPoblacion(10,30)



#inicializar -> funcion objetivo -> funcion fitness -> seleccion (ruleta) -> crossover (1 punto) -> mutacion 
