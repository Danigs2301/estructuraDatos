from funciones import *
from menu import *

def main():
    listaNombres = ["Juan","Sara","Messi","Taura","Diosisto"]
    listaNumeros = [12, 13, 23, 9, 2]
    listaHabilidad = ["Fuego", "Agua", "Tierra", "Aire", "Electricidad"]
    print(menu(listaNombres, listaNumeros, listaHabilidad))

    

if __name__ == "__main__":
    main()