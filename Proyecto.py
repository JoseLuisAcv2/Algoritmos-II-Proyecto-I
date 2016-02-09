from math import*
from random import*
#estaOrdenado
def esta_ordenado(a,p,r):
	k = all(a[i]<=a[i+1] for i in range(p,r))
	if k: print("Esta ordenado")
	else: print("Jodete")
##########################################################################################################################################

#Insertion sort
def insertionsort(A,p,r):
	for i in range(p+1,r+1):
		key = A[i]
		j = i-1
		while j>=p and A[j] > key:
			A[j+1] = A[j]
			j-=1
		A[j+1] = key
##########################################################################################################################################

#Heapsort
def maxHeapify(A, i, heapSize,p):
	left  = 2*i + 1-p
	right = 2*i + 2-p
	if left-p < heapSize and A[left] > A[i]:
		largest = left
	else:
		largest = i

	if right-p < heapSize and A[right] > A[largest]:
		largest = right

	if largest != i:
		A[largest], A[i] = A[i], A[largest]
		maxHeapify(A, largest, heapSize,p)
def buildMaxHeap(A, heapSize,p,r):
	for i in range(r-heapSize // 2, p-1, -1):
		maxHeapify(A, i, heapSize,p)
def heapsort(A,p,r):

	heapSize = r-p+1
	buildMaxHeap(A, heapSize,p,r)

	for i in range(p,r):
		A[p], A[p+heapSize -1] = A[p+heapSize - 1], A[p]
		heapSize -= 1
		maxHeapify(A, p, heapSize,p)
##########################################################################################################################################

#Hoare Partition
def Partition(A,p,r,x):
	i = p-1
	j = r+1
	while True:
		while True:
			j-=1
			if A[j]<=x: break
		while True:
			i+=1
			if A[i]>=x: break
		if i < j:
			A[i],A[j] = A[j],A[i]
		else:
			return j
##########################################################################################################################################
 
 #Median of 3
def median_of_three(a,b,c):
	B = [a,b,c]
	B.sort()
	return B[1]
##########################################################################################################################################

#Median-of-Three Quicksort
def median_of_threeQuicksort(A,p,r):
	quicksort_loop(A,p,r)
def quicksort_loop(A,p,r):
	while r-p+1>15:
		m = Partition(A,p,r,median_of_three(A[p],A[r],A[(p+r)//2]))
		if m-p >= r-m:
			quicksort_loop(A,m,r)
			r = m
		else:
			quicksort_loop(A,p,m)
			p = m+1
	#print("Comenzando Insertion Sort...")
	insertionsort(A,p,r)
############################################################################################################################################

#Introsort
def introsort(A,p,r):
	introsort_loop(A,p,r,2*int(log(len(a),2)))
def introsort_loop(A,p,r,limit):
	while r-p+1>15:
		if limit == 0:
			#print("comenzando heapsort para",p,"y",r)
			heapsort(A,p,r)
			return 
		else:
			limit-=1
			m = Partition(A,p,r,median_of_three(A[p],A[r],A[(p+r)//2]))
			introsort_loop(A,m,r,limit)
			r = m
	#print("Comenzando Insertion Sort...")
	insertionsort(A,p,r)
############################################################################################################################################

#3-way-Partitionig Quicksort
def quicksort_3_way_partitioning(A,l,r):
	if r-l+1<=15:insertionsort(A,l,r)
	else:
		i,j,p,q,v = l-1,r,l-1,r,A[r]
		if r>l:
			while True:
				while True:
					i+=1
					if A[i]>=v: break
				while True:
					j-=1
					if A[j]<=v or j==l: break
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

a = [i for i in range(40000)]
quicksort_3_way_partitioning(a,0,len(a)-1)
esta_ordenado(a,0,len(a)-1)