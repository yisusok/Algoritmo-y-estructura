from grafo import Graph


grafo = Graph()
grafo.insert_vertice('Luke Skywalker')
grafo.insert_vertice('Darth Vader')
grafo.insert_vertice('Yoda')
grafo.insert_vertice('Leia Organa')
grafo.insert_vertice('Bobba Fett')
grafo.insert_vertice('C-3PO')
grafo.insert_vertice('Chewbacca')
grafo.insert_vertice('Kylo Ren')
grafo.insert_vertice('Rei')
grafo.insert_vertice('BB-8')
grafo.insert_vertice('Han Solo')
grafo.insert_vertice('R2D2')

grafo.insert_arista('Luke Skywalker', 'Darth Vader', 5)
grafo.insert_arista('Luke Skywalker', 'Yoda', 7)
grafo.insert_arista('Yoda', 'Leia Organa', 3)
grafo.insert_arista('Darth Vader', 'Leia Organa', 4)
grafo.insert_arista('Bobba Fett', 'C-3PO', 0)
grafo.insert_arista('Bobba Fett', 'Chewbacca', 1)
grafo.insert_arista('Kylo Ren', 'Rei', 8)
grafo.insert_arista('Kylo Ren', 'BB-8', 4)
grafo.insert_arista('Chewbacca', 'Han Solo', 9)
grafo.insert_arista('R2D2', 'BB-8', 2)


# Mostrar el grafo
grafo.show_graph()

par, episodios = grafo.episodios_compartidos_max()
print("Los personajes con el máximo de episodios compartidos son:", par, "con", episodios, "episodios.")



aem = grafo.kruskal()
print("Árbol de expansión mínima:", aem)

yoda_en_aem = any("Yoda" in arista for arista in aem)
if yoda_en_aem == True:
    yoda_en_aem="si"
print("¿Yoda está en el árbol de expansión mínima?", yoda_en_aem)



