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


2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
#Multiplicación de matrices

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

def multiplicar_matrices(matriz_1, matriz_2):                  # Define función para multiplicar matrices
    if len(matriz_1[0]) == len(matriz_2):                      # Verifica que el número de columnas de la primera matriz sea igual al número de filas de la segunda
        matriz_3 = []                                          # Crea lista para la matriz resultante
        for h in range(len(matriz_1)):                         # Recorre las filas de la primera matriz
            fila_3 = []
            for s in range(len(matriz_2[0])):                  # Recorre las columnas de la segunda matriz
                fila_3.append(0)                               # Inicializa cada elemento de la fila resultante en 0

            for s in range(len(matriz_2[0])):
                suma = 0
                for k in range(len(matriz_2)):                 #Recorre las filas de la matriz 2
                    suma += matriz_1[h][k] * matriz_2[k][s]    # Realiza la multiplicación y acumula la suma de los productos
                fila_3[s] = suma                               #Almacena el resultado en la fila resultante

            matriz_3.append(fila_3)                            #Agrega la fila 3 a la matriz 3
    else:
        print()
        print("No es posible multiplicar las matrices, las filas de una matriz deben ser equivalentes a las columnas de la otra")

    return matriz_3

if __name__ == "__main__":
    filas_1 = int(input("Ingrese el número de filas para la matriz 1: "))
    columnas_1 = int(input("Ingrese el número de columnas para la matriz 1: "))
    filas_2 = int(input("Ingrese el número de filas para la matriz 2: "))
    columnas_2 = int(input("Ingrese el número de columnas para la matriz 2: "))
    matriz_1, matriz_2 = generar_matriz(filas_1, filas_2, columnas_1, columnas_2)

    print()

    print("La matriz 1 es: ")
    for fila_1 in matriz_1:                                  #Genera los datos en forma de matriz
        print(fila_1)                                        #Imprime la primera matriz

    print()

    print("La matriz 2 es: ")
    for fila_2 in matriz_2:                                  #Genera los datos en forma de matriz
        print(fila_2)                                        #Imprime la segunda matriz

    matriz_3 = multiplicar_matrices(matriz_1, matriz_2)

    print()
    print("La multiplicación de las matrices es: ")
    for fila_3 in matriz_3:                                  #Genera los datos en forma de matriz
        print(fila_3)                                        #Imprime la matriz resultante
```
3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
#Matriz transpuesta
#Para este punto en vez de usar el paquete random, se definió una función para que el usuario ingrese cada uno de los números
                                                                                               
def generar_matriz(filas, columnas):                     #Define una función que genera una matriz
  matriz = []
  for i in range(filas):                                 #A partir del número de filas dadas
    fila = []                                            #Se crea una lista donde irán los datos ingresados
    for s in range(columnas):                            #A partir del número de columnas dadas
      num = int(input("Ingrese número entero: "))        #Se repite el mensaje el número de veces necesario
      fila.append(num)                                   #Se agregan los números a la lista fila
    matriz.append(fila)                                  #Agrega la lista fila a la  lista de la matriz

  return matriz

if __name__ == "__main__":
  filas = int(input("Ingrese número de filas: "))
  columnas = int(input("Ingrese número de columnas: "))
  matriz_generada = generar_matriz(filas, columnas)
  print()

  print("La matriz generada es: ")
  for fila in matriz_generada:                           #Genera los datos en forma de matriz
    print(fila)                                          #Imprime la matriz

def matriz_transpuesta(matriz):                          #Define la función para la matriz transpuesta
  matriz_transpuesta = []
  for o in range(len(matriz[0])):                        #Recorre las columnas de la matriz
    matriz_transpuesta.append([])                        #Genera la lista de la matriz vacía
    for p in range(len(matriz)):                         #Recorre las filas
      matriz_transpuesta[o].append(matriz[p][o])         #Agrega la matriz con las filas y columnas intercambiadas a la matriz vacía
  return matriz_transpuesta

if __name__ == "__main__":
  matriz_transpuesta = matriz_transpuesta(matriz_generada)
  print()
  print("La matriz transpuesta es: ")

  for h in range(len(matriz_transpuesta)):   
    print(matriz_transpuesta[h])

```
4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
import random

def generar_matriz(filas, columnas):  
    matriz = []

    for i in range(filas):
        fila = []
        for n in range(columnas):
            fila.append(random.randint(1, 100))
        matriz.append(fila)

    return matriz


if __name__ == "__main__":
    filas = int(input("Ingrese el número de filas para la matriz : "))
    columnas = int(input("Ingrese el número de columnas para la matriz : "))
    matriz = generar_matriz(filas, columnas)


    print()

    print("La matriz es: ")                  
    for fila in matriz:
      print(fila)
    print()


def suma_columna(matriz, num_columna):
  suma = 0
  for fila in matriz:
    suma += fila[num_columna]
  return suma


if __name__ == "__main__":
   num_columna = int(input("Ingrese el número de la columna que desea sumar, recordando que la primera columna es cero: "))
   suma_columna = suma_columna(matriz, num_columna)

   print()
   print("La suma de los elementos de la columna " + str(num_columna) + " es: ")
   print(suma_columna)
```
5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
import random

```python
def generar_matriz(filas, columnas):
    matriz = []

    for i in range(filas):
        fila = []
        for n in range(columnas):
            fila.append(random.randint(1, 100))
        matriz.append(fila)

    return matriz


if __name__ == "__main__":
    filas = int(input("Ingrese el número de filas para la matriz : "))
    columnas = int(input("Ingrese el número de columnas para la matriz : "))
    matriz = generar_matriz(filas, columnas)


    print()

    print("La matriz es: ")
    for fila in matriz:
      print(fila)
    print()


def suma_fila(matriz, num_columna):
  suma = 0
  for f in matriz[num_columna]:
    suma += f
  return suma


if __name__ == "__main__":
   num_fila = int(input("Ingrese el número de la fila que desea sumar, recordando que la primera fila es cero: "))
   suma_fila = suma_fila(matriz, num_fila)

   print()
   print("La suma de los elementos de la fila " + str(num_fila) + " es: ")
   print(suma_fila)
```
