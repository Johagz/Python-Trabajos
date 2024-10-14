#Operaciones Matematicas

import math
num=float(input("Ingrese un numero con punto decimal:"))
numero_redondeado_superior=math.ceil(num)
print(f"El núemro {num} redondeado al número superior es:{numero_redondeado_superior}")
numero_redondeado_inferior=math.floor(num)
print(f"El núemro {num} redondeado al número inferior es:{numero_redondeado_inferior}")
Raiz_cuadrada=math.sqrt(num)
print(f"La raiz cuadrada del número {num} es:{Raiz_cuadrada}")
factorial_num=math.factorial(numero_redondeado_superior)
print(f"El factorial del número redondeado superior {numero_redondeado_superior} es:{factorial_num}")
factorial_num1=math.factorial(numero_redondeado_inferior)
print(f"El factorial del número {numero_redondeado_inferior} es:{factorial_num1}")
potencia=math.pow(num,8)
print(f"La potencia del número {num} elevado a la 8 es:{potencia}")
