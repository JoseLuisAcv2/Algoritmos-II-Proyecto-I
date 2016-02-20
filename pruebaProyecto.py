from Proyecto import*
from threading import*
from time import*
def obtenerArreglo(m,n):
	if m == 1:
		a = puntoFlotante(n)
	elif m == 2:
		a = ordenado(n)
	elif m == 3:
		a = inverso(n)
	elif m == 4:
		a = ceroUno(n)
	elif m == 5:
		a = mitad(n)
	elif m == 6:
		a = casiOrdenado1(n)
	elif m == 7:
		a = casiOrdenado2(n)
	return a
def puntoFlotante(n):
	A = [random() for i in range(n)]
	return A
def ordenado(n):
	A = [i for i in range(n)]
	return A
def inverso(n):
	A = [n-i for i in range(n)]
	return A
def ceroUno(n):
	A = [randint(0,1) for i in range(n)]
	return A
def mitad(n):
	A = [i+1 for i in range(n//2)] + [n//2 - i for i in range(n//2)]
	return A
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
def hola(n,m):
	print "Obteniendo Arreglo..."
	arr = obtenerArreglo(m,n)
	print "Comenzando Heapsort..."
	a = arr
	start_time = time()
	heapsort(a,0,len(a)-1)
	end_time = time() - start_time
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de heapsort:",end_time
	print
	print "Median Of Three Quicksort"
	a = arr
	start_time = time()
	median_of_threeQuicksort(a,0,len(a)-1)
	end_time = time() - start_time
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de Median Of Three Quicksort:",end_time 
	print
	print "Instrosort"
	a = arr
	start_time = time()
	introsort(a,0,len(a)-1)
	end_time = time() - start_time
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de Introsort:",end_time
	print
	print "3-way Partitioning Quicksort"
	a = arr
	start_time = time()
	quicksort_3_way_partitioning(a,0,len(a)-1)
	end_time = time() - start_time
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de 3-way Partitioning Quicksort:",end_time
	print
	print "Dual Pivot Quicksort"
	a = arr
	start_time = time()
	quicksort_2p(a,0,len(a)-1)
	end_time = time() - start_time
	esta_ordenado(a,0,len(a)-1)
	print "Tiempo de Dual Pivot Quicksort:",end_time
def iniciar(n,m,l):
	for i  in range(l):
		print "---"
		hola(n,m)
k = map(int,argv[1:])
stack_size(67108864)
tr = Thread(target=iniciar,args=(k[0],k[1],k[2]))
tr.start()

