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
