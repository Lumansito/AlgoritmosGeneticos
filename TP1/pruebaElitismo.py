numIndividuos=5
valObj = [0.7,0.5,0.4,0.2,0.5]
individuos=[1,2,3,4,5]


def elitismo(n):    #Selecciona los n mejores individuos del arreglo individuos
    global mayores, indices

    mayores = [-1 for _ in range(n)]
    indices = [-1 for _ in range (n)]
    
    for j in range(n):
        for i in range(numIndividuos):
            
            if(valObj[i]>mayores[j] and not (i in indices)):
                if(i==0):
                    print("entro")
                mayores[j]=valObj[i]
                indices[j]=i

    print("Los mejores")
    for i in range(n):
        print(individuos[indices[i]])

elitismo(4)