#Crear una matriz que vaya agregando valores

matriz = []

Filas= int(input("Indicar el numero de filas: "))
Columnas= int(input("Indicar el numero de columnas: "))

for numero_fila in range(0, Filas):
	matriz.append([])
	for numero_columnas in range(0, Columnas):
		#Arma la matriz
		numero= int(input("Ingrese el numero para matriz [" + str(numero_fila) + "][" + str(numero_columnas) + "]"))
		matriz[numero_fila].append(numero)
		
print("La matriz ingresada es: ")
print(matriz)
		


