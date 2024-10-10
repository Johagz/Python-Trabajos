import csv
#definimos los nombres de las columnas para el archivo csv
fieldnames= ["nombre","edad","ciudad"]
with open('archivo.csv', 'w', newline='') as file:  
    #El newline se utiliza para enviar lineas en blanco adicionales
    #creamos un objeto dictwriter
    #se pasa el archivo y la lista de nombres de las columnas(fieldnames)
    writer= csv.DictWriter(file, fieldnames=fieldnames)
    #escribir la fila de encabezados en el archivo csv
    writer.writeheader()
    #escribir un afila con los datos 
    #cada diccionario debe tener claves que coincidan  con los nombres de las columnas
writer.writerows({"nombre": "ana", "edad": "35", "ciudad": "caracas"})
     
     #escribir multiples filas de datos en el archivo
     
writer.writerows([
    {"nombre":"ana", "edad":"35", "ciudad": "caracas"},{"nombre":"Camila", "edad":"36", "ciudad": "caracas"}
    ])
    