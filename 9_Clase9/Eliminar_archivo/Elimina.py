#Importamos el modulo
import os

#definimos el nombre del archivo
nombre_archivo='archivo_e.txt'

#Comprobar si el archivo existe en la ruta
#la funcion os.path.exists() devuelve true en caso de que el archivo exista y false en caso contrario
if os.path.exists(nombre_archivo):
    #si el archivo existe, procedera a eliminarlo
    #la funcion os.remove() elimina el archivo en la ruta especificada
    os.remove(nombre_archivo)
    print(f"archivo '{nombre_archivo}' eliminado")
else:
    #Si el archivo no existe le indico al usuario que no existe el archivo
    print(f"El archivo {nombre_archivo} no existe")    
