# 2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden nú-
# meros pares.

class Stack:
    def __init__(self):
        self.__elements=[] #el doble guion bajo oculta la informacion para el usuario para no modificar el codigo fuente
    
    def push(self,element):
        self.__elements.append(element)
        
        
    def pop(self):
        if len(self.__elements)>0:
            return self.__elements.pop()
        else:
            return None
        
        
    def on_top(self):
        return self.__elements[-1]
    
        
    def size(self):
        return len (self.__elements)
    
    
    
pila=Stack()
pila_aux=Stack()

from random import randint

for i in range(7):
    pila.push(randint(1, 10))
    

while pila.size()>0:
    data=pila.pop()
    if data % 2 == 0:
        pila_aux.push(data)


        
while pila_aux.size()>0:
    print(pila_aux.pop())
    pila.push(pila_aux.pop())
    
print()
print()
print()
    
print(pila.size())

        