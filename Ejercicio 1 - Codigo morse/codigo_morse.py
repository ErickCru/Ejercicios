# -*- coding: utf-8 -*
'''
 Librerías necesarias para el funcionamiento
 del código
'''

import sys # Permite terminar la ejecución del programa
import os  # Permite limpiar la terminal (CLI)
import platform # Permite conocer el S.O. utilizado

#Variables globales

'''
Diccionario que contiene el valor de las letras y números
en código morse.
'''
diccionario_codigo_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ' ': '   '
}

'''
Variable que contendrá un menú con las 
opciones que se tiene en el programa.
'''

menu = '''
\t CÓDIGO MORSE
Ingrese la letra de la opción
\na. Convertir texto a código morse
b. Convertir código morse a texto
c. Salir del programa
>'''



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


# Método que permite validar que solo se ingresen caracteres válidos.
def validar_caracteres(texto):
    for caracter_valido in texto:
        if not caracter_valido in diccionario_codigo_morse:
            return True

# Método que permite validar que solo se ingresen códigos válidos.
def validar_codigo_morse(codigo):
    lista = list(diccionario_codigo_morse.values())
    for c in codigo.split(' '):
        if c != '':
            if not c in lista:
                return True
 
# Método que permite realizar la conversión del texto ingresado.
def conversion_morse(texto, opcion):
    # Se convierte el texto a mayúsculas para hacer la comparación
    texto = texto.upper()

    # Se valida que solo haya caracteres válidos.
    if opcion:
        if validar_caracteres(texto):
            limpiar()
            return "\tIngrese solo caracteres válidos\n" + str(diccionario_codigo_morse.keys()) 
    else:
        if validar_codigo_morse(texto):
            limpiar()
            return "\tIngrese solo códigos válidos\n" + str(diccionario_codigo_morse.values())

    # Variable que sirvirá para almacenar la traducción del texto ingresado.
    conversion = ''

    '''
    Se valida la variable opcion, si es True se hará una conversion 
    de texto a código morse y es False se hara lo contrario.
    '''
    if opcion:
        for caracter in texto:
            if caracter == ' ':
                conversion += diccionario_codigo_morse[caracter]
            else:
                conversion += diccionario_codigo_morse[caracter] + ' '
    else:
        for i, codigo in enumerate(texto.split(' ')):
            if codigo == '':
                if i%2:
                    conversion += ' '
            else:
                conversion += list(diccionario_codigo_morse.keys())[list(diccionario_codigo_morse.values()).index(codigo)]

    # Retornamos la conversión
    return conversion


# Método que servirá para la ejecución del programa.
def iniciar():
    #try:
        eleccion = input(menu)
        if eleccion == 'a' or eleccion == 'A':
            limpiar()
            texto = input("\nIngrese el texto > ")
            # Se valida que no se envie texto vacío
            while texto == '':
                print("\tIngrese el texto a convertir")
                texto = input("\nIngrese el texto > ")
            print("\n\tResultado: \n" + conversion_morse(texto, True))
            iniciar()
        elif eleccion == 'b' or eleccion == 'B':
            limpiar()
            texto = input("\nIngrese el Código Morse > ")
            # Se valida que no se envie texto vacío
            while texto == '':
                print("\tIngrese el código a convertir")
                texto = input("\nIngrese el texto > ")
            print("\n\tResultado: \n" + conversion_morse(texto, False)) 
            iniciar()
        elif eleccion == 'c' or eleccion == 'C':
            terminar()
        else:
            limpiar()
            print ("Seleccione solo una de las opciones válidas.")
            iniciar()
    #except:
        print("Terminó la ejecución.")
               

if __name__ == "__main__":
    iniciar()
