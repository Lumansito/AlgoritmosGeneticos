import random

numIndividuos = 10
numGenes = 30
individuos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] 
valObj = [0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
porcFitness = [0 for i in range(numIndividuos)]

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
        totalObj += valObj[i] #acumula la sumatoria de valor obj

    return totalObj


def funcionFitness():
    suma = 0
    total = calculoObjetivo()
    
    for i in range(numIndividuos):
        porcFitness[i]=valObj[i]/total
        suma += porcFitness[i]


calculoObjetivo()
print(valObj)
print(individuos)