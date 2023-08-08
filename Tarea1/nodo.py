class nodo:
    def __init__(self, persona= None,siguiente=None,anterior=None):
        self.persona = persona
        self.prev = anterior
        self.next = siguiente
