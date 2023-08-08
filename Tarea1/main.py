
from lista_persona import lista_persona
from persona import persona


# Crear instancias de personas
persona1 = persona(1, "Juan", 30)
persona2 = persona(2, "María", 25)
persona3 = persona(3, "Carlos", 40)
persona4 = persona(4, "Ana", 22)

# Crear lista y agregar personas ordenadamente
lista_personas = lista_persona()
lista_personas.insertar_ordenado(persona1)
lista_personas.insertar_ordenado(persona2)
lista_personas.insertar_ordenado(persona3)
lista_personas.insertar_ordenado(persona4)

# Imprimir la lista ordenada por edad
lista_personas.imprimir_lista()
