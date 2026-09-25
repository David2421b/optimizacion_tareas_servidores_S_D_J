#Hecho Por

#Simon Correa Bravo
#David Hernandez Mejia
#Juan Pablo Tafur

from itertools import permutations, product
import time
import matplotlib.pyplot as plt

class Tarea:
    def __init__(self, id, tiempo, prioridad, dependencias):
        self.id = id
        self.tiempo = tiempo
        self.prioridad = prioridad
        self.dependencias = dependencias

    def __repr__(self):
        return str(self.id)
