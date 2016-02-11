# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos cuadraticos
#              que son aplicados sobre listas de elementos de tipo numerico
# Autor: 
# email:

"""
Todos los algoritmos de ordenamiento tienen como
parametro a 'seq' que es un arreglo de elementos numericos
"""
import sys
from random import randint
# Ordenamiento por Insertion
def insertionsort(seq):
    insertionsortaux(seq,0,len(seq)-1)
def insertionsortaux(seq,p,r):
    for i in range(p+1,r+1):
        key = seq[i]
        j = i-1
        while j>=p and seq[j] > key:
            seq[j+1] = seq[j]
            j-=1
        seq[j+1] = key

# Ordenamiento por Bubble sort
def pablosort(seq):
    N = len(seq)
    for i in range(1,N):
        for j in range(0,N):
            if seq[i] < seq[j]:
                seq[i],seq[j] = seq[j],seq[i]
def bubblesort(A):
    n = 0
    N = len(A)
    while n != N:
        k = N-1
        while k != n:
            if A[k-1] > A[k]:
               A[k-1],A[k] = A[k],A[k-1]
            k = k-1
        n = n+1
# Ordenamiento por Selection
def selectionsort(seq):
    N = len(seq)
    for i in range(N):
        pos = i
        for j in range(i,N):
            if seq[pos] > seq[j] : pos = j
        seq[i],seq[pos] = seq[pos],seq[i]

# Ordenamiento por Mezcla
def merge(seq,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [10000000 for i in range(n1+1)]
    R = [10000000 for i in range(n2+1)]
    for i in range(n1):
        L[i] = seq[p+i]
    for i in range(n2):
        R[i] = seq[q+i+1]
    i,j = 0,0
    for k in range(n1+n2):
        if R[i] < L[j]:
            seq[p+k] = R[i]
            i+=1
        else:
            seq[p+k] = L[j]
            j+=1
def mergesort(seq):
    mergesortaux(seq,0,len(seq)-1)
def mergesortaux(seq,p,r):
    if(p<r):
        q = (p+r)//2
        mergesortaux(seq,p,q)
        mergesortaux(seq,q+1,r)
        merge(seq,p,q,r)

# Ordenamiento por Mezcla con corte usando Insercion
def mergesort_cutoff_insert(seq):
    mergesort_cutoff_insertaux(seq,0,len(seq)-1)
def mergesort_cutoff_insertaux(seq,p,r):
    if(r-p) < 100: insertionsortaux(seq,p,r)
    else:
        if(p<r):
            q = (p+r)//2
            mergesort_cutoff_insertaux(seq,p,q)
            mergesort_cutoff_insertaux(seq,q+1,r)
            merge(seq,p,q,r)
# Ordenamiento por monticulo
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
def quicksort_basico(A):
    sys.setrecursionlimit(len(A) +100)
    quicksort(A,0,len(A)-1)
def quicksort(A,p,r):
    if r-p +1<= 15: insertionsortaux(A,p,r)
    else:
	    if p<r:
		q = partition(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1
def quicksort_aleatorio(A):
    sys.setrecursionlimit(len(A) +100)
    quicksort_rand(A,0,len(A)-1)
def quicksort_rand(A,p,r):
    if r-p +1<= 15: insertionsortaux(A,p,r)
    else:
	    if p<r:
		q = partition_aleatorio(A,p,r)
		quicksort_rand(A,p,q-1)
		quicksort_rand(A,q+1,r)
def partition_aleatorio(A,p,r):
    i = randint(p,r)
    A[i],A[r] = A[r],A[i]
    return partition(A,p,r)
