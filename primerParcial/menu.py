
from funciones import *

def menu(listaNombres, listaNumeros, listaHabilidad):
    menu = """"
            ----------------------------------------------------BIENVENIDO---------------------------------------------------
            Escoge la opción de tu preferencia:
            1. Mostrar un listado de Pokémons ordenados por el número usando del método de ordenamiento por conteo
            2. Realizar un listado ordenado por nombre utilizando el método de ordenamiento rápido
            3. Mostrar toda la información un Pokémon de un número en especifico
            4. Determinar si existe el Pokémon de un nombre en especifico y mostrar toda su información 
            5. Realizar un listado de todos los Pokémon de una habilidad en especifico y calcular cuantos son
            """
    
    optionsDirectory = {
        1: countsort,
        2: quicksort,
        3: buscarPokemonNumero,
        4: buscarPokemonNombre,
        5: buscarPokemonHabilidad
    }

    while True: 
        print(menu)

        try:
            option = int(input("Ingrese la opción a seleccionar: "))

        except BaseException:
            print("Tienes que ingresar un valor correcto")
            continue

        if option not in optionsDirectory.values():
            break

    selection = optionsDirectory.get(option)

    if selection is None:
        print("Opcion no valida")
        return 
    
    return selection(listaNumeros, listaNombres, listaHabilidad)
        
    
    

