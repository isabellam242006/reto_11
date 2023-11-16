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