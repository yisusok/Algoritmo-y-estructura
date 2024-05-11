# 2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.


from cola import Queue
from pila import Stack

cola=Queue()
pila=Stack()

for i in range(10):
    cola.arrive(input("ingrese numero"))


for i in range(cola.size()-1):
    
    pila.push(cola.attention())
    
    
print()
print()
print()


for i in range(pila.size()):
    cola.arrive(pila.pop())
    
    
for i in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()