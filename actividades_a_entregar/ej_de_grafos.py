# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.


from grafo import Graph


grafo = Graph(dirigido=False)

habitaciones = ["cocina", "comedor", "cochera", "quincho", "baño 1", 
                "baño 2", "habitación 1", "habitación 2", "sala de estar", 
                "terraza", "patio"]

for habitacion in habitaciones:
    grafo.insert_vertice(habitacion)

grafo.insert_arista("cocina", "comedor", 5)
grafo.insert_arista("cocina", "baño 1", 8)
grafo.insert_arista("cocina", "habitacion 1", 12)
grafo.insert_arista("comedor", "sala de estar", 7)
grafo.insert_arista("comedor", "quincho", 15)
grafo.insert_arista("comedor", "baño 2", 6)
grafo.insert_arista("cochera", "quincho", 10)
grafo.insert_arista("cochera", "patio", 20)
grafo.insert_arista("cochera", "terraza", 25)
grafo.insert_arista("baño 1", "habitacion 1", 3)
grafo.insert_arista("baño 1", "habitacion 2", 10)
grafo.insert_arista("baño 1", "sala de estar", 9)
grafo.insert_arista("quincho", "terraza", 4)
grafo.insert_arista("terraza", "patio", 8)
grafo.insert_arista("patio", "sala de estar", 18)
grafo.insert_arista("habitacion 1", "habitacion 2", 5)
grafo.insert_arista("habitacion 2", "sala de estar", 10)

arbol_minimo = grafo.kruskal("cocina")
print("Árbol de expansión mínima:")
print("Contenido de arbol_minimo:", arbol_minimo)




camino_corto = grafo.dijkstra("Habitación 1")
print("Camino más corto desde Habitación 1 hasta Sala de Estar:")
while camino_corto.size() > 0:
    nodo = camino_corto.pop()
    print(nodo[1][0])
    if nodo[1][0] == "sala de estar":
        break

# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.



maravillas_grafo = Graph(dirigido=False)


maravillas_arquitectonicas = [
    ("Chichen Itza", ["Mexico"], "arquitectonica"),
    ("Cristo Redentor", ["Brasil"], "arquitectonica"),
    ("Coliseo Romano", ["Italia"], "arquitectonica"),
    ("Machu Picchu", ["Peru"], "arquitectonica")
]

maravillas_naturales = [
    ("Gran Barrera de Coral", ["Australia"], "natural"),
    ("Monte Everest", ["Nepal", "China"], "natural"),
    ("Selva Amazónica", ["Brasil"], "natural")
]


for maravilla in maravillas_arquitectonicas:
    maravillas_grafo.insert_vertice(maravilla[0])


for maravilla in maravillas_naturales:
    maravillas_grafo.insert_vertice(maravilla[0])


maravillas_grafo.insert_arista("Chichen Itza", "Cristo Redentor", 12000)
maravillas_grafo.insert_arista("Chichen Itza", "Coliseo Romano", 10000)
maravillas_grafo.insert_arista("Chichen Itza", "Machu Picchu", 3500)
maravillas_grafo.insert_arista("Cristo Redentor", "Coliseo Romano", 15000)
maravillas_grafo.insert_arista("Cristo Redentor", "Machu Picchu", 5000)
maravillas_grafo.insert_arista("Coliseo Romano", "Machu Picchu", 11000)


maravillas_grafo.insert_arista("Gran Barrera de Coral", "Monte Everest", 1500)
maravillas_grafo.insert_arista("Gran Barrera de Coral", "Selva Amazónica", 2000)
maravillas_grafo.insert_arista("Monte Everest", "Selva Amazónica", 5000)


arbol_minimo_arquitectonicas = maravillas_grafo.kruskal("Chichen Itza")
print("Árbol de expansión mínima para maravillas arquitectónicas:")
print(arbol_minimo_arquitectonicas)


arbol_minimo_naturales = maravillas_grafo.kruskal("Gran Barrera de Coral")
print("Árbol de expansión mínima para maravillas naturales:")
print(arbol_minimo_naturales)


paises_arquitectonicos = set()
paises_naturales = set()

for maravilla, paises, tipo in maravillas_arquitectonicas:
    paises_arquitectonicos.update(paises)

for maravilla, paises, tipo in maravillas_naturales:
    paises_naturales.update(paises)

paises_comunes = paises_arquitectonicos.intersection(paises_naturales)
print("Países con maravillas arquitectónicas y naturales:", paises_comunes)

paises_multiples = {}

for maravilla, paises, tipo in maravillas_arquitectonicas:
    for pais in paises:
        if pais in paises_multiples:
            paises_multiples[pais] += 1
        else:
            paises_multiples[pais] = 1

for maravilla, paises, tipo in maravillas_naturales:
    for pais in paises:
        if pais in paises_multiples:
            paises_multiples[pais] += 1
        else:
            paises_multiples[pais] = 1

paises_con_multiples_maravillas = {pais: count for pais, count in paises_multiples.items() if count > 1}
print("Países con más de una maravilla:", paises_con_multiples_maravillas)
