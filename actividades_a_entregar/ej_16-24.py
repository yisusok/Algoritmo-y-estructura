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

# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que

# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.

# episodio_v=Stack()
# episodio_vii=Stack()

# inteseccion=Stack()


# episodio_v.push("Luke Skywalker")
# episodio_v.push("Han Solo")
# episodio_v.push("Leia Organa")
# episodio_v.push("Darth Vader")

# episodio_vii.push("Luke Skywalker")
# episodio_vii.push("Rey")
# episodio_vii.push("Finn")
# episodio_vii.push("Kylo Ren")



# while episodio_v.size() > 0 and episodio_vii.size() > 0:
#     episodio_v_element = episodio_v.pop()
#     episodio_vii_element = episodio_vii.pop()
#     if episodio_v_element == episodio_vii_element:
#         inteseccion.push(episodio_v_element)

# while inteseccion.size()>0:
#     print(inteseccion.pop())
    

# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila;

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

# MCU=Stack()
# aux=Stack()
# def agregar_dic():

#     nombre=input("ingrese nombre del personaje: ").upper()
#     peliculas=int(input("ingrese numero de peliculas en las que participó: "))
    

#     chr_lista={
#         'nombre':nombre,
#         'peliculas':peliculas,
#     }
#     return chr_lista

# for i in range(5):
#     MCU.push(agregar_dic())

# while MCU.size() != 0:
#     element = MCU.pop()
#     if element["nombre"] == "ROCKET RACCOON":
#         print("ROCKET RACCOON se encuentra")
#     elif element["nombre"] == "GROOT":
#         print("GROOT se encuentra")
#     aux.push(element)
    
    

# while aux.size() > 0 :
#     MCU.push(aux.pop())
    
# print()
# print()
# print()
# print()
    
# # b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# # car la cantidad de películas en la que aparece;
# while MCU.size() > 0:
#     element = MCU.pop()
#     if element["peliculas"] > 5:
#         print(f"{element["nombre"]} aparecio en {element["peliculas"]}")
#     aux.push(element)
    

# while aux.size() > 0 :
#     MCU.push(aux.pop())


# print()
# print()
# print()
# print()
# # c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

# while MCU.size() > 0:
#     element = MCU.pop()
#     if element["nombre"] == "BLACK WIDOW":
#         print(f"{element["nombre"]} aparecio en {element["peliculas"]}")
#     aux.push(element)    
    
# print()
# print()
# print()
# print()
# # d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
# while MCU.size() > 0:
#     element = MCU.pop()
#     if element["nombre"].startswith(("C", "D", "G")):
#         print(f"{element['nombre']} apareció en {element['peliculas']} películas")
#     aux.push(element)
 