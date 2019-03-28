# -*- coding: utf-8 -*
'''
 Librerías necesarias para el funcionamiento
 del código
'''

import sys # Permite terminar la ejecución del programa
import os  # Permite limpiar la terminal (CLI)
import platform # Permite conocer el S.O. utilizado
import math # Permite usar el metodo floor 

# Varibles gloabales

# Se crean tuplas con los valores correspondientes a los números romanos validos como invalidos
# Se usan tuplas en vez de listas, debido a que su valor no cambiara durante la ejecución
unidad_romana = ('' , 'I' , 'II' , 'III' , 'IV' , 'V' , 'VI' , 'VII' , 'VIII' , 'IX')
decena_romana =('' , 'X' , 'XX' , 'XXX' , 'XL' , 'L' , 'LX' , 'LXX' , 'LXXX' , 'XC')
centena_romana = ('' , 'C' , 'CC' , 'CCC' , 'CD' , 'D' , 'DC' , 'DCC' , 'DCCC' , 'CM')
valores_romanos_invalidos = ('IIII', 'XXXX', 'CCCC', 'DD', 'VV', 'LL')

# Se crea un diccionario con los valores romanos a decimal
valores_decimales = { 'I' : 1, 'V': 5, 'X':10 , 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


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

# Método que nos permite saber si el número ingresado esta entre 0 y 1000
def validar_num_decimal(num_decimal):
    if num_decimal < 0 or num_decimal > 1000:
        return True
    return False
    
# Método que permite comprobar que los números romanos sean válidos.
def validar_num_romano(num_romano):
    # Ciclo que permite saber si el numero no se encuentra entre los valores permitidos
    for num in num_romano:
        if not num in valores_decimales:
            return 1

    # Ciclo que permite saber si el numero se encuentra entre los valores inválidos
    for num_invalid in valores_romanos_invalidos:
        if num_invalid in num_romano:
            return 2

# Método que se hace carga de la conversión de un número decimal a romano
def decimal_romano(num_decimal):  
    # Se valida que el número ingresado este dentro de los parametros permitidos.
    if validar_num_decimal(num_decimal):
        print("\t\nIngrese un valor mayor a 0 menor igual a 1000")
        num = input("\n Número decimal > ")
        while not num.isdigit() or '.' in num:
            print("Ingrese un número entero")
            num = input("\n Número decimal > ")
        decimal_romano(int(num))
    
    # Comprobamos las unidades, decenas y centenas del número ingresado
    unidades = num_decimal % 10
    decenas = int(math.floor(num_decimal / 10)) % 10
    centenas = int(math.floor(num_decimal / 100))

    # Una vez obtenidos las unidades, decenas y centenas solo se imprime los valores.
    print("\tResultado: \n")
    
    # Variable que tendrá el valor de la conversión
    resultado = 0

    if(num_decimal >= 100): 
        resultado = centena_romana[centenas] + decena_romana[decenas] + unidad_romana[unidades]
    else:
        if(num_decimal >= 10):
            resultado = decena_romana[decenas] + unidad_romana[unidades]
        else:
            resultado = unidad_romana[unidades]

    print("{} es igual a: {}".format(num_decimal, resultado))

    iniciar()

# Método que se hace carga de la conversión de un número romano a decimal
def romano_decimal(num_romano):

    # Se comprueba que el número ingresado sea válido
    if validar_num_romano(num_romano) == 1:
        print("\tSolo se permiten los siguientes numeros: " + str(valores_decimales.keys()))
        romano_decimal(input("\n Número romano > ").upper())
    elif validar_num_romano(num_romano) == 2:
        print("\tValor inválido!\nNo se permite los siguientes valores: " + str(valores_romanos_invalidos))
        romano_decimal(input("\n Número romano > ").upper())

    # Variable que tendrá el valor de la conversión
    resultado = 0
     
    print("\tResultado: \n")

    # En caso de ser solo un número mostramos el resultado
    if len(num_romano) < 1:
        # Con esto, siempre sumamos el primer numero
        valor_anterior = valores_decimales[num_romano]
        print("{} es igual a: {}".format(num_romano, resultado))
        iniciar()
    else:
        valor_anterior = valores_decimales[num_romano[0]]
        for num in num_romano:
            valor_actual = valores_decimales[num]

            if valor_anterior >= valor_actual:
                resultado += valor_actual
            else:
                resultado += valor_actual - (2 * valor_anterior)

            valor_anterior = valor_actual
                
        print("{} es igual a: {}".format(num_romano, resultado))
        iniciar()

# Método que servirá para la ejecución del programa.
def iniciar():

    try:
        opcion = input('''
        \tNúmeros romanos
        Ingrese la letra correspondiente:
        a). Convertir decimal a romano.
        b). Convertir romano a decirmal.
        c) Salir
        >''')

        if opcion == 'a' or opcion == 'A':
            limpiar()
            num = input("\n Número decimal > ")
            while not num.isdigit() or '.' in num:
                print("Ingrese un número entero")
                num = input("\n Número decimal > ")
            decimal_romano(int(num))
        elif opcion == 'b' or opcion == 'B':
            limpiar()
            romano_decimal(input("\n Número romano > ").upper())
        elif opcion == 'c' or opcion == 'C':
            terminar()
        else:
            limpiar()
            print("Elija una de las opciones.")
            iniciar()
    except:
        print("Terminó la ejecución")

if __name__ == "__main__":
    iniciar()