""" Proyecto I Algoritmos II
	Integrantes: Jose Luis Acevedo #13-10006
				 Pablo Betancourt  #13-10147

									Libreria de Algoritmos de ordenamiento
"""

from math import*
from random import*
from sys import*

""" Nombre: estaOrdenado
	Descripcion: Funcion que verifica si un arreglo A esta ordenado en el intervalo [p,r]
"""
def esta_ordenado(a,p,r):
	if all(a[i]<=a[i+1] for i in range(p,r)):
		print("Esta ordenado")
	else: 
		print("No esta ordenado")

##########################################################################################################################################

"""	Nombre: insertionsort
	Descripcion: Algoritmo de ordenamiento O(N²)
"""
def insertionsort(A,p,r):
	for i in range(p+1,r+1):
		key = A[i]
		j = i-1
		while j>=p and A[j] > key:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = key

##########################################################################################################################################

#Heapsort
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

def buildMaxHeap(A, heapSize, p, r):
	for i in range(r - heapSize//2, p-1, -1):
		maxHeapify(A, i, heapSize, p)

def heapsort(A,p,r):

	heapSize = r - p + 1
	buildMaxHeap(A, heapSize, p, r)

	for i in range(p,r):
		A[p], A[p + heapSize -1] = A[p + heapSize - 1], A[p]
		heapSize -= 1
		maxHeapify(A, p, heapSize, p)

##########################################################################################################################################

#Hoare Partition
def Partition(A,p,r,x):
	i = p
	j = r
	while True:
		while True:
			j-=1
			if A[j]<=x:
				break
		while True:
			i+=1
			if A[i]>=x:
				break
		if i < j:
			A[i],A[j] = A[j],A[i]
		else:
			return i

##########################################################################################################################################
 
 #Median of 3
def median_of_three(a,b,c):
	if a < b and b < c:
		return b
	elif b < a and a < c:
		return a
	else:
		return c

##########################################################################################################################################

#Median-of-Three Quicksort
def median_of_threeQuicksort(A,p,r):
	quicksort_loop(A,p,r)
	insertionsort(A,p,r)
def quicksort_loop(A,p,r):
	while r-p+1>15:
		m = Partition(A,p,r,median_of_three(A[p],A[r],A[(p+r)//2]))
		if m-p >= r-m:
			quicksort_loop(A,m,r)
			r = m
		else:
			quicksort_loop(A,p,m)
			p = m+1
############################################################################################################################################

#Introsort
def introsort(A,p,r):
	introsort_loop(A,p,r,2*int(log(len(A),2)))
	insertionsort(A,p,r)
def introsort_loop(A,p,r,limit):
	while r-p+1>15:
		if limit == 0:
			heapsort(A,p,r)
			return 
		else:
			limit-=1
			m = Partition(A,p,r,median_of_three(A[p],A[r],A[(p+r)//2]))
			introsort_loop(A,m,r,limit)
			r = m
############################################################################################################################################

#3-way-Partitionig Quicksort
def quicksort_3_way_partitioning(A,l,r):
	#setrecursionlimit(len(A) + 100000)
	if r-l+1<=15:
		insertionsort(A,l,r)
	else:
		u = randint(l,r)
		A[u],A[r] = A[r],A[u]
		i,j,p,q,v = l-1,r,l-1,r,A[r]
		if r>l:
			while True:
				while True:
					i+=1
					if A[i]>=v: break
				while True:
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
def quicksort_2p(A,left,right):
	#setrecursionlimit(len(A)+100000)
	if right-left+1<=15:
		insertionsort(A,left,right)
	else:
		x,y = randint(left,right),randint(left,right)
		A[left],A[right],A[x],A[y] = A[x],A[y],A[left],A[right]
		if A[left]>A[right]:
			p,q = A[right],A[left]
		else:
			q,p = A[right],A[left]
		l,g = left+1,right-1
		k = l
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
