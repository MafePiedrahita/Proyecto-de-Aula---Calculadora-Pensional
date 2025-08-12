class Error_no_cumple_semanas(Exception):
     """Error cuando las semanas cotizadas no cumplen el minimo"""
     


def calcular_reemplazo_colpensiones(salario_promedio,  reemplazo, semanas, edad, entidad):
    """Calcula la pension mensual """
    if semanas < 1000:
         raise Error_no_cumple_semanas("No cumple con el minimo de semanas cotizadas")
   
    if semanas >= 1000:
         return salario_promedio * reemplazo 


def calcular_pension_privado(saldo_acomulado, factor, edad, entidad ):
     """Calcula la pension mensual"""
     if saldo_acomulado > 0:
          return round (saldo_acomulado / factor, 2)
     else:
          return "No tiene saldo suficiente"
     
       

