
from nodo import nodo

class lista_persona:
    def __init__(self):
        self.primero=None

    def insertar_ordenado(self, persona):
        nuevo_nodo = nodo(persona=persona)
        if self.primero is None:
        # Si la lista está vacía, simplemente se inserta la persona como el primero
            self.primero = nuevo_nodo
            return
        # Comparar la edad de la persona con el primero de la lista
        if persona.edad < self.primero.persona.edad:
            nuevo_nodo.next = self.primero
            self.primero.prev = nuevo_nodo
            self.primero = nuevo_nodo
            return
        actual = self.primero
        while actual.next and actual.next.persona.edad < persona.edad:
            actual = actual.next
        # Insertar la persona después del nodo "actual"
        nuevo_nodo.next = actual.next
        if actual.next:
            actual.next.prev = nuevo_nodo
        actual.next = nuevo_nodo
        nuevo_nodo.prev = actual

    def imprimir_lista(self):
        if self.primero is None:
            print("La lista se encuentra vacía")
            return
        
        actual = self.primero
        while actual is not None:
            persona = actual.persona
            print(f"ID: {persona.id}, Nombre: {persona.nombre}, Edad: {persona.edad}")
            actual = actual.next  # Avanzamos hacia las edades menores