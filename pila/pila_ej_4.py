from pila import Stack
# 4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

pila=Stack()
pila_aux=Stack()

from random import randint
for i in range(5):
    pila.push(randint(1,10))
    
while pila.size()>0:
    data=pila.pop()
    print(data)
    pila_aux.push(data)
    
    
print()
print()
print()

while pila_aux.size()>0:
    data=pila_aux.pop()
    print(data)
    