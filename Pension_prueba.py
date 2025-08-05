def calcular_reemplazo_colpensiones(salario_promedio,  reemplazo, semanas, edad, entidad):
    """Calcula la pension mensual """
    if semanas >= 1000:
         return salario_promedio * reemplazo 
    else:
         return "No cumple con el minimo de semanas cotizadas"
    
def calcular_pension_privado(saldo_acomulado, factor, edad, entidad ):
     """Calcula la pension mensual"""
     if saldo_acomulado > 0:
          return round (saldo_acomulado / factor, 2)
     else:
          return "No tiene saldo suficiente"
     
       

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
     pension_mensual = calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)

     #Verifica la Salida
     pension_esperada = 1_950_000
     if round(pension_mensual,2) == round(pension_esperada):
          print("Prueba Normal 1 exitosa")
     else:
          print("la prueba Normal 1 falló")

def prueba_extraordinario_1():
     """Ejecuta el caso de prueba Extraordinario 1"""
     #Entradas
     sexo = "Mujer"
     edad = 57
     semanas = 1000
     salario_promedio = 2_000_000
     reemplazo = 0.65
     entidad = "Colpensiones"

     #Procesos de Preuba
     pension_mensual = calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)

     #Verifica la Salida
     pension_esperada = 1_300_000
     if round(pension_mensual,2) == round(pension_esperada):
          print("Prueba Extraordinario 1 exitosa")
     else:
          print("la prueba Extraordinario 1 falló")

def prueba_ideal_1():
     """Ejecuta el caso de prueba Ideal 1"""
     #Entradas
     sexo = "Hombre"
     edad = 62
     semanas = 1800
     salario_promedio = 4_000_000
     reemplazo = 0.80
     entidad = "Colpensiones"

     #Procesos de Preuba
     pension_mensual = calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)

     #Verifica la Salida
     pension_esperada = 3_200_000
     if round(pension_mensual,2) == round(pension_esperada):
          print("Prueba Ideal 1 exitosa")
     else:
          print("la prueba Ideal 1 falló")
    
def prueba_Error_1():
     """Ejecuta el caso de prueba Extraordinario 1"""
     #Entradas
     sexo = "Hombre"
     edad = 62
     semanas = 900
     salario_promedio = 2_500_000
     reemplazo = "No Aplica"
     entidad = "Colpensiones"

     #Procesos de Preuba
     pension_mensual = calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)

     #Verifica la Salida
     pension_esperada = "No cumple el minimo de semanas esperadas"
     if pension_esperada == pension_esperada:
          print("Prueba Error 1 exitosa")
     else:
          print("la prueba Error 1 falló")

def prueba_normal_privada_1():
     """Ejecuta el caso de Prueba Normal Privada 1"""
     #Entradas
     sexo = "Hombre"
     edad = 62
     semanas = "No aplica"
     salario_promedio = 3_000_000
     saldo_acomulado =350_000_000
     entidad = "Porvenir"
     factor = 171

     #Proceso de Prueba
     pension_mensual = calcular_pension_privado(saldo_acomulado, factor, edad, entidad)

     #Verifica salida
     pension_esperada = 2_046_783.63
     if round(pension_mensual,2) == round(pension_esperada,2):
          print("la Prueba Normal Privada 1 exitosa")
     else:
          print("la Prueba Normal Privada 1 falló")

def prueba_normal_privada_2():
     """Ejecuta el caso de Prueba Normal Privada 2"""
     #Entradas
     sexo = "Mujer"
     edad = 57
     semanas = "No aplica"
     salario_promedio = 2_500_000
     saldo_acomulado =280_000_000
     entidad = "Porvenir"
     factor = 195

     #Proceso de Prueba
     pension_mensual = calcular_pension_privado(saldo_acomulado, factor, edad, entidad)

     #Verifica salida
     pension_esperada = 1_435_897.44
     if round(pension_mensual,2) == round(pension_esperada,2):
          print("la Prueba Normal Privada 2 exitosa")
     else:
          print("la Prueba Normal Privada 2 falló")


     

prueba_normal_1()
prueba_extraordinario_1()
prueba_ideal_1()
prueba_Error_1()
prueba_normal_privada_1()
prueba_normal_privada_2()





     










