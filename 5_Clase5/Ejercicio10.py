#Ejercicio 10: Buscar y Actualizar la Información en un Diccionario Anidado 
#1. Crea un diccionario que represente una base de datos de empleados de una empresa. El diccionario debe tener: 
#o nombre_empresa 
#o empleados, que es una lista de diccionarios, donde cada diccionario representa un empleado con: 
#▪ id_empleado 
#▪ nombre 
#▪ departamento 
#▪ salario 
#2. Escribe una función que busque y actualice el salario de un empleado dado su id_empleado. La función debe: 
#o Buscar el empleado por su id_empleado. 
#o Actualizar el salario del empleado a un nuevo valor proporcionado. 
#o Imprimir la información del empleado después de la actualización.

#Ejercicio 10: Buscar y Actualizar la Información en un Diccionario Anidado 

empresa={
    "Nombre-empresa":"Polar"
    "Empleados":[
        {"id_empleado":"Jmartinez","Nombre":"Jose","departamento":"Recursos Humanos","Salario":200},{"id_empleado":"Mgarcia","Nombre":"Maricela","departamento":"Financiero","Salario":250} ,
        {"id_empleado":"Lperez","Nombre":"Luis","departamento":"Marketing","Salario":190}
        ]
}

