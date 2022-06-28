# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
import math


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    csvfile = open('stock.csv')
    data = list (csv.DictReader(csvfile))

    # ESTO NO ME SALIÓ. Me podrían informar cómo resolverlo??
   # cantidad_tornillos = sum(data['tornillos'])
    #print("La cantidad de tornillos en stock es de :", cantidad_tornillos)
    
        
    total = 0
    sumatoria =0
    for row in data:
        # Forma 1
        tornillos_fila = int(row.get('tornillos'))
        total += tornillos_fila
        print("La cantidad de tornillos por fila es:", tornillos_fila, "y el total acumulado es:", total)
        # Forma 2
        cantidad_tornillos= int((row['tornillos']))
        sumatoria += cantidad_tornillos
        print ("La cantidad de tornillos en stock es de :", sumatoria)
    
    csvfile.close()

def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open('propiedades.csv') as archivo:
        datos = list (csv.DictReader(archivo))

    cantidad_filas = len(datos)
    print("Cantidad de filas:", cantidad_filas)
    for i in range(cantidad_filas):
        
        row = datos[i]
        try:
            ambientes = int(row.get('ambientes'))
            print('Fila', i, 'ambientes:',ambientes)
        except:
            print('Fila',i, 'vacia, no informa ambientes')

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
