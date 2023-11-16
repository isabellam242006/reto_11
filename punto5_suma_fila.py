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