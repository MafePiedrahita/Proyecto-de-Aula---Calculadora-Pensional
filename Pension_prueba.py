def calcular_reemplazo(salario_promedio,  reemplazo, semanas, edad, entidad):
    """Calcula la pension mensual """
    if semanas > 1000:
         return salario_promedio * reemplazo 
    else:
         return "No cumple con el minimo de semanas cotizadas"
    

def prueba_normal_1():
     """Ejecuta el caso de prueba Normal 1"""
     #Entradas
     sexo = "Hombre"
     edad = 62
     semanas = 1300
     salario_promedio = 3_000_000
     reemplazo = 0.65
     entidad = "Colpensiones"

     #Procesos de Prueba
     pension_mensual = calcular_reemplazo(salario_promedio, reemplazo, semanas, edad, entidad)

     #Verifica la Salida
     pension_esperada = 1_950_000
     if round(pension_mensual,2) == round(pension_esperada):
          print("Prueba Normal 1 exitosa")
     else:
          print("la prueba Normal 1 falló")

prueba_normal_1()










