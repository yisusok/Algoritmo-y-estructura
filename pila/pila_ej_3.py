class Stack:
    def __init__(self):
        self.__elements=[]
    
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
# 3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.

pila=Stack()
pila_aux=Stack()

from random import randint
for i in range(10):
    pila.push(randint(1,10))
    

buscado=int(input("ingrese numero a reemplazar: "))
reemplazo=int(input("numero en su lugar: "))



while pila.size()>0:
    data=pila.pop()
    if data==buscado:
        pila_aux.push(reemplazo)
    else:
        pila_aux.push(data)
        
        

while pila_aux.size()>0:
    data_aux=pila_aux.pop()
    pila.push(data_aux)
    
