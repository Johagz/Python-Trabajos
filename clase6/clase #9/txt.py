#paso 1 definir nombre del archivo
nombre_archivo= 'archivo.txt'
#paso 2 leer el contenido de una sola vez
with open (nombre_archivo, 'r') as archivo:
    print("leyendo el archivo de una vez con read():")
    contenido_completo=archivo.read()
    print(contenido_completo)
    print("-"*40)