from validadorclave.modelo.errores import *
from validadorclave.modelo.validador import Validador


def validar_clave(clave: str, reglas: list):
    global nombre_regla
    for regla in reglas:
        nombre_regla = regla.__class__.__name__
        validador = Validador(regla)
        print(f"\nValidando con regla: {nombre_regla}")

        try:
            validador.es_valida(clave)
            print(f"✅ Clave válida según la regla {nombre_regla}")
        except NoCumpleLongitudMinimaError:
            print(f"❌ [Longitud inválida] en la regla {nombre_regla}")
        except NoTieneLetraMayusculaError:
            print(f"❌ [Falta mayúscula] en la regla {nombre_regla}")
        except NoTieneLetraMinusculaError:
            print(f"❌ [Falta minúscula] en la regla {nombre_regla}")
        except NoTieneNumeroError:
            print(f"❌ [Falta número] en la regla {nombre_regla}")
        except NoTieneCaracterEspecialError:
            print(f"❌ [Falta carácter especial] en la regla {nombre_regla}")
        except NoTienePalabraSecretaError:
            print(f"❌ [Error en formato 'calisto'] en la regla {nombre_regla}")
        except Exception as e:
            print(f"❌ Error desconocido en la regla {nombre_regla}: {e}")