from pila import Stack

# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
# a) Contar cuantas especies hay;
# b) Determinar cuantos descubridores distintos hay;
# c) Mostrar todos los dinosaurios que empiecen con T;
# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

pila=Stack()



def contar_especies(pila):
    especies = set()  
    pila_aux = Stack()
    
    while pila.size() > 0:
        dinosaurio = pila.pop()
        especie = dinosaurio["especie"]  
        especies.add(especie)  
        pila_aux.push(dinosaurio)
    
 
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return len(especies)



def contar_descubridores_distintos(pila):
    descubridores = set()
    pila_aux = Stack()
    
    while pila.size() > 0:
        dinosaurio = pila.pop()
        descubridor = dinosaurio["descubridor"]
        descubridores.add(descubridor)
        pila_aux.push(dinosaurio)
    

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return len(descubridores)


def mostrar_dinosaurios_que_empiezan_con_T(pila):
    
    pila_aux = Stack()
    
    while pila.size() > 0:
        dinosaurio = pila.pop()
        dino_con_t = dinosaurio["nombre"]
        if dino_con_t[:1]== "T":
            print(dino_con_t)
        pila_aux.push(dinosaurio)
        
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())


def mostrar_dinos_con_menos_de_275(pila):
    pila_aux = Stack()  
    while pila.size() > 0:
        dinosaurio = pila.pop()
        peso_de_dino = dinosaurio["peso"] 
        peso_numerico = int(peso_de_dino)  
        if peso_numerico < 275:
            print("El dinosaurio", dinosaurio["nombre"], "pesa menos de 275 kg") 
        pila_aux.push(dinosaurio)
        
   
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())


def dejar_en_pila_aparte(pila):
    pila_nueva = Stack()  
    pila_aux = Stack() 

    while pila.size() > 0:
        dinosaurio = pila.pop()
        nombre_dino = dinosaurio["nombre"]
        primera_letra = nombre_dino[0].upper() 
        if primera_letra in ['A', 'Q', 'S']:
            pila_nueva.push(dinosaurio)  
        else:
            pila_aux.push(dinosaurio)  

   
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return pila_nueva



dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000 ,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15 ,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000 ,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000 ,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000 ,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500 ,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

for dinosaurio in dinosaurios:
    pila.push(dinosaurio)
    
    

    
print(contar_especies(pila))

print()
print()

print(contar_descubridores_distintos(pila))

print()
print()

mostrar_dinosaurios_que_empiezan_con_T(pila)

print()
print()

print(mostrar_dinos_con_menos_de_275(pila))

print()
print()

print(pila.size())

print()

pila_e=dejar_en_pila_aparte(pila)

while pila_e.size()>0:
    print(pila_e.pop())


