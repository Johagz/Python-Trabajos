#lEER ARCHIVO TXT
#Definir el nombre del archivo
mi_archivo='Ejercicio.txt'

#Leer todo el contenido de una sola vez
with open (mi_archivo, 'r') as archivo:
    print("leyendo el Archivo de una vez con read():")
    todo_el_archivo=archivo.read()
    print(todo_el_archivo)
    print("-"*40)

with open(nuevo_archivo, 'w') as file:
    file.write("Hola Clase #9 \n")
    file.write("Viene la Clase #10 \n")
    todo_el_archivo=file.read()
    print(todo_el_archivo)
print("-"*40)