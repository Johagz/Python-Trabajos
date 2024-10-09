#Definir el nombre del archivo
nombre_archivo='archivo.txt'

#Leer todo el contenido de una sola vez
with open (nombre_archivo, 'r') as archivo:
    print("leyendo el Archivo de una vez con read():")
    contenido_completo=archivo.read()
    print(contenido_completo)
    print("-"*40)


#Ejemplo leer el archivo ñinea por linea

with open(nombre_archivo, 'r') as archivo:
    print("Leyendo el archivo linea por linea con readline()")
    linea=archivo.readline()
    while linea:
        print(linea.strip())
        linea=archivo.readline()
print("-"*40)

#Ejemplo leer todas las lineas del archivo a la vez con readlines()

with open(nombre_archivo, 'r') as archivo:
    print("Leyendo todas las lineas a la vez readlines()")
    lineas=archivo.readlines()
    for linea in lineas:
        print(linea.strip())
print("-"*40)


#Ejemplo de escritura en un archivo txt

with open(nombre_archivo, 'w') as file:
    file.write("Hola may \n")
    file.write("Hola Jose \n")
    print(contenido_completo)
print("-"*40)

#Ejemplo de agregar contenido al final de lo existente y crear un archivo si no existe

with open(nombre_archivo, 'a') as file:
    file.write("casa \n")
    file.write("Jose es lindo \n")
    print(contenido_completo)
print("-"*40)

#Ejemplo crear un archivo y si ya existe me indica un error de existencia

with open ('archivo_1.txt', 'x') as file:
    file.write("crea \n")
    file.write("no crea \n")
    print(contenido_completo)
print("-"*40)