from Proyecto import*
from threading import*
from time import*
from sys import*


#Descripcion: Funcion que verifica si un arreglo A esta ordenado en el intervalo [p,r]

def estaOrdenado(A,p,r):
	if all(A[i]<=A[i+1] for i in range(p,r)):
		print("Esta ordenado")
	else: 
		print("No esta ordenado")

#Descripcion: Dados m y n, la funcion retorna un arreglo de longitud n 
#con ciertas caracteristicas asociadas al valor de m. 


def obtenerArreglo(m,n):
	if m == 1:
		return puntoFlotante(n)
	elif m == 2:
		return ordenado(n)
	elif m == 3:
		return inverso(n)
	elif m == 4:
		return ceroUno(n)
	elif m == 5:
		return mitad(n)
	elif m == 6:
		return casiOrdenado1(n)
	elif m == 7:
		return casiOrdenado2(n)


#Descripcion: Retorna un arreglo de numeros reales entre 0 y 1.

def puntoFlotante(n):
	return [random() for i in range(n)]


#Descripcion: Retorna un arreglo ordenado de forma estrictamente ascendente.

def ordenado(n):
	return [i for i in range(n)]


#Descripcion: Retorna un arreglo ordenado de forma estrictamente descendiente.

def inverso(n):
	return [n-i for i in range(n)]


#Descripcion: Retorna un arreglo con 0's y 1's elegidos de forma aleatoria.

def ceroUno(n):
	return [randint(0,1) for i in range(n)]


#Descripcion: Retorna un arreglo de la forma 1,2,...N/2,N/2,...,2,1.

def mitad(n):
	return [i+1 for i in range(n//2)] + [n//2 - i for i in range(n//2)]


#Descripcion: Dado un conjunto ordenado de elementos de tipo entero, se escogen
#			  al azar 16 pares de elementos que se encuentran separados 8 lugares, entonces se
#			  intercambian los pares.
def casiOrdenado1(n):
	A = ordenado(n)
	B = [False]*n
	for i in range(16):
		while True:
			j = randint(0,n-9)
			if not(B[j]) and not(B[j+8]):
				A[j],A[j+8] = A[j+8],A[j]
				B[j],B[j+8] = True,True
				break
	return A

#Descripcion: Dado un conjunto ordenado de N elementos de tipo entero, se escogen
#			  al azar n/4 pares de elementos que se encuentran separados 4 lugares, entonces se
#             intercambian los pares
def casiOrdenado2(n):
	A = ordenado(n)
	B = [False]*n
	for i in range(n//4):
		while True:
			j = randint(0,n-5)
			if not(B[j]) and not(B[j+4]):
				A[j],A[j+4] = A[j+4],A[j]
				B[j],B[j+4] = True,True
				break
	return A


#Descripcion: Retorna una copia exacta del arreglo que recibe como parametro

def copiarArreglo(A):
	return [A[i] for i in range(len(A))]

def pruebaAlgoritmos(n,m,T):

	print "Obteniendo Arreglo..."
	print
	arr = obtenerArreglo(m,n)							#Se obtiene el arreglo principal para la realizacion de las pruebas.
	
	print "Comenzando Heapsort..."
	a = copiarArreglo(arr)								#Se crea una copia del arreglo principal para cada prueba.

	start_time = time()									#Se toma el tiempo justo antes de empezar el algoritmo de ordenamiento.
	heapsort(a,0,len(a)-1)
	end_time = time() - start_time						#Se toma el tiempo justo despues de que finaliza el algoritmo y
														#Se le resta al tiempo justo antes para poder obtener su tiempo de ejecucion.

	T[0].append(end_time)								#Se guarda el tiempo de ejecucion en un arreglo para su posterior analisis.

	estaOrdenado(a,0,len(a)-1)							#Se verifica que el arreglo haya sido ordenado correctamente.
	print "Tiempo de heapsort:",end_time
	print
	print "Comenzando Median Of Three Quicksort..."
	a = copiarArreglo(arr)
	start_time = time()
	median_of_threeQuicksort(a,0,len(a)-1)
	end_time = time() - start_time
	T[1].append(end_time)
	estaOrdenado(a,0,len(a)-1)
	print "Tiempo de Median Of Three Quicksort:",end_time 
	print
	print "Comenzando Introsort..."
	a = copiarArreglo(arr)
	start_time = time()
	introsort(a,0,len(a)-1)
	end_time = time() - start_time
	T[2].append(end_time)
	estaOrdenado(a,0,len(a)-1)
	print "Tiempo de Introsort:",end_time
	print
	print "Comenzando 3-way Partitioning Quicksort..."
	a = copiarArreglo(arr)
	start_time = time()
	quicksort_3_way_partitioning(a,0,len(a)-1)
	end_time = time() - start_time
	T[3].append(end_time)
	estaOrdenado(a,0,len(a)-1)
	print "Tiempo de 3-way Partitioning Quicksort:",end_time
	print
	print "Comenzando Dual Pivot Quicksort..."
	a = copiarArreglo(arr)
	start_time = time()
	quicksort_2p(a,0,len(a)-1)
	end_time = time() - start_time
	T[4].append(end_time)
	estaOrdenado(a,0,len(a)-1)
	print "Tiempo de Dual Pivot Quicksort:",end_time
	print

#Descripcion: Procedimiento que muestra el tiempo promedio de ejecucion de cada algoritmo de ordenamiento

def mostrarPromedios(P):
	
	print "---------- Promedios ----------"
	print "Heapsort:                     ",round(P[0],4)
	print "Median of Three Quicksort:    ",round(P[1],4)
	print "Introsort:                    ",round(P[2],4)
	print "3-Way Partitioning Quicksort: ",round(P[3],4)
	print "Dual Pivot Quicksort:         ",round(P[4],4)

#Descripcion: Procedimiento que revisa la correctitud de los parametros introducidos por el usuario.

def validarParametros(n,m,l):
	if n<1:
		print "La longitud del arreglo debe ser mayor a 0"
		exit()
	if not(1<=m<8):
		print "El segundo parametro debe ser un numero entre 1 y 7"
		exit()
	if l<3:
		print "Se deben realizar 3 o mas repeticiones"
		exit()

#Descripcion: Funcion principal que llama a todos los procedimientos necesarios bajo los parametros
#			  introducidos por el usuario.

def Main(n,m,l):
	
	validarParametros(n,m,l)

	T = [[] for i in range(5)]
	P = [ 0 for i in range(5)]
	
	for i in range(l):
		print "---------- Prueba",i+1,"----------\n"
		pruebaAlgoritmos(n,m,T)

	for i in range(5):
		P[i] = (sum(T[i][j] for j in range(l)) - max(T[i]) - min(T[i]))/float(l-2)

	mostrarPromedios(P)

k = map(int,argv[1:])								#Se almacenan los parametros de entrada en un arreglo para realizar la conversion
													# de string a entero.

stack_size(67108864)								# Se crea un stack adicional de 64mm.

tr = Thread(target=Main,args=(k[0],k[1],k[2]))		#Se crea un thread que selecciona a la funcion Main y le pasa como
													#parametros los elementos del arreglo k.

tr.start()											#Se inicia el thread para empezar la ejecucion del programa.
