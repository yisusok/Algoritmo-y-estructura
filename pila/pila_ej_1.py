# 1. Determinar el número de ocurrencias de un determinado elemento en una pila.
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
buscado=int(input("ingrese numero a buscar"))

ac=0


from random import randint

for i in range(5):
    pila.push(randint(1,10))


while pila.size()>0:
    if buscado==pila.on_top():
        ac+=1
    pila.pop()
    
    
print(ac)
    