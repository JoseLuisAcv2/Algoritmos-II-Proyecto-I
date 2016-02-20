from Proyecto import*
def hola(a,n):
	median_of_threeQuicksort(a,0,len(a)-1)
	esta_ordenado(a,0,len(a)-1)
	a = arr
	introsort(a,0,len(a)-1)
	esta_ordenado(a,0,len(a)-1)
	a = arr
	quicksort_3_way_partitioning(a,0,len(a)-1)
	esta_ordenado(a,0,len(a)-1)
	a = arr
	quicksort_2p(a,0,len(a)-1)
	esta_ordenado(a,0,len(a)-1)
k = argv
for i in range(1,len(k)):
	k[i] = int(k[i])
n = k[1]

for i in range(k[3]):
	hola(n)