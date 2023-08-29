
#CentinelaW
def centinelaw(lista, buscado):
    posicion = -1
    i=0
    prueba = lista.items()
    prueba2 = list(prueba)

    print(prueba2)
    print(prueba2[0][0])
    
    
    while (i<len(lista)) and (posicion==-1):
        print(i)
        if (lista[i] == buscado):
            posicion = i
        i +=1
    print(str(buscado)+" está en la posición "+str(posicion))
    
    return posicion

def quicksort(listaNumeros, listaNombres, listaHabilidad, primero=0, ultimo=None):
    if ultimo is None:
        ultimo = len(listaNombres) - 1
    
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo
    auxiliar2 = 0

    while izquierda < derecha:
        while listaNombres[izquierda] < listaNombres[pivote] and izquierda <= derecha:
            izquierda += 1
        while listaNombres[derecha] > listaNombres[pivote] and derecha >= izquierda:
            derecha -= 1
        if izquierda < derecha:
            listaNombres[izquierda], listaNombres[derecha] = listaNombres[derecha], listaNombres[izquierda]
            listaNumeros[izquierda], listaNumeros[derecha] = listaNumeros[derecha], listaNumeros[izquierda]
            listaHabilidad[izquierda], listaHabilidad[derecha] = listaHabilidad[derecha], listaHabilidad[izquierda]

    if listaNombres[pivote] < listaNombres[izquierda]:
        listaNombres[izquierda], listaNombres[pivote] = listaNombres[pivote], listaNombres[izquierda]
        listaNumeros[izquierda], listaNumeros[pivote] = listaNumeros[pivote], listaNumeros[izquierda]
        listaHabilidad[izquierda], listaHabilidad[pivote] = listaHabilidad[pivote], listaHabilidad[izquierda]
    
    if primero < izquierda:
        quicksort(listaNumeros, listaNombres, listaHabilidad, primero, izquierda - 1)
    if ultimo > izquierda:
        quicksort(listaNumeros, listaNombres, listaHabilidad, izquierda + 1, ultimo)

    diccionario = {}

    for clave in listaNombres:
        diccionario[clave] = [listaNumeros[auxiliar2], listaHabilidad[auxiliar2]]
        auxiliar2 += 1
    
    return diccionario

#Count
def countsort(listaNumeros, listaNombres, listaHabilidad):
    lista_conteo=[0]*(max(listaNumeros)+1)
    lista_ordenada=[None]*len(listaNumeros)
    lista_ordenadaNm=[None]*len(listaNumeros)
    lista_ordenadaHb=[None]*len(listaNumeros)
    
    for i in listaNumeros:
        lista_conteo[i]+=1
    
    total=0
    for i in range(len(lista_conteo)):
        lista_conteo[i], total = total, total+lista_conteo[i]
    
    for indice in listaNumeros:
        lista_ordenada[lista_conteo[indice]] = indice
        lista_conteo[indice]+=1
        #print(lista_ordenada)

    orden = []
    auxiliar = 0
    auxiliar2 = 0

    for i in range(len(lista_ordenada)):

        for j in range (len(lista_ordenada)):

            if lista_ordenada[i] == listaNumeros[j]:

                orden.append(j)

    for a in orden:

        lista_ordenadaNm[auxiliar] = listaNombres[a]
        lista_ordenadaHb[auxiliar] = listaHabilidad[a]
        auxiliar+=1

    diccionario = {}

    for clave in lista_ordenada:
        diccionario[clave] = [lista_ordenadaNm[auxiliar2], lista_ordenadaHb[auxiliar2]]
        auxiliar2+=1
    
    return diccionario
           


#centinelaw(b, 640)