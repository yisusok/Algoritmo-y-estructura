from cola import Queue

# 7. Eliminar el i-ésimo elemento después del frente de la cola.

cola=Queue()
cola_aux=Queue()
for i in range(0,11):
    cola.arrive(i)
    
cont=0
while cola.size()>0:
    cont+=1
    data=cola.attention()
    if cont!=2:
        cola_aux.arrive(data)
        

while cola_aux.size()>0:
    print(cola_aux.attention())