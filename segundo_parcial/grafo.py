from cola import Queue
from heap import HeapMin
from pila import Stack

class Graph:
    def __init__(self, dirigido=False):
        self.elements = []
        self.dirigido = dirigido

    def show_graph(self):
        print()
        print("nodos")
        for index, nodo in enumerate(self.elements):
            print(nodo['value'])
            print(f"    aristas")
            for second_index, second_element in enumerate(nodo['aristas']):
                print(f'    destino {second_element['value']} peso: {second_element['peso']}')
        print()

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index

    def search_arista(self, vertice_value, value):
        pos_origen = self.search(vertice_value)
        if pos_origen is not None:
            for index, element in enumerate(self.elements[pos_origen]['aristas']):
                if element['value'] == value:
                    return pos_origen, index

    def insert_vertice(self, value, other_value=None):
        nodo = {
        'value': value,
        'aristas': [],
        'visitado': False,
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            # print(origen, destino)
            arista = {
                'value': destino,
                'peso': peso
            }
            self.elements[pos_origen]['aristas'].append(arista)
            if not self.dirigido:
                arista = {
                    'value': origen,
                    'peso': peso
                }
                self.elements[pos_destino]['aristas'].append(arista)

    
    def delete_arista(self, origen, destino):
        result = self.search_arista(origen, destino)
        if result:
            pos_vertice, pos_arista = result
            value = self.elements[pos_vertice]['aristas'].pop(pos_arista)
            if not self.dirigido:
                result = self.search_arista(destino, origen)
                if result:
                    pos_vertice, pos_arista = result
                    self.elements[pos_vertice]['aristas'].pop(pos_arista)
            return value
    
    def delete_vertice(self, value):
        pos_vertice = self.search(value)
        if pos_vertice is not None:
            delete_value = self.elements.pop(pos_vertice)
            for nodo in self.elements:
                self.delete_arista(nodo['value'], value)
            return delete_value
    
    def mark_as_not_visited(self):
        for nodo in self.elements:
            nodo['visitado'] = False

    def deep_show(self, origin):
        def __deep_show(graph, origin):
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    print(graph.elements[pos_vertice]['value'])
                    adyacentes = graph.elements[pos_vertice]['aristas']
                    for adyacente in adyacentes:
                        __deep_show(graph, adyacente['value'])
        
        self.mark_as_not_visited()
        __deep_show(self, origin)

    def amplitude_show(self, origin):
        self.mark_as_not_visited()
        cola = Queue()
        pos_vertice = self.search(origin)
        if pos_vertice is not None:
            if not self.elements[pos_vertice]['visitado']:
                cola.arrive(self.elements[pos_vertice])
                while cola.size() > 0:
                    nodo = cola.attention()
                    nodo['visitado'] = True
                    print(nodo['value'])
                    adyacentes = nodo['aristas']
                    for adyacente in adyacentes:
                        pos_adyaecnte = self.search(adyacente['value'])
                        if not self.elements[pos_adyaecnte]['visitado']:
                            cola.arrive(self.elements[pos_adyaecnte])
    
    def exist_path(self, origen, destino):
        def __exist_path(graph, origin, destino):
            result = False
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    if graph.elements[pos_vertice]['value'] == destino:
                        return True
                    else:
                        adyacentes = graph.elements[pos_vertice]['aristas']
                        for adyacente in adyacentes:
                            result = __exist_path(graph, adyacente['value'], destino)
                            if result:
                                break
            return result
        
        self.mark_as_not_visited()
        result = __exist_path(self, origen, destino)
        return result

    def dijkstra(self, origen):
        from math import inf
        no_visitados = HeapMin()
        camino = Stack()
        for nodo in self.elements:
            distancia = 0 if nodo['value'] == origen else inf
            no_visitados.arrive([nodo['value'], nodo, None], distancia)
        while len(no_visitados.elements) > 0:
            node = no_visitados.atention()
            costo_nodo_actual = node[0]
            camino.push(node)
            adjacentes = node[1][1]['aristas']
            # print(costo_nodo_actual, adjacentes)
            for adjacente in adjacentes:
                pos = no_visitados.search(adjacente['value'])
                if pos is not None:
                    if costo_nodo_actual + adjacente['peso'] < no_visitados.elements[pos][0]:
                        no_visitados.elements[pos][1][2] = node[1][0]
                        no_visitados.change_proirity(pos, costo_nodo_actual + adjacente['peso'])
        return camino

    def kruskal(self):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                if buscado in arbol:
                    return index
            return None

        bosque = []
        aristas = []

        for nodo in self.elements:
            for adyacente in nodo['aristas']:
                aristas.append((adyacente['peso'], nodo['value'], adyacente['value']))

        aristas.sort(key=lambda x: x[0])

        for nodo in self.elements:
            bosque.append(nodo['value'])

        aem = []
        for arista in aristas:
            peso, origen, destino = arista
            origen_index = buscar_en_bosque(bosque, origen)
            destino_index = buscar_en_bosque(bosque, destino)

            if origen_index != destino_index:
                aem.append((origen, destino, peso))

                nuevo_arbol = f'{bosque[origen_index]}-{bosque[destino_index]}'
                bosque[origen_index] = nuevo_arbol  
                bosque.pop(destino_index) 

        return aem

    
    def episodios_compartidos_max(self):
        max_episodios = 0
        par = ()
        
        for var1 in self.elements:
            for var2 in var1['aristas']:
                weight = var2['peso']
                if weight > max_episodios:
                    max_episodios = weight
                    par = (var1['value'], var2['value'])
        
        return par, max_episodios
    
