def centinelaw(lista, buscado):
    posicion = -1
    i=0
    while (i<len(lista)) and (posicion==-1):
        print(i)
        if (lista[i] == buscado):
            posicion = i
        i +=1
    print(str(buscado)+" está en la posición "+str(posicion))
    return posicion