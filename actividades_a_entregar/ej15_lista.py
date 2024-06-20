# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
entrenadores = [
    {
        'nombre': 'Ash',
        'torneos_ganados': 5,
        'batallas_perdidas': 10,
        'batallas_ganadas': 40,
        'pokemons': [
            {'nombre': 'Pikachu', 'nivel': 50, 'tipo': 'Eléctrico', 'subtipo': 'N/A'},
            {'nombre': 'Charizard', 'nivel': 70, 'tipo': 'Fuego', 'subtipo': 'Volador'}
        ]
    },
    {
        'nombre': 'Misty',
        'torneos_ganados': 3,
        'batallas_perdidas': 5,
        'batallas_ganadas': 30,
        'pokemons': [
            {'nombre': 'Starmie', 'nivel': 40, 'tipo': 'Agua', 'subtipo': 'Psíquico'},
            {'nombre': 'Gyarados', 'nivel': 55, 'tipo': 'Agua', 'subtipo': 'Volador'}
        ]
    },
    {
        'nombre': 'Brock',
        'torneos_ganados': 2,
        'batallas_perdidas': 7,
        'batallas_ganadas': 20,
        'pokemons': [
            {'nombre': 'Onix', 'nivel': 45, 'tipo': 'Roca', 'subtipo': 'Tierra'},
            {'nombre': 'Geodude', 'nivel': 30, 'tipo': 'Roca', 'subtipo': 'Tierra'}
        ]
    }
]


# a. obtener la cantidad de Pokémons de un determinado entrenador;

index=input("ingrese entrenador a investigar: ")
for entrenador in entrenadores:
  if entrenador["nombre"]==index:
    print(len(entrenador))

# b. listar los entrenadores que hayan ganado más de tres torneos;
for entrenador in entrenadores:
  if entrenador["torneos_ganados"]>3:
    print(entrenador["nombre"])
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
mas_ganador=0


mas_ganador_nombre=None
for i in entrenadores:
  if entrenador["torneos_ganados"]>mas_ganador:
    mas_ganador=entrenador["torneos_ganados"]
    mas_ganador_nombre=entrenador["nombre"]




pokemon_nivel=0
pokemon_nombre=None
for entrenador in entrenadores:
  if entrenador["nombre"]==mas_ganador_nombre:
    for pokemon in entrenador["pokemons"]:
      if pokemon["nivel"]>pokemon_nivel:
        pokemon_nivel=pokemon["nivel"]
        pokemon_nombre=pokemon["nombre"]
print("el pokemon de mayor nivel de: ",mas_ganador_nombre, "es: ", pokemon_nombre)
      

# d. mostrar todos los datos de un entrenador y sus Pokémos;
for entrenador in entrenadores:
  print(entrenador["nombre"],entrenador["torneos_ganados"],entrenador["batallas_ganadas"],entrenador["batallas_perdidas"])
  print("pokemons")
  for pokemon in entrenador["pokemons"]:
    print(pokemon["nombre"],pokemon["nivel"],pokemon["tipo"],pokemon["subtipo"])
  print()
  print()


# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
for entrenador in entrenadores:
    porcentaje_ganadas = (entrenador["batallas_ganadas"] / (entrenador["batallas_ganadas"] + entrenador["batallas_perdidas"])) * 100
    if porcentaje_ganadas > 79:
        print(entrenador['nombre'], "tiene un porcentaje de batallas ganadas mayor al 79%.")
        
        
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
for entrenador in entrenadores:
    for pokemon in entrenador["pokemons"]:
        if (pokemon["tipo"] == "fuego" and pokemon["subtipo"] == "planta") or \
           (pokemon["tipo"] == "agua" and pokemon["subtipo"] == "volador"):
            print(entrenador["nombre"])


# g. el promedio de nivel de los Pokémons de un determinado entrenador;
index=input("ingrese entrenador a investigar: ")
for entrenador in entrenadores:
    if entrenador["nombre"] == index:
        suma_niveles = 0
        cantidad_pokemons = len(entrenador["pokemons"])
        for pokemon in entrenador["pokemons"]:
            suma_niveles += pokemon["nivel"]
        if cantidad_pokemons > 0:
            promedio_nivel = suma_niveles / cantidad_pokemons
            print("El promedio de nivel de los Pokémon de ",index ,"es: ", promedio_nivel)

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
pokemon_buscar = input("Ingrese el nombre del Pokémon que desea buscar: ")
contador_entrenadores = 0

for entrenador in entrenadores:
    for pokemon in entrenador["pokemons"]:
        if pokemon["nombre"].lower() == pokemon_buscar.lower():
            contador_entrenadores += 1

print(f"{contador_entrenadores} entrenador(es) tienen al Pokémon {pokemon_buscar}.")


# i. mostrar los entrenadores que tienen Pokémons repetidos;

pokemons_vistos = set()
for entrenador in entrenadores:
    for pokemon in entrenador["pokemons"]:
        if pokemon["nombre"] in pokemons_vistos:
          print(entrenador["nombre"], "tiene pokemons repetidos")

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
pokemons_buscar = {"Tyrantrum", "Terrakion", "Wingull"}


for entrenador in entrenadores:
  for pokemon in entrenador["pokemons"]:
    if pokemon["nombre"] in pokemons_buscar:
      print(entrenador["nombre"])
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

nombre_entrenador = input("Ingrese el nombre del entrenador: ")
nombre_pokemon = input("Ingrese el nombre del Pokémon: ")

entrenador_encontrado = None
for entrenador in entrenadores:
    if entrenador["nombre"] == nombre_entrenador:
        entrenador_encontrado = entrenador
        break

if entrenador_encontrado:
    pokemon_encontrado = None
    for pokemon in entrenador_encontrado["pokemons"]:
        if pokemon["nombre"] == nombre_pokemon:
            pokemon_encontrado = pokemon
            
    if pokemon_encontrado:
        print(f"El entrenador {nombre_entrenador} tiene el Pokémon {nombre_pokemon}:")
        print("Datos del entrenador:")
        print(entrenador_encontrado)
        print("Datos del Pokémon:")
        print(pokemon_encontrado)
