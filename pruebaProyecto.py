from Proyecto import*
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
	for i in range(16):
		j = randint(0,n-9)
		A[j],A[j+8] = A[j+8],A[j]
	return A
def casiOrdenado2(n):
	A = ordenado(n)
	for i in range(n//4):
		j = randint(0,n-5)
		A[j],A[j+4] = A[j+4],A[j]
	return A
def hola(n):
	arr = obtenerArreglo(k[1],k[0])
	print("Heapsort")
	a = arr
	heapsort(a,0,len(a)-1)
	esta_ordenado(a,0,len(a)-1)
	print("Median Of Three Quicksort")
	a = arr
	median_of_threeQuicksort(a,0,len(a)-1)
	esta_ordenado(a,0,len(a)-1)
	print("Instrosort")
	a = arr
	introsort(a,0,len(a)-1)
	esta_ordenado(a,0,len(a)-1)
	print("3-way Partitioning Quicksort")
	a = arr
	quicksort_3_way_partitioning(a,0,len(a)-1)
	esta_ordenado(a,0,len(a)-1)
	print("Dual Pivot Quicksort")
	a = arr
	quicksort_2p(a,0,len(a)-1)
	esta_ordenado(a,0,len(a)-1)
k = map(int,argv[1:])
for i  in range(k[2]):
	print "---"
	hola(k[0])

