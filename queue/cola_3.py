# 3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar
# si es un palíndromo.
from pila import Stack
from cola import Queue




pila=Stack()
pila_aux=Stack()
cola=Queue()
cola_aux=Queue()

palabra=input("ingrese una palabra: ")
palabra.upper()

for letras in palabra:
    cola.arrive(letras)
    
    
ac_o=0
for i in range(cola.size()//2):
    pila.push(cola.attention())
    ac_o+=1

    
if cola.size()>pila.size():
    cola.attention()
    
 
    
ac=0
for i in range(cola.size()):
    if cola.attention()==pila.pop():
        ac+=1
        
if ac_o==ac:
    print("es palindromo")
    
