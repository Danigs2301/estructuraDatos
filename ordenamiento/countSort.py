def countsort(lista,maximo):
    lista_conteo=[0]*(maximo+1)
    lista_ordenada=[None]*len(lista)
    
    for i in lista:
        lista_conteo[i]+=1
    
    total=0
    for i in range(len(lista_conteo)):
        lista_conteo[i], total = total, total+lista_conteo[i]
    
    for indice in lista:
        lista_ordenada[lista_conteo[indice]] = indice
        lista_conteo[indice]+=1
        print(lista_ordenada)
    return lista_ordenada
    