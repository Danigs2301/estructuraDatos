def seleccion(lista):
    for i in range(0, len(lista)-1):
        minimo = i
        for j in range(i+1, len(lista)):
            if(lista[j] < lista[minimo]):
                minimo= j    
        print(lista)
        lista[i], lista[minimo] = lista[minimo], lista[i]
