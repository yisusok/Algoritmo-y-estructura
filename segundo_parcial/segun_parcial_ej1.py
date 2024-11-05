from arbol import BinaryTree

class Pokemon:
    def __init__(self, nombre, numero, tipo):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo 

    def __str__(self):
        return f"Nombre: {self.nombre}, Número: {self.numero}, Tipo(s): {', '.join(self.tipo)}"


arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

pokemons = [
    Pokemon("Bulbasaur", 1, ["planta", "veneno"]),
    Pokemon("Ivysaur", 2, ["planta", "veneno"]),
    Pokemon("Venusaur", 3, ["planta", "veneno"]),
    Pokemon("Charmander", 4, ["fuego"]),
    Pokemon("Charmeleon", 5, ["fuego"]),
    Pokemon("Charizard", 6, ["fuego", "volador"]),
    Pokemon("Squirtle", 7, ["agua"]),
    Pokemon("Wartortle", 8, ["agua"]),
    Pokemon("Blastoise", 9, ["agua"]),
    Pokemon("Pikachu", 25, ["eléctrico"]),
    Pokemon("Raichu", 26, ["eléctrico"]),
    Pokemon("Jolteon", 135, ["eléctrico"]),
    Pokemon("Magnemite", 81, ["eléctrico", "acero"]),
    Pokemon("Magneton", 82, ["eléctrico", "acero"]),
    Pokemon("Steelix", 208, ["acero", "tierra"]),
    Pokemon("Electabuzz", 125, ["eléctrico"]),
    Pokemon("Zapdos", 145, ["eléctrico", "volador"]),
    Pokemon("Flareon", 136, ["fuego"]),
    Pokemon("Vaporeon", 134, ["agua"]),
    Pokemon("Leafeon", 470, ["planta"]),
    Pokemon("Glaceon", 471, ["hielo"]),
    Pokemon("Sylveon", 700, ["hada"]),
    Pokemon("Espeon", 196, ["psíquico"]),
    Pokemon("Umbreon", 197, ["siniestro"]),
    Pokemon("Lycanroc", 745, ["roca"]),
    Pokemon("Tyrantrum", 697, ["roca", "dragón"]),
    Pokemon("Gyarados", 130, ["agua", "volador"]),
    Pokemon("Alakazam", 65, ["psíquico"]),
    Pokemon("Mewtwo", 150, ["psíquico"]),
    Pokemon("Dragonite", 149, ["dragón", "volador"]),
    Pokemon("Lucario", 448, ["lucha", "acero"]),
    Pokemon("Greninja", 658, ["agua", "siniestro"]),
    Pokemon("Decidueye", 724, ["planta", "fantasma"]),
]


for p in pokemons:
    arbol_nombre.insert(p.nombre, p)
    arbol_numero.insert(p.numero, p)
    for tipo in p.tipo:
        arbol_tipo.insert(tipo, p)  


buscar_por_numero = arbol_numero.search(4)
print(buscar_por_numero)
print()
print()
print()

busca_por_nombre = arbol_nombre.search_by_prefix("bul")
for p in busca_por_nombre:
    print(p)


def pokemons_by_type(tipo):
    resultado_tipo = arbol_tipo.search_by_prefix(tipo)
    for p in resultado_tipo:
        print(p.nombre)
        
print()
print()
print()


print("Pokémon de tipo Agua: ", pokemons_by_type("agua"))

print()
print()
print()


print("Pokémons ordenados por número:")
for p in arbol_numero.in_order():
    print(p)
    
print()
print()
print()


print("Pokémons ordenados por nombre:")
for p in arbol_nombre.in_order():
    print(p)

print()
print()
print()

print("Pokémons por nivel (ordenados por nombre):")
for p in arbol_nombre.by_level():
    print(p)

print()
print()
print()

for nombre in ["Jolteon", "Lycanroc", "Tyrantrum"]:
    pokemon = arbol_nombre.search(nombre)
    if pokemon:
        print(pokemon)
    else:
        print(nombre + " no encontrado.")
        
        
print()
print()
print()


tipo_electrico = arbol_tipo.search_by_prefix("eléctrico")
tipo_acero = arbol_tipo.search_by_prefix("acero")

print("Cantidad de Pokémon tipo eléctrico: " , len(tipo_electrico))
print("Cantidad de Pokémon tipo acero: " , len(tipo_acero))
