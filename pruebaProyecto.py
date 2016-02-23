from Proyecto import*
from threading import*
from time import*
from sys import*

""" Nombre: estaOrdenado
	Descripcion: Funcion que verifica si un arreglo A esta ordenado en el intervalo [p,r]
"""
def esta_ordenado(a,p,r):
	if all(a[i]<=a[i+1] for i in range(p,r)):
		print("Esta ordenado")
	else: 
		print("No esta ordenado")

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

def puntoFlotante(n):
	return [random() for i in range(n)]

def ordenado(n):
	return [i for i in range(n)]

def inverso(n):
	return [n-i for i in range(n)]

def ceroUno(n):
	return [randint(0,1) for i in range(n)]

def mitad(n):
	return [i+1 for i in range(n//2)] + [n//2 - i for i in range(n//2)]

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

def copiarArreglo(A):
	return [A[i] for i in range(len(A))]

def pruebaAlgoritmos(n,m,T):

	print "Obteniendo Arreglo...\n"
	arr = obtenerArreglo(m,n)
	
	print "Comenzando Heapsort..."
	a = copiarArreglo(arr)
	start_time = time()
	heapsort(a,0,len(a)-1)
	end_time = time() - start_time
	T[0].append(end_time)
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de heapsort:",end_time
	print
	print "Comenzando Median Of Three Quicksort..."
	a = copiarArreglo(arr)
	start_time = time()
	median_of_threeQuicksort(a,0,len(a)-1)
	end_time = time() - start_time
	T[1].append(end_time)
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de Median Of Three Quicksort:",end_time 
	print
	print "Comenzando Introsort..."
	a = copiarArreglo(arr)
	start_time = time()
	introsort(a,0,len(a)-1)
	end_time = time() - start_time
	T[2].append(end_time)
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de Introsort:",end_time
	print
	print "Comenzando 3-way Partitioning Quicksort..."
	a = copiarArreglo(arr)
	start_time = time()
	quicksort_3_way_partitioning(a,0,len(a)-1)
	end_time = time() - start_time
	T[3].append(end_time)
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de 3-way Partitioning Quicksort:",end_time
	print
	print "Comenzando Dual Pivot Quicksort..."
	a = copiarArreglo(arr)
	start_time = time()
	quicksort_2p(a,0,len(a)-1)
	end_time = time() - start_time
	T[4].append(end_time)
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de Dual Pivot Quicksort:",end_time
	print

def mostrarPromedios(P):
	
	print "---------- Promedios ----------"
	print "Heapsort:                     ",round(P[0],4)
	print "Median of Three Quicksort:    ",round(P[1],4)
	print "Introsort:                    ",round(P[2],4)
	print "3-Way Partitioning Quicksort: ",round(P[3],4)
	print "Dual Pivot Quicksort:         ",round(P[4],4)

def validarParametros(n,m,l):
	if n<1:
		print "La longitud del arreglo debe ser mayor a 0"
		exit()
	if not(1<=m<8):
		print "El segundo parametro debe ser un numero entre 1 y 7"
		exit()
	if l<3:
		print "Se deben realizar mas de 3 repeticiones"
		exit()

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

k = map(int,argv[1:])
stack_size(67108864)
tr = Thread(target=Main,args=(k[0],k[1],k[2]))
tr.start()