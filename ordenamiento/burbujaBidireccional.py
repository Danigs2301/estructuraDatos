def burbuja_bidir(lista):
    izquierda = 0
    derecha = len(lista)-1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            if(lista[i] > lista[i+1]):
                control = True
                lista[i], lista[i+1] = lista[i+1], lista[i]
                print(lista)
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            if(lista[j] < lista[j-1]):
                control = True
                lista[j], lista[j-1] = lista[j-1], lista[j]
                print(lista)
        izquierda += 1
