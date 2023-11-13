# reto_11

1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
#Suma de matrices

import random                                                  # Importar paquete para generar números aleatorios y rellenar la matriz

def generar_matriz(filas_1, filas_2, columnas_1, columnas_2):  #Define la función para crear la matriz teniendo en cuenta filas y columnas
    matriz_1 = []                                              #Genera matriz vacía
    matriz_2 = []

    for i in range(filas_1):                                   #Recorre las filas de la primera matriz
        fila_1 = []              
        for n in range(columnas_1):                            #Recorre las columnas de la primera matriz
            fila_1.append(random.randint(1, 100))              #Agrega números aleatorios a la lista "fila_1" donde irán columnas y filas
        matriz_1.append(fila_1)                                #Agrega la anterior lista a la lista de la matriz


    for o in range(filas_2):                                   #Recorre las filas de la segunda matriz
        fila_2 = []                                   
        for p in range(columnas_2):                            #Recorre las columnas de la segunda matriz
            fila_2.append(random.randint(1, 100))              #Agrega números aleatorios a la lista "fila_2"
        matriz_2.append(fila_2)                                #Agrega la anterior lista a la lista de la matriz

    return matriz_1, matriz_2                                  #Retorna ambas listas


if __name__ == "__main__":
    filas_1 = int(input("Ingrese el número de filas para la matriz 1: "))         
    columnas_1 = int(input("Ingrese el número de columnas para la matriz 1: "))
    filas_2 = int(input("Ingrese el número de filas para la matriz 2: "))
    columnas_2 = int(input("Ingrese el número de columnas para la matriz 2: "))
    matriz_1, matriz_2 = generar_matriz(filas_1, filas_2, columnas_1, columnas_2)  #Genera dos matrices teniendo en cuenta número de filas y columnas ingresadas


    print()

    print("La matriz 1 es: ")
    for fila_1 in matriz_1:                                   #Genera los datos en forma de matriz
      print(fila_1)                                           #Imprime la matriz 1

    print()

    print("La matriz 2 es: ")
    for fila_2 in matriz_2:                                   #Genera los datos en forma de matriz
      print(fila_2)                                           #Imprime matriz 2


def suma_matrices(matriz_1, matriz_2):                                           #Define la función para sumar dos matrices
  if len(matriz_1) == len(matriz_2) and len(matriz_1[0]) == len(matriz_2[0]):    #Se tiene en cuenta que las filas y columnas de ambas matrices deben ser equivalentes
    matriz_3 = []
    for h in range(len(matriz_1)):                                               #Recorre las filas
      fila_3 = []
      for s in range(len(matriz_1[0])):                                          #Recorre las columnas
        fila_3.append(matriz_1[h][s] + matriz_2[h][s])                           #Suma los elementos correspondientes de las dos matrices y los agrega a la fila_3
      matriz_3.append(fila_3)                                                    #Agrega la fila 3 a la matriz 3 
  else:
    print()
    print("No es posible sumar las matrices, deben ser del mismo tamaño")        #Si no se cumple con la condición devuelve un mensaje

  return matriz_3                                                                #Retorna la matriz 3

if __name__ == "__main__":
   matriz_3 = suma_matrices(matriz_1, matriz_2)  

   print()
   print("La suma de las matrices es: ")
   for fila_3 in matriz_3:                                                       #Genera los datos en forma de matriz
    print(fila_3)                                                                #Imprime la matriz 3
```
```python
#Resta de matrices

import random                                                  # Importar paquete para generar números aleatorios y rellenar la matriz

def generar_matriz(filas_1, filas_2, columnas_1, columnas_2):  # Define la función para crear la matriz teniendo en cuenta filas y columnas
    matriz_1 = []                                              # Genera matriz vacía
    matriz_2 = []

    for i in range(filas_1):                                   # Recorre las filas de la primera matriz
        fila_1 = []              
        for n in range(columnas_1):                            # Recorre las columnas de la primera matriz
            fila_1.append(random.randint(1, 100))              # Agrega números aleatorios a la lista "fila_1" donde irán columnas y filas
        matriz_1.append(fila_1)                                # Agrega la anterior lista a la lista de la matriz


    for o in range(filas_2):                                   # Recorre las filas de la segunda matriz
        fila_2 = []                                   
        for p in range(columnas_2):                            # Recorre las columnas de la segunda matriz
            fila_2.append(random.randint(1, 100))              # Agrega números aleatorios a la lista "fila_2"
        matriz_2.append(fila_2)                                # Agrega la anterior lista a la lista de la matriz

    return matriz_1, matriz_2                                  # Retorna ambas listas


if __name__ == "__main__":
    filas_1 = int(input("Ingrese el número de filas para la matriz 1: "))         
    columnas_1 = int(input("Ingrese el número de columnas para la matriz 1: "))
    filas_2 = int(input("Ingrese el número de filas para la matriz 2: "))
    columnas_2 = int(input("Ingrese el número de columnas para la matriz 2: "))
    matriz_1, matriz_2 = generar_matriz(filas_1, filas_2, columnas_1, columnas_2)  # Genera dos matrices teniendo en cuenta número de filas y columnas ingresadas


    print()

    print("La matriz 1 es: ")
    for fila_1 in matriz_1:                                   # Genera los datos en forma de matriz
      print(fila_1)                                           # Imprime la matriz 1

    print()

    print("La matriz 2 es: ")
    for fila_2 in matriz_2:                                   # Genera los datos en forma de matriz
      print(fila_2)                                           # Imprime matriz 2


def resta_matrices(matriz_1, matriz_2):                                            # Define la función para restar dos matrices
    if len(matriz_1) == len(matriz_2) and len(matriz_1[0]) == len(matriz_2[0]):    # Se tiene en cuenta que las filas y columnas de ambas matrices deben ser equivalentes
        matriz_3 = []
        for h in range(len(matriz_1)):                                             # Recorre las filas
            fila_3 = []
            for s in range(len(matriz_1[0])):                                      # Recorre las columnas
                fila_3.append(matriz_1[h][s] - matriz_2[h][s])                     # Resta los elementos correspondientes de las dos matrices y los agrega a la fila_3
            matriz_3.append(fila_3)                                                # Agrega la fila 3 a la matriz 3 
    else:
        print()
        print("No es posible restar las matrices, deben ser del mismo tamaño")     # Si no se cumple con la condición, devuelve un mensaje

    return matriz_3                                                                # Retorna la matriz 3

if __name__ == "__main__":
   matriz_3 = resta_matrices(matriz_1, matriz_2)  

   print()
   print("La resta de las matrices es: ")
   for fila_3 in matriz_3:                                                         # Genera los datos en forma de matriz
    print(fila_3)                                                                  # Imprime la matriz 3
```





