from abc import ABC

class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) >= self.longitud_esperada:
            return True
        else:
            return False

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(ch.isupper() for ch in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(ch.islower() for ch in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(ch.isdigit() for ch in clave)

class ReglaValidacionGanimedes:

    def __init__(self):
        pass

   