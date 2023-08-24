def centinela(lista, buscado):
    posicion = -1
    for i in range(0, len(lista)):
        print(i)
        if (lista[i] == buscado):
            posicion = i
            print(str(buscado)+" está en la posición "+str(posicion))
            break
    return posicion