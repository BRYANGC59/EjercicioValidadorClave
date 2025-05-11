from abc import ABC, abstractmethod

class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) >= self.longitud_esperada:
            return True
        else:
            return False

    def _contiene_mayuscula(self, clave: str)-> bool:
        return any(ch.isupper() for ch in clave)

    def _contiene_minuscula(self, clave: str)-> bool:
        return any(ch.islower() for ch in clave)

    def _contiene_numero(self, clave: str)-> bool:
        return any(ch.isdigit() for ch in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str)-> bool:
        return any(not ch.isalnum() for ch in clave)

    def es_valida(self):
        pass

class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str)-> bool:
        account = 0
        if "calisto" in clave.lower():
            for ch in clave:
                if ch.isupper:
                    account += 1
            if 1 < account < len(clave):
                return True
            else:
                return False
        else:
            return False

    def es_valida(self):
        pass