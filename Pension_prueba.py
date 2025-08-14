class Error_no_cumple_semanas(Exception):
    """Error cuando las semanas cotizadas no cumplen el mínimo"""

class Error_invalidez(Exception):
    """Error por invalidez no válida"""

def calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad):
    """Calcula la pensión mensual en Colpensiones"""

    if semanas < 1000:
        raise Error_no_cumple_semanas("No cumple con el mínimo de semanas cotizadas")

    if edad < 50:
        raise Error_invalidez("Error por invalidez no válida")

    return salario_promedio * reemplazo


def calcular_pension_privado(saldo_acumulado, factor, edad, entidad):
    """Calcula la pensión mensual en un fondo privado"""

    if saldo_acumulado > 0:
        return round(saldo_acumulado / factor, 2)
    else:
        return "No tiene saldo suficiente"

       

