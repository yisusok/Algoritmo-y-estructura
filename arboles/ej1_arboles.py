# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
# toria– que resuelva las siguientes actividades:

# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.

from arbol_avl import BinaryTree
import random

arbol=BinaryTree()


for i in range(1,10):
    arbol.insert_node(random.randint(1,150))


arbol.preorden()
# arbol.inorden()
# arbol.postorden()
# arbol.by_level()

# print()
# print()
# buscar=int(input("variable a buscar: "))
# print(arbol.search(buscar))

# for i in range(0,3):
#     numero_borrar=int(input("numero a eliminar: "))
#     arbol.delete_node(numero_borrar)

# a=int(input("cargar entero: "))
# contador=arbol.contar(a)

# print(contador)


arbol.update_height(arbol.root)
print("el arbol izquierdo tiene una altura de : ",arbol.height(arbol.root.left),
      "el arbol derecho tiene una altura de : ",arbol.height(arbol.root.right) )


