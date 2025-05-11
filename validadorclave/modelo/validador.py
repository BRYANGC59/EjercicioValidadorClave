from abc import ABC, abstractmethod

from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) > self.longitud_esperada:
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
        caracter_especial = {"@", "_", "#", "$", "%"}
        return any(ch in caracter_especial for ch in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La longitud de la clave no cumple las condiciones")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave no tiene ninguna mayuscula")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave no tiene ninguna minuscula")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave no tiene ningun numero")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave no tiene ningun caracter especial")

        return True


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str)-> bool:
        clave_lower = clave.lower()
        if "calisto" not in clave_lower:
            return False

        inicio = clave_lower.find("calisto")
        fin = inicio + len("calisto")
        subcadena_original = clave[inicio:fin]
        mayusculas = sum(1 for ch in subcadena_original if ch.isupper())

        return 2 <= mayusculas < 7

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La longitud de la clave no cumple las condiciones")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave no tiene ningun numero")
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("La clave no contiene la palabra calisto")

        return True

class Validador:

    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)



