

def buscarPokemonNumero(listaNumeros, listaNombres, listaHabilidad):
    buscado = int(input("Ingrese número que busca: "))
    diccionario = countsort(listaNumeros, listaNombres, listaHabilidad)

    resultado = diccionario.get(buscado)
    if resultado == None:
        return "El pokemmon no se encuentra en la lista"
    else: 
        return f"El Pokemon {buscado} es de nombre {diccionario[buscado][0]} y es de tipo {diccionario[buscado][1]}"


def buscarPokemonNombre(listaNumeros, listaNombres, listaHabilidad):
    buscado = input("Ingrese nombre que busca: ").capitalize()
    diccionario = quicksort(listaNumeros, listaNombres, listaHabilidad)

    resultado = diccionario.get(buscado)
    if resultado == None:
        return "El pokemmon no se encuentra en la lista"
    else: 
        return f"El Pokemon {buscado} tiene nùmero {diccionario[buscado][0]} y es de tipo {diccionario[buscado][1]}"


def buscarPokemonHabilidad(listaNumeros, listaNombres, listaHabilidad):
    buscado = input("Ingrese habilidad que busca: ").capitalize()
    diccionario = {}

    for i in range(0, len(listaHabilidad)):

        if listaHabilidad[i] == buscado:
            diccionario[listaNumeros[i]] = [listaNombres[i], listaHabilidad[i]]

    print(f"Los pokemones de tipo {buscado} son: {len(diccionario)}")
    return diccionario

def buscarPokemonInicial(listaNumeros, listaNombres, listaHabilidad):
    buscado = input("Ingrese letra que busca: ").capitalize()
    diccionario = {}

    for i in range(0, len(listaNombres)):

        if listaNombres[i][0] == buscado:
            diccionario[listaNumeros[i]] = [listaNombres[i], listaHabilidad[i]]

    return f"Los pokemones que incian con {buscado} son: {diccionario}"


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
    
    return f"La lista pokemon ordenada alfabeticamente es la siguiente: {diccionario}"

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
    
    return f"La lista pokemon ordenada por numero de menor a mayor es la siguiente: {diccionario}"
           

