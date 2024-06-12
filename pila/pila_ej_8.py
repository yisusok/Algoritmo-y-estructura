from pila import Stack

# 8. Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
# cartas de baraja española–,resolver las siguientes actividades:
# a. generar las cartas del mazo de forma aleatoria;
# b. separar la pila mazo en cuatro pilas una por cada palo;
# c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

class Carta:
    def __init__(self,numero,palo) :
        self.numero=numero
        self.palo=palo
        
    def getValor(self):
        return self.numero + self.palo
        
        
pila_basto=Stack()
pila_espada=Stack()
pila_oro=Stack()
pila_copa=Stack()
mazo=Stack()

from random import randint

for i in range (1, 13):
    carta=Carta(i,"basto")
    pila_basto.push(carta)
    
for i in range (1, 13):
    carta=Carta(i,"espada")
    pila_espada.push(carta)

for i in range (1, 13):
    carta=Carta(i,"oro")
    pila_oro.push(carta)

for i in range (1, 13):
    carta=Carta(i,"copa")
    pila_copa.push(carta)


for i in range(1,49):
    random=randint(1,4)
    data_basto=pila_basto.pop()
    data_espada=pila_espada.pop()
    data_oro=pila_oro.pop()
    data_copa=pila_copa.pop()
    
    if random==1 and not pila_basto.is_empty():
        mazo.push(data_basto)
    elif random==2 and not pila_espada.is_empty():
        mazo.push(data_espada)
    elif random==3 and not pila_oro.is_empty():
        mazo.push(data_oro)
    elif random==3 and not pila_copa.is_empty():
        mazo.push(data_copa)
        
while mazo.size()>0:
    print(mazo.pop())