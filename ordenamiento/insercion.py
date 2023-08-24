def insercion(lista):
    for i in range(1, len(lista)+1):
        k=i-1
        while (k>0) and (lista[k]<lista[k-1]):
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k -= 1
        print(lista)
