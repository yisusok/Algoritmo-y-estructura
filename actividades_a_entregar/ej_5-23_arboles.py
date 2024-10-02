# Deberá resolver los ejercicios 5 y 23 de la guía de arboles del libro y subirlos a git,
# realice la entrega de este trabajo pegando el link del repositorio donde subió los trabajos.

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# class BinaryTree:

#     class __Node:
#         def __init__(self, value, left=None, right=None, other_value=None):
#             self.value = value
#             self.left = left
#             self.right = right
#             self.other_value = other_value if other_value else {'is_hero': False}

#     def __init__(self):
#         self.root = None

#     def insert_node(self, value, is_hero):
#         def __insert(root, value, other_value):
#             if root is None:
#                 return BinaryTree.__Node(value, other_value=other_value)
#             elif value < root.value:
#                 root.left = __insert(root.left, value, other_value)
#             else:
#                 root.right = __insert(root.right, value, other_value)
#             return root

#         self.root = __insert(self.root, value, {'is_hero': is_hero})

#     def inorden_villanos(self):
#         villanos = []

#         def __inorden_villanos(root):
#             if root is not None:
#                 __inorden_villanos(root.left)
#                 if root.other_value.get('is_hero') is False:
#                     villanos.append(root.value)
#                 __inorden_villanos(root.right)

#         if self.root is not None:
#             __inorden_villanos(self.root)
#         villanos.sort()
#         print("Villanos ordenados alfabéticamente:")
#         for v in villanos:
#             print(v)

#     def inorden_superheroes_con_C(self):
#         print("Superhéroes que comienzan con 'C':")

#         def __inorden_superheroes_con_C(root):
#             if root is not None:
#                 __inorden_superheroes_con_C(root.left)
#                 if root.other_value.get('is_hero') is True and root.value.startswith('C'):
#                     print(root.value)
#                 __inorden_superheroes_con_C(root.right)

#         if self.root is not None:
#             __inorden_superheroes_con_C(self.root)

#     def contar_superheroes(self):
#         def __contar_superheroes(root):
#             if root is None:
#                 return 0
#             count = __contar_superheroes(root.left) + __contar_superheroes(root.right)
#             if root.other_value.get('is_hero') is True:
#                 count += 1
#             return count

#         return __contar_superheroes(self.root)

#     def buscar_y_modificar(self, name_incorrecto, name_correcto):
#         nodo = self.search(name_incorrecto)
#         if nodo is not None:
#             print(f"Cambiando {name_incorrecto} a {name_correcto}")
#             nodo.value = name_correcto
#         else:
#             print(f"{name_incorrecto} no fue encontrado.")

#     def inorden_superheroes_descendente(self):
#         superheroes = []

#         def __inorden_superheroes(root):
#             if root is not None:
#                 __inorden_superheroes(root.left)
#                 if root.other_value.get('is_hero') is True:
#                     superheroes.append(root.value)
#                 __inorden_superheroes(root.right)

#         if self.root is not None:
#             __inorden_superheroes(self.root)
#         superheroes.sort(reverse=True)
#         print("Superhéroes en orden descendente:")
#         for s in superheroes:
#             print(s)

#     def generar_bosques(self):
#         heroes_tree = BinaryTree()
#         villanos_tree = BinaryTree()

#         def __insertar_bosques(root):
#             if root is not None:
#                 __insertar_bosques(root.left)
#                 if root.other_value.get('is_hero') is True:
#                     heroes_tree.insert_node(root.value, True)
#                 else:
#                     villanos_tree.insert_node(root.value, False)
#                 __insertar_bosques(root.right)

#         __insertar_bosques(self.root)

#         return heroes_tree, villanos_tree

#     def contar_nodos(self):
#         def __contar_nodos(root):
#             if root is None:
#                 return 0
#             return 1 + __contar_nodos(root.left) + __contar_nodos(root.right)

#         return __contar_nodos(self.root)

#     def inorden(self):
#         def __inorden(root):
#             if root is not None:
#                 __inorden(root.left)
#                 print(root.value)
#                 __inorden(root.right)

#         if self.root is not None:
#             __inorden(self.root)

#     def search(self, value):
#         def __search(root, value):
#             if root is None or root.value == value:
#                 return root
#             elif value < root.value:
#                 return __search(root.left, value)
#             else:
#                 return __search(root.right, value)

#         return __search(self.root, value)


# # Ejemplo de uso
# tree = BinaryTree()

# tree.insert_node("Captain America", True)
# tree.insert_node("Iron Man", True)
# tree.insert_node("Doctor Strange", True)
# tree.insert_node("Thanos", False)
# tree.insert_node("Loki", False)
# tree.insert_node("Captain Marvel", True)
# tree.insert_node("Red Skull", False)

# # Listar villanos
# tree.inorden_villanos()

# # Listar superhéroes que empiezan con 'C'
# tree.inorden_superheroes_con_C()

# # Contar el total de superhéroes
# print(f"Total de superhéroes: {tree.contar_superheroes()}")

# # Buscar y modificar nodo
# tree.buscar_y_modificar("Doctor Strang", "Doctor Strange")

# # Superhéroes en orden descendente
# tree.inorden_superheroes_descendente()

# # Generar bosques de héroes y villanos
# heroes_tree, villanos_tree = tree.generar_bosques()

# print("Nodos en el árbol de héroes:", heroes_tree.contar_nodos())
# print("Nodos en el árbol de villanos:", villanos_tree.contar_nodos())

# # Superhéroes ordenados alfabéticamente
# print("Superhéroes ordenados alfabéticamente:")
# heroes_tree.inorden()

# # Villanos ordenados alfabéticamente
# print("Villanos ordenados alfabéticamente:")
# villanos_tree.inorden()



# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:

class Nodo:
    def __init__(self, criatura, capturada=None, descripcion=""):
        self.criatura = criatura
        self.capturada = capturada
        self.descripcion = descripcion
        self.left = None
        self.right = None

class ArbolBinario:
    def __init__(self):
        self.root = None

    def insert_node(self, criatura, capturada=None, descripcion=""):
        def __insert(root, criatura, capturada, descripcion):
            if root is None:
                return Nodo(criatura, capturada, descripcion)
            if criatura < root.criatura:
                root.left = __insert(root.left, criatura, capturada, descripcion)
            else:
                root.right = __insert(root.right, criatura, capturada, descripcion)
            return root

        self.root = __insert(self.root, criatura, capturada, descripcion)

    # a. Listado inorden de las criaturas y quienes las derrotaron
    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f"Criatura: {root.criatura}, Capturada por: {root.capturada}")
                __inorden(root.right)

        __inorden(self.root)

    # b. Buscar y mostrar la información de una criatura específica
    def buscar_criatura(self, criatura):
        def __buscar(root, criatura):
            if root is None:
                return None
            if root.criatura == criatura:
                return root
            elif criatura < root.criatura:
                return __buscar(root.left, criatura)
            else:
                return __buscar(root.right, criatura)

        nodo = __buscar(self.root, criatura)
        if nodo:
            print(f"Criatura: {nodo.criatura}, Capturada por: {nodo.capturada}, Descripción: {nodo.descripcion}")
        else:
            print(f"La criatura {criatura} no se encontró en el árbol.")

    # d. Determinar los héroes que capturaron más criaturas (sin defaultdict)
    def top_heroes(self, top_n=3):
        capturas = {}

        def __contar_capturas(root):
            if root is not None:
                if root.capturada:
                    if root.capturada in capturas:
                        capturas[root.capturada] += 1
                    else:
                        capturas[root.capturada] = 1
                __contar_capturas(root.left)
                __contar_capturas(root.right)

        __contar_capturas(self.root)
        top_capturas = sorted(capturas.items(), key=lambda x: x[1], reverse=True)[:top_n]

        print(f"Top {top_n} héroes o dioses que capturaron más criaturas:")
        for heroe, cantidad in top_capturas:
            print(f"{heroe}: {cantidad} criaturas")

    # e. Listar las criaturas derrotadas por un héroe o dios específico
    def criaturas_derrotadas_por(self, heroe):
        def __buscar_criaturas(root, heroe, lista):
            if root is not None:
                if root.capturada == heroe:
                    lista.append(root.criatura)
                __buscar_criaturas(root.left, heroe, lista)
                __buscar_criaturas(root.right, heroe, lista)

        lista_criaturas = []
        __buscar_criaturas(self.root, heroe, lista_criaturas)

        if lista_criaturas:
            print(f"Criaturas derrotadas por {heroe}: {', '.join(lista_criaturas)}")
        else:
            print(f"{heroe} no ha derrotado ninguna criatura en el árbol.")

    # f. Listar las criaturas que no han sido derrotadas
    def criaturas_no_derrotadas(self):
        def __buscar_no_derrotadas(root, lista):
            if root is not None:
                if root.capturada is None:
                    lista.append(root.criatura)
                __buscar_no_derrotadas(root.left, lista)
                __buscar_no_derrotadas(root.right, lista)

        lista_no_derrotadas = []
        __buscar_no_derrotadas(self.root, lista_no_derrotadas)

        if lista_no_derrotadas:
            print(f"Criaturas no derrotadas: {', '.join(lista_no_derrotadas)}")
        else:
            print("Todas las criaturas han sido derrotadas.")

# Ejemplo de uso
tree = ArbolBinario()

# Insertar criaturas del árbol
tree.insert_node("Cerbero")
tree.insert_node("León de Nemea", "Heracles", "León invulnerable")
tree.insert_node("Hidra de Lerna", "Heracles", "Serpiente gigante con muchas cabezas")
tree.insert_node("Quimera", "Belerofonte", "Criatura con partes de león, cabra y dragón")
tree.insert_node("Talos", "Medea", "Gigante de bronce de Creta")

# a. Listado inorden de las criaturas y quienes las derrotaron
print("Listado Inorden:")
tree.inorden()

# b. Cargar una breve descripción sobre cada criatura (ya lo estamos haciendo en insert_node)

# c. Mostrar toda la información de la criatura Talos
print("\nInformación de Talos:")
tree.buscar_criatura("Talos")

# d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
print("\nTop 3 héroes o dioses que capturaron más criaturas:")
tree.top_heroes()

# e. Listar las criaturas derrotadas por Heracles
print("\nCriaturas derrotadas por Heracles:")
tree.criaturas_derrotadas_por("Heracles")

# f. Listar las criaturas que no han sido derrotadas
print("\nCriaturas no derrotadas:")
tree.criaturas_no_derrotadas()
