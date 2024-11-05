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



from cola import Queue

from heap import HeapMax,HeapMin


from pila import Stack


class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.vertices[vertex1].append((vertex2, weight))
        self.vertices[vertex2].append((vertex1, weight))

    def min_spanning_tree(self):
        start_vertex = next(iter(self.vertices))
        visited = set()
        edges = HeapMin()
        total_weight = 0

        for to, weight in self.vertices[start_vertex]:
            edges.add((weight, start_vertex, to))

        visited.add(start_vertex)

        while edges.elements:
            weight, frm, to = edges.remove()
            if to not in visited:
                visited.add(to)
                total_weight += weight
                for next_to, next_weight in self.vertices[to]:
                    if next_to not in visited:
                        edges.add((next_weight, to, next_to))

        return total_weight

    def dijkstra(self, start, end):
        queue = HeapMin()
        queue.add((0, start))
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        previous_vertices = {vertex: None for vertex in self.vertices}

        while queue.elements:
            current_distance, current_vertex = queue.remove()

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    queue.add((distance, neighbor))

        path = []
        current_vertex = end
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]

        return path[::-1], distances[end]


# Creación del grafo
house_graph = Graph()

# Agregar vértices (ambientes)
environments = ["cocina", "comedor", "cochera", "quincho", "baño 1", 
                "baño 2", "habitación 1", "habitación 2", "sala de estar", 
                "terraza", "patio"]

for env in environments:
    house_graph.add_vertex(env)

# Agregar aristas (distancias en metros)
edges = [
    ("cocina", "comedor", 5),
    ("cocina", "cochera", 10),
    ("cocina", "baño 1", 3),
    ("comedor", "quincho", 8),
    ("comedor", "sala de estar", 12),
    ("baño 1", "baño 2", 2),
    ("habitación 1", "sala de estar", 7),
    ("habitación 2", "terraza", 4),
    ("sala de estar", "patio", 6),
    ("quincho", "cochera", 15),
]

for edge in edges:
    house_graph.add_edge(*edge)

# Obtener el árbol de expansión mínima
total_cable_length = house_graph.min_spanning_tree()
print(f"Total de metros de cables necesarios para conectar todos los ambientes: {total_cable_length}")

# Determinar el camino más corto desde habitación 1 hasta sala de estar
shortest_path, cable_length = house_graph.dijkstra("habitación 1", "sala de estar")
print(f"Camino más corto de habitación 1 a sala de estar: {shortest_path} con {cable_length} metros de cable de red.")









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