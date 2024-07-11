import time
#arreglo de todos los objetosA, [peso][precio]
objetosA = [[150,20],[325,40],[600,50],[805,36],[430,25],[1200,64],[770,54],[60,18],[930,46],[353,28]]
limiteMaxA = 4200
objetosB = [[1800,72],[600,36],[1200,60]]
limiteMaxB = 3000
objetosExp = [[150,20],[325,40],[600,50],[805,36],[430,25],[1200,64],[770,54],[60,18],[930,46],[353,28],[1800,72],[600,36],[1200,60],[400,30],[200,20]]
limiteMaxExp = 7000




#creamos un arreglo con todas las combinaciones posibles de 10 elementos
def cargaArreglo(objetosX):
    global arregloExhaustivo
    longitud = len(objetosX)
    arregloExhaustivo = [[0 for _ in range(longitud)]for _ in range(2**longitud)] #arreglo vacio de mochilas posibles, [nro de la mochila][posicion en la mochila]
    for i in range(2**len(objetosX)):
        binario = bin(i)  #convertimos el indice decimal en binario
        arregloExhaustivo[i]= binario[2:].rjust(len(objetosX),'0')  #nos quedamos con el valor binario 
                           #y completamos con 0 el resto de posiciones del numero


def peso(combinacion,objetosX): #para una combinacion posible devuelve su peso
    peso = 0
    for i in range(len(objetosX)):
        if (combinacion[i] == "1"):
            peso = objetosX[i][0] + peso
    return peso
        

def valor(combinacion,objetosX): #para una combinacion posible devuelve su valor
    precio = 0
    for i in range(len(objetosX)):
        if(combinacion[i] == "1"):
            precio = objetosX[i][1] + precio
    return precio


def busquedaExahustiva(limiteMaxA, arregloX):
    global mejorCombinacion
    mejorCombinacion= arregloExhaustivo[0]
    for i in range(len(arregloExhaustivo)):
        if (peso(arregloExhaustivo[i],arregloX)<=limiteMaxA and valor(arregloExhaustivo[i],arregloX)>valor(mejorCombinacion,arregloX)):
          mejorCombinacion = arregloExhaustivo[i]
    arregloParaPrint = [0 for _ in range(len(arregloX))]
    for i in range(len(arregloX)):
        if(mejorCombinacion[i] == "1"):
            arregloParaPrint[i] = 1

    print("valor: ", valor(mejorCombinacion,arregloX))
    print("mochila: ", arregloParaPrint)
    print("capacidad: ", peso(mejorCombinacion,arregloX) )
   


def busquedaGreedy(objetosX, limiteMaxX):
    arregloDensidad = [[0 for _ in range(2)]for _ in range(len(objetosX))]#Arreglo de proporciones con el indice en la segunda posicion
    for i in range(len(arregloDensidad)):
        arregloDensidad[i][0] = objetosX[i][1] / objetosX[i][0]
        arregloDensidad[i][1] = i
    #ordenar por densidad de mayor a menor
    arregloDensidad.sort(reverse=True)
    #print(arregloDensidad)
    #llenar (guardar elementos)

    capacidad = 0
    indice = 0
    valor = 0
    mochila = [0 for _ in range(len(objetosX))]
    while(indice<len(objetosX)) :
        indiceObjeto=arregloDensidad[indice][1] #indice del objeto que se agrega
        if(capacidad + objetosX[indiceObjeto][0]<=limiteMaxX):
            capacidad = capacidad + objetosX[indiceObjeto][0]
            valor = valor + objetosX[indiceObjeto][1]
            mochila[indiceObjeto] = 1

        indice += 1

    print("valor: ",valor)
    print("mochila: ", mochila)
    print("capacidad: ", capacidad)    
        
    
    
print("\033[92m--------  PARTE A  --------\033[0m")
print("BUSQUEDA EXAHUSTIVA CON EL ARREGLO DE 10 OBJETOS")

timeInicio = time.perf_counter() #tomamos el tiempo de inicio antes de ejecutar la funcion
cargaArreglo(objetosA)
busquedaExahustiva(limiteMaxA, objetosA)
timeFinal = time.perf_counter()- timeInicio
tiempo_formateado = format(timeFinal, '.10f')


print("Tiempo transcurrido PARA EXAHUSTIVO: ", tiempo_formateado)


print("\nBUSQUEDA GREEDY CON EL ARREGLO DE 10 OBJETOS")

timeInicio = time.perf_counter()
busquedaGreedy(objetosA,limiteMaxA)
timeFinal = time.perf_counter() - timeInicio
tiempo_formateado = format(timeFinal, '.10f')


print("Tiempo transcurrido PARA GREEDEY: ", tiempo_formateado)


print("\033[92m--------  PARTE B  --------\033[0m")

print("BUSQUEDA EXAHUSTIVA CON EL ARREGLO DE 3 OBJETOS")

timeInicio = time.perf_counter()
cargaArreglo(objetosB)
busquedaExahustiva(limiteMaxB, objetosB)
timeFinal = time.perf_counter()- timeInicio
tiempo_formateado = format(timeFinal, '.10f')

print("Tiempo transcurrido PARA EXAHUSTIVO: ", tiempo_formateado)



print("\nBUSQUEDA GREEDY CON EL ARREGLO DE 3 OBJETOS")

timeInicio = time.perf_counter()
busquedaGreedy(objetosB, limiteMaxB)
timeFinal = time.perf_counter() - timeInicio
tiempo_formateado = format(timeFinal, '.10f')

print("Tiempo transcurrido PARA GREEDEY: ", tiempo_formateado)




print("\033[92m--------  PARTE C  --------\033[0m")

print("BUSQUEDA EXAHUSTIVA CON EL ARREGLO DE 15 OBJETOS")

timeInicio = time.perf_counter()
cargaArreglo(objetosExp)
busquedaExahustiva(limiteMaxExp, objetosExp)
timeFinal = time.perf_counter()- timeInicio
tiempo_formateado = format(timeFinal, '.10f')

print("Tiempo transcurrido PARA EXAHUSTIVO: ", tiempo_formateado)



print("\nBUSQUEDA GREEDY CON EL ARREGLO DE 15 OBJETOS")

timeInicio = time.perf_counter()
busquedaGreedy(objetosExp, limiteMaxExp)
timeFinal = time.perf_counter() - timeInicio
tiempo_formateado = format(timeFinal, '.10f')

print("Tiempo transcurrido PARA GREEDEY: ", tiempo_formateado)