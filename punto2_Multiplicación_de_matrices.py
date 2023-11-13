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
