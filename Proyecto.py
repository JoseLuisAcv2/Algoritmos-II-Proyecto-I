#   Proyecto I Algoritmos II
#	Integrantes: Jose Luis Acevedo #13-10006
#				 Pablo Betancourt  #13-10147
#									Libreria de Algoritmos de ordenamiento


from math import*
from random import*
from sys import*

##########################################################################################################################################

	
#Descripcion: Algoritmo de ordenamiento O(N^2)
#Precondicion: |A| > 0 ^ 0<=p<r<|A|
#Postcondicion: all(A[i]<=A[i+1] for i in range(p,r))
def insertionsort(A,p,r):
	for i in range(p+1,r+1):
		key = A[i]
		j = i-1
		while j>=p and A[j] > key:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = key

##########################################################################################################################################

#Descripcion: Procedimiento que se encarga de mantener la propiedad de max-heap sobre el arreglo
#Precondicion: Para un nodo i, se cumple que los subarboles generados por sus hijos son heaps.
#Postcondicion: El arbol de raiz i es un heap.
def maxHeapify(A, i, heapSize, p):

	left  = 2*i + 1 - p
	right = 2*i + 2 - p

	if left-p < heapSize and A[left] > A[i]:
		largest = left
	else:
		largest = i

	if right-p < heapSize and A[right] > A[largest]:
		largest = right

	if largest != i:
		A[largest], A[i] = A[i], A[largest]
		maxHeapify(A, largest, heapSize, p)
#Descripcion: Procedimiento bottom up que convierte un arreglo en un heap.
#Precondicion: heapSize > 0 ^ |A| > 0 ^ p<r ^ 0<=p<r<|A|
#Postcondicion: El arreglo A es un heap.
def buildMaxHeap(A, heapSize, p, r):
	for i in range(r - heapSize//2, p-1, -1):
		maxHeapify(A, i, heapSize, p)

#Descripcion: Algoritmo de ordenamiento de complejidad O(NlogN) para el mejor y el peor caso
#Precondicion: |A| > 0 ^ 0<=p<r<|A|
#Postcondicion: all(A[i]<=A[i+1] for i in range(p,r))
def heapsort(A,p,r):

	heapSize = r - p + 1
	buildMaxHeap(A, heapSize, p, r)

	for i in range(p,r):
		A[p], A[p + heapSize -1] = A[p + heapSize - 1], A[p]
		heapSize -= 1
		maxHeapify(A, p, heapSize, p)

##########################################################################################################################################


#Nombre: Hoare Partition
#Precondicion: |A| > 0 ^ 0<=p<r<|A| ^ x pertenece a A
#Postcondicion: (Para todo i <= j se cumple que A[i]<=x) ^ (Para todo i>=j se cumple que A[i]>=x)
def Partition(A,p,r,x):
	i = p-1
	j = r+1
	while True:
		while True:
			j-=1
			if A[j] <= x:
				break
		while True:
			i+=1
			if A[i]>=x:
				break
		if i < j:
			A[i],A[j] = A[j],A[i]
		else:
			return j

##########################################################################################################################################
 
 #Descripcion: Funcion que retorna el elemento medio entre 3 dados como parametros.
def median_of_three(a,b,c):
	if a < b and b < c:
		return b
	elif b < a and a < c:
		return a
	else:
		return c

##########################################################################################################################################


#Descripcion: Algoritmo de ordenamiento de complejidad O(NlogN) para caso promedio y O(N^2) para el peor caso.
#Precondicion: |A| > 0 ^ 0<=p<r<|A|
#Postcondicion: all(A[i]<=A[i+1] for i in range(p,r))

def median_of_threeQuicksort(A,p,r):
	quicksort_loop(A,p,r)
	insertionsort(A,p,r)				#Se llama a Insertion sort al final para ordenar los subarreglos de longitud
										#menor o igual a 15, esto se realiza en tiempo lineal.
def quicksort_loop(A,p,r):
	while r-p+1>15:
		m = Partition(A,p,r,median_of_three(A[p],A[r],A[(p+r)//2]))

		if m-p >= r-m:					#Esta condicion garantiza que siempre se escoja el segmento de menor
										#longitud para asegurar que la profundidad del arbol de decisiones sera O(NlogN)
			quicksort_loop(A,m,r)
			r = m
		else:
			quicksort_loop(A,p,m)
			p = m+1

############################################################################################################################################

#Introsort
#Descripcion: Algoritmo de ordenamiento de complejidad O(NlogN) para el mejor y el peor caso.
#Precondicion: |A| > 0 ^ 0<=p<r<|A|
#Postcondicion: El arreglo esta ordenado de forma ascendente.
def introsort(A,p,r):
	introsort_loop(A,p,r,2*int(log(len(A),2)))
	insertionsort(A,p,r)
def introsort_loop(A,p,r,limit):
	while r-p+1>15:
		if limit == 0:				#Se llama a la funcion heapsort cuando la profundidad de la pila de recursion es
									#mayor al doble del piso del logaritmo base 2 de la longitud del arreglo. A partir
									#de ese momento heapsort ordena el resto del subarreglo.
			heapsort(A,p,r)
			return 
		else:
			limit-=1
			m = Partition(A,p,r,median_of_three(A[p],A[r],A[(p+r)//2]))
			introsort_loop(A,m,r,limit)
			r = m

############################################################################################################################################

#3-way-Partitionig Quicksort
#Descripcion: Algoritmo de ordenamiento de complejidad O(NlogN) para el mejor caso y O(N^2) para el peor Caso.
#Precondicion: |A| > 0 ^ 0<=p<r<|A|
#Postcondicion: El arreglo esta ordenado de forma ascendente.
def quicksort_3_way_partitioning(A,l,r):
	setrecursionlimit(len(A) + 100000000) 			#Se aumenta la longitud de la pila de recursion debido a la cantidad
													#de posibles llamadas recursivas a realizar
	if r-l+1<=15:
		insertionsort(A,l,r)
	else:
		#u = randint(l,r)
		#A[u],A[r] = A[r],A[u]
		i,j,p,q,v = l-1,r,l-1,r,A[r]				#A partir de este momento, empieza el procedimiento de la 
		if r>l:										#particion de Hoare con algunas modificaciones, ya que 
			while True:								#al finalizar se garantiza que los elementos iguales al pivote
				while True:							#estaran en el centro, los mayores estrictos a la derecha y
					i+=1 							#los menores estrictos a la izquierda. Esto se logra
					if A[i]>=v: break 				#separando a todos los elementos iguales al pivote a los extremos
				while True: 						#y luego pasandolos al centro.
					j-=1
					if A[j]<=v: break
				if i>=j: break
				A[i],A[j] = A[j],A[i]
				if A[i] == v:
					p+=1
					A[p],A[i] = A[i],A[p]
				if v == A[j]:
					q-=1
					A[j],A[q] = A[q],A[j]
			A[i],A[r] = A[r],A[i]
			j = i-1
			i+=1
			for k in range(l,p):
				A[k],A[j] = A[j],A[k]
				j-=1
			for k in range(r-1,q,-1):
				A[k],A[i] = A[i],A[k]
				i+=1
			quicksort_3_way_partitioning(A,l,j)
			quicksort_3_way_partitioning(A,i,r)
############################################################################################################################################

#Quicksort 2 pivotes
#Descripcion: Algoritmo de ordenamiento de complejidad O(NlogN) para el mejor caso y O(N^2) para el peor Caso.
#Precondicion: |A| > 0 ^ 0<=p<r<|A|
#Postcondicion: El arreglo esta ordenado de forma ascendente.
def quicksort_2p(A,left,right):
	setrecursionlimit(len(A)+100000000)
	if right-left+1<=15:
		insertionsort(A,left,right)
	else:
		#x,y = randint(left,right),randint(left,right)
		#A[left],A[right],A[x],A[y] = A[x],A[y],A[left],A[right]
		if A[left]>A[right]:
			p,q = A[right],A[left]				#Para este Quicksort, el sistema de particion es distinto, puesto
		else:									#que toma 2 pivotes a y b tales que a<=b. El resultado final de la
			q,p = A[right],A[left] 				#particion es que los menores que a quedan a la izquierda, los mayores
		l,g = left+1,right-1 					#o iguales que a y menores o iguales que b quedan entre a y b, y
		k = l 									#los mayores estrictos que b quedan a la derecha.
		while k<=g:
			if A[k] < p:
				A[k],A[l] = A[l],A[k]					
				l+=1
			else:
				if A[k]>=q:
					while A[g]>q and k<g:
						g-=1
					if A[g]>=p:
						A[k],A[g] = A[g],A[k]
					else:
						A[k],A[g] = A[g],A[k]
						A[k],A[l] = A[l],A[k]
						l+=1
					g-=1
			k+=1
		l-=1
		g+=1
		A[left] = A[l]
		A[l] = p
		A[right] = A[g]
		A[g] = q
		quicksort_2p(A,left,l-1)
		quicksort_2p(A,l+1,g-1)
		quicksort_2p(A,g+1,right)