from Proyecto import*
arr = [i for i in range(1000000)]
a = arr
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