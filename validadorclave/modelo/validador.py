from abc import ABC

class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

