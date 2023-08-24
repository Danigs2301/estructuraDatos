def burbuja_mejorado(lista):
    i=0
    control=True
    while (i<=len(lista)-2) and control:
        control=False
        for j in range(0, len(lista)-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control=True
                print(lista)
        i +=1
