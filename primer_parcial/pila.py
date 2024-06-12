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
    
    
    
# pila=Stack()
# pila_aux=Stack()



# pila.push(4)
# pila.push(87)
# pila.push(31)
# pila.push(10)

# print(pila.__elements)
# print(pila.on_top())
# print(pila.size())
# print()
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())



# para mostrar

# data=pila.pop()
# while pila.size()>0:
#     print(data)
#     pila_aux.push(data)
    
    
# while pila_aux.size()>0:
#     pila.push(pila_aux.pop())
    
    
    
    
#hacer ejercicios desde la pag 83