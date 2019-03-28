# -*- coding: utf-8 -*
'''
 Librerías necesarias para el funcionamiento
 del código
'''

import sys # Permite terminar la ejecución del programa
import os  # Permite limpiar la terminal (CLI)
import platform # Permite conocer el S.O. utilizado

# Se importa las clases
from clases import Cuadrado, Cubo

# Métodos

# Método que permite limpiar la terminal
def limpiar():
    # Permite saber el S.O que se utiliza
    if platform.system() == 'Windows':
        # Limpiar terminal en windows
        os.system('cls')
    else:
        # Limpiar terminal en Linux o Mac
        os.system('clear')

# Método que permite salir de la ejecución del programa.
def terminar():
    # Limpiar terminal antes de salir
    limpiar() 
    
    # Terminar ejecución del programa
    sys.exit()  

# Método que contiene el menu con las opciones que se puede hacer.
def menu_opciones(lado):
    opcion = input('''
    \tIngrese la letra de la operación que desea
    \tValor actual: {}\n
    a). Calcular área cuadrado.
    b). Calcular perimerto cuadrado.
    c). Calcular volumen cubo.
    d). Calcular perimetro cubo.
    e). Atrás.
    f). Salir.
    >'''.format(lado))

    if opcion == 'a' or opcion == 'A':
        limpiar()
        # Se crea el objeto de la clase cuadrado.
        c = Cuadrado(lado)
        # Se imprime el área del cuadrado
        print("\n área: {} del cuadrado".format(c.area_cuadrado()))
    elif opcion == 'b' or opcion == 'B':
        limpiar()
        # Se crea el objeto de la clase cuadrado.
        c = Cuadrado(lado)
        # Se imprime el área del cuadrado
        print("\n perimetro: {} del cuadrado".format(c.perimetro_cuadrado()))
    elif opcion == 'c' or opcion == 'C':
        limpiar()
        # Se crea el objeto de la clase cuadrado.
        c = Cubo(lado)
        # Se imprime el área del cuadrado
        print("\n volumen: {} del cubo".format(c.volumen_cubo()))
    elif opcion == 'd' or opcion == 'D':
        limpiar()
        # Se crea el objeto de la clase cuadrado.
        c = Cubo(lado)
        # Se imprime el área del cuadrado
        print("\n perimetro: {} del cubo".format(c.perimetro_cubo()))
    elif opcion == 'e' or opcion == 'E':
        limpiar()
        iniciar()
    elif opcion == 'f' or opcion == 'F':
        terminar()
    else:
        limpiar()
        print ("Seleccione solo una de las opciones válidas.")
        menu_opciones(lado)

    # Se llama al mismo método hasta que se elija la opción de salir.
    menu_opciones(lado)

# Método que servirá para la ejecución del programa.
def iniciar():
    lado = input("\tOperaciones de cuadrados y cubos\nIngrese el valor de un lado > ")
    while not lado.isdigit():
        print("Ingrese un número")
        lado = input("\nIngrese el valor de un lado > ")
    menu_opciones(int(lado))
    
if __name__ == "__main__":
    iniciar()