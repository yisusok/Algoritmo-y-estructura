from cola import Queue
from random import randint
# Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ningu-
# na estructura auxiliar.

cola=Queue()
buscado=int(input("ingrese numero a buscar: "))
cont=0


for i in range(1,31):
    cola.arrive(randint(1,10))
    
while cola.size()>0:
    if buscado==cola.attention():
        cont+=1
        
        
        
print("El numero " , buscado , " aparecio " , cont , "veces")