# Deberá resolver los ejercicios 11 y 22 de la guía de cola del libro utilizando la clase 
# cola y subirlos a git, realice la entrega de este trabajo pegando el link del repositorio 
# donde subió los trabajos. Y de la guía de heap del libro 
# realice uno de lo siguientes ejercicios  a eleccion (3, 5 o 6) utilizando la clase heap.


# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks


class Personaje:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__(self):
        return f"{self.nombre} de {self.planeta}"

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)

    def find_planets(self, planetas):
        return [str(elem) for elem in self.__elements if elem.planeta in planetas]

    def insert_before(self, new_personaje, existing_name):
        for i in range(len(self.__elements)):
            if self.__elements[i].nombre == existing_name:
                self.__elements.insert(i, new_personaje)
                return
        print(f"{existing_name} no fue encontrado en la cola.")

    def remove_after(self, existing_name):
        for i in range(len(self.__elements)):
            if self.__elements[i].nombre == existing_name and i + 1 < len(self.__elements):
                self.__elements.pop(i + 1)
                return
        print(f"No se pudo encontrar a {existing_name} o no hay un personaje después de él.")

cola = Queue()

cola.arrive(Personaje("Luke Skywalker", "Tatooine"))
cola.arrive(Personaje("Han Solo", "Corellia"))
cola.arrive(Personaje("Yoda", "Dagobah"))
cola.arrive(Personaje("Jar Jar Binks", "Naboo"))
cola.arrive(Personaje("Leia Organa", "Alderaan"))
cola.arrive(Personaje("Chewbacca", "Kashyyyk"))
cola.arrive(Personaje("C-3PO", "Tatooine"))

print("Personajes de Alderaan, Endor y Tatooine:")
personajes_de_planetas = cola.find_planets(["Alderaan", "Endor", "Tatooine"])
for personaje in personajes_de_planetas:
    print(personaje)

luke_planeta = next((p.planeta for p in cola._Queue__elements if p.nombre == "Luke Skywalker"), None)
han_planeta = next((p.planeta for p in cola._Queue__elements if p.nombre == "Han Solo"), None)
print(f"El planeta natal de Luke Skywalker es: {luke_planeta}")
print(f"El planeta natal de Han Solo es: {han_planeta}")

nuevo_personaje = Personaje("Rey", "Jakku")
cola.insert_before(nuevo_personaje, "Yoda")

print("\nCola después de insertar a Rey antes de Yoda:")
for i in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()

cola.remove_after("Jar Jar Binks")

print("\nCola después de eliminar al personaje después de Jar Jar Binks:")
for i in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()





# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
    
class Personaje:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

    def __str__(self):
        return f"{self.nombre_personaje}, {self.nombre_superheroe}, {self.genero}"


class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None

    def find_superhero_name(self, superhero_name):
        for personaje in self.__elements:
            if personaje.nombre_superheroe == superhero_name:
                return personaje.nombre_personaje
        return None

    def show_female_superheroes(self):
        return [p.nombre_superheroe for p in self.__elements if p.genero == 'F']

    def show_male_characters(self):
        return [p.nombre_personaje for p in self.__elements if p.genero == 'M']

    def find_superhero_by_character(self, character_name):
        for personaje in self.__elements:
            if personaje.nombre_personaje == character_name:
                return personaje.nombre_superheroe
        return None

    def show_data_starting_with(self, letter):
        return [str(p) for p in self.__elements if p.nombre_personaje.startswith(letter)]

    def character_exists(self, character_name):
        for personaje in self.__elements:
            if personaje.nombre_personaje == character_name:
                return personaje.nombre_superheroe
        return None


cola = Queue()

cola.arrive(Personaje("Tony Stark", "Iron Man", "M"))
cola.arrive(Personaje("Steve Rogers", "Capitán América", "M"))
cola.arrive(Personaje("Natasha Romanoff", "Black Widow", "F"))
cola.arrive(Personaje("Carol Danvers", "Capitana Marvel", "F"))
cola.arrive(Personaje("Scott Lang", "Ant-Man", "M"))
cola.arrive(Personaje("Thor Odinson", "Thor", "M"))
cola.arrive(Personaje("Wanda Maximoff", "Scarlet Witch", "F"))

personaje_captain_marvel = cola.find_superhero_name("Capitana Marvel")
print(f"El personaje de la superhéroe Capitana Marvel es: {personaje_captain_marvel}")

print("Superhéroes femeninos:")
for superheroe in cola.show_female_superheroes():
    print(superheroe)

print("Personajes masculinos:")
for personaje in cola.show_male_characters():
    print(personaje)

superheroe_scott_lang = cola.find_superhero_by_character("Scott Lang")
print(f"El superhéroe del personaje Scott Lang es: {superheroe_scott_lang}")

print("Personajes cuyos nombres comienzan con 'S':")
for datos in cola.show_data_starting_with("S"):
    print(datos)

superheroe_carol_danvers = cola.character_exists("Carol Danvers")
if superheroe_carol_danvers:
    print(f"Carol Danvers se encuentra en la cola, su superhéroe es: {superheroe_carol_danvers}")
else:
    print("Carol Danvers no se encuentra en la cola.")


# 5. El gran almirante Thrawn es el estratega del imperio galáctico para combatir contra los re-
# beldes, el mismo normalmente se encuentra desbordado de pedidos de sugerencia de cómo
# actuar por los distintos generales, para lo cual nos solicita desarrollar un algoritmo que le per-
# mita atender los pedidos de ayuda de acuerdo a la prioridad de los mismo en base a los siguien-
# te requerimientos:

class Heap:
    def __init__(self):
        self.elements = []

    def add(self, priority, value):
        self.elements.append((priority, value))
        self._float(len(self.elements) - 1)

    def remove(self):
        if len(self.elements) > 0:
            self._interchange(0, len(self.elements) - 1)
            value = self.elements.pop()
            self._sink(0)
            return value
        return None

    def _interchange(self, index1, index2):
        self.elements[index1], self.elements[index2] = self.elements[index2], self.elements[index1]

    def _float(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.elements[index][0] > self.elements[parent][0]:
                self._interchange(index, parent)
                index = parent
            else:
                break

    def _sink(self, index):
        size = len(self.elements)
        while True:
            left = index * 2 + 1
            right = index * 2 + 2
            max_index = index

            if left < size and self.elements[left][0] > self.elements[max_index][0]:
                max_index = left
            if right < size and self.elements[right][0] > self.elements[max_index][0]:
                max_index = right
            if max_index != index:
                self._interchange(index, max_index)
                index = max_index
            else:
                break

    def is_empty(self):
        return len(self.elements) == 0

class Queue:
    def __init__(self):
        self.queue = []
        self.heap = Heap()

    def enqueue(self, general_name, planet, description):
        if general_name == "Gran Inquisidor" or planet == "Lothal" or "Hera Syndulla" in description:
            priority = 3
        elif general_name == "Agente Kallus" or "Destructor Estelar" in description or "AT-AT" in description:
            priority = 2
        else:
            priority = 1
        self.heap.add(priority, (general_name, planet, description))

    def dequeue(self):
        if not self.heap.is_empty():
            return self.heap.remove()
        return None

    def process_requests(self):
        log = []
        while not self.heap.is_empty():
            request = self.dequeue()
            log.append(request)  
            print(f"Processing: {request}")

        return log

    def add_request(self, general_name, planet, description):
        self.enqueue(general_name, planet, description)

queue = Queue()

queue.enqueue("Gran Inquisidor", "Lothal", "Need help with Hera Syndulla")
queue.enqueue("Agente Kallus", "Imperial Star Destroyer", "Requesting reinforcements")
queue.enqueue("General Veers", "Hoth", "Need AT-AT support")
queue.enqueue("General Dodonna", "Yavin", "Strategy meeting")

processed_requests = queue.process_requests()

queue.add_request("General Hux", "Unknown", "Requesting advice on strategy")
