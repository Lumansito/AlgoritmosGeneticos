#arreglo de todos los objetos, [peso][precio]
objetos = [[10,20],[325,40],[600,50],[805,36],[430,25],[1200,64],[770,54],[60,18],[930,46],[353,28]]
limiteMax= 4200




#creamos un arreglo con todas las combinaciones posibles de 10 elementos
def cargaArreglo():
    global arregloExhaustivo
    arregloExhaustivo = [[0 for _ in range(10)]for _ in range(1024)] #arreglo vacio de mochilas posibles, [nro de la mochila][posicion en la mochila]
    for i in range(2**10):
        binario = bin(i)  #convertimos el indice decimal en binario
        arregloExhaustivo[i]= binario[2:].rjust(10,'0')  #nos quedamos con el valor binario 
                           #y completamos con 0 el resto de posiciones del numero


def peso(combinacion):
    peso = 0
    for i in range(10):
        if (combinacion[i] == "1"):
            peso = objetos[i][0] + peso
    return peso
        

def valor(combinacion):
    precio = 0
    for i in range(10):
        if(combinacion[i] == "1"):
            precio = objetos[i][1] + precio
    return precio


def busquedaExahustiva(limiteMax):
    global mejorCombinacion
    mejorCombinacion= arregloExhaustivo[0]
    for i in range(len(arregloExhaustivo)):
        if (peso(arregloExhaustivo[i])<=limiteMax and valor(arregloExhaustivo[i])>valor(mejorCombinacion)):
          mejorCombinacion = arregloExhaustivo[i]
          print('NUEVO MEJOR: ', mejorCombinacion,' VALOR: ',valor(mejorCombinacion),' PESO: ',peso(mejorCombinacion))
    print(mejorCombinacion)
    

def busquedaGreedy():
    arregloDensidad = [[0 for _ in range(2)]for _ in range(10)]#Arreglo de proporciones con el indice en la segunda posicion
    for i in range(len(arregloDensidad)):
        arregloDensidad[i][0] = objetos[i][1] / objetos[i][0]
        arregloDensidad[i][1] = i
    #ordenar por densidad de mayor a menor
    arregloDensidad.sort(reverse=True)
    print(arregloDensidad)
    #llenar (guardar elementos)
    #
    capacidad = 0
    indice = 0
    valor = 0
    mochila = [0 for _ in range(10)]
    while(indice<10) :
        indiceObjeto=arregloDensidad[indice][1] #indice del objeto que se agrega
        if(capacidad + objetos[indiceObjeto][0]<=limiteMax):
            capacidad = capacidad + objetos[indiceObjeto][0]
            valor = valor + objetos[indiceObjeto][1]
            mochila[indiceObjeto] = 1

        indice += 1

    print("valor: ",valor)
    print("mochila: ", mochila)
    print("capacidad: ", capacidad)    
    print("indice: ", indice)
        
    
    


cargaArreglo()
busquedaExahustiva(limiteMax)
busquedaGreedy()
