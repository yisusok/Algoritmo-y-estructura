from pila import Stack
# 7. Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.

pila=Stack()
pila_aux=Stack()
for i in range(3):
    palabra=input("ingrese palabra a pila: ")
    pila.push(palabra)
    
cont=0
while pila.size()>0:
    cont+=1
    data=pila.pop()
    if cont==2:
        data
    else:
        print(data)
        pila_aux.push(data)
        
print()
while pila_aux.size():
    data=pila_aux.pop()
    print(data)
    pila.push(data)