import csv
#definimos los nombres de las columnas para el archivo csv
alumno= ["nombre","edad"]
with open('alumnos.csv', 'w', newline='') as file:   
    writer= csv.DictWriter(file, fieldnames=alumno)
    #escribir la fila de encabezados en el archivo csv
    writer.writeheader()
    #escribir un afila con los datos 
    #cada diccionario debe tener claves que coincidan  con los nombres de las columnas 
    #escribir multiples filas de datos en el archivo
    writer.writerows([
    {"nombre":"Ana", "edad":"23"},{"nombre":"Luis", "edad":"25"}
    ])
    