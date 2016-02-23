#!/usr/bin/env python
#
# Descripcion: Programa que dibuja puntos en el plano y su mejor ajuste
#     	       a polinomio de orden cuadratico
#
# Autor: Guillermo Palma
# 

import matplotlib.pyplot as plt
import math
import numpy as np

def puntos_cuadraticos(x, y):
    fit = np.polyfit(x,y,2)
    fit_fn = np.poly1d(fit)
    x_new = np.linspace(x[0], x[-1], 50)
    y_new = fit_fn(x_new)
    return x_new, y_new  

# Dibuja puntos en el plano
#
# Parametros
# x: Vector con las coordenadas del eje X
# y: Vector con las coordenadas del eje Y
# color: color de los puntos, los colores disponibles son:
#       'r' rojo, 'b' azul, 'g' verde, 'c' cyan, 'm' magenta, 'y' amarillo y 'k' negro 
# marca: tipo de marca que van a dejar los puntos, algunas opciones son:
#        'o' circulo, '*' estrella, 'x' letra x, '+' suma
# nombre: nombre de la grafica

def dibujar_puntos(x, y, color, marca, nombre):
    x_new, y_new = puntos_cuadraticos(x, y)
    plt.plot(x_new, y_new, color)
    plt.plot(x, y, color+marca, label=nombre)

def mostrar_grafico():
    plt.xlabel("Num. de elementos")
    plt.ylabel("Tiempo (seg)")
    plt.legend(loc=2)

    plt.legend(bbox_to_anchor=(0.05, 0.95), loc=2, borderaxespad=0.)
    plt.show(4)

if __name__ == '__main__':

    x = [1000, 2000, 3000, 4000, 5000]
    y1 = [1.2, 4.2, 8.5, 15.5, 26.2]
    y2 = [1.1, 2.2, 3.3, 3.9, 4.8]
    y3 = [1.4, 5, 9.3, 16.9, 28]

    dibujar_puntos(x, y1, "b", "o", "countingsort")
    dibujar_puntos(x, y2, "r", "*", "quicksort")
    dibujar_puntos(x, y3, "g", "+", "bucketsort")

    mostrar_grafico()
