from abc import ABC

class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) >= self.longitud_esperada:
            return True
        else:
            return False

