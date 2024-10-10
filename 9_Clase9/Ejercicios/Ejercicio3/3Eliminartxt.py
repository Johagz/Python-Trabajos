import os

#definimos el nombre del archivo
archivo_para_Eliminar='archivo_e.txt'

#Comprobar si el archivo existe en la ruta
#la funcion os.path.exists() devuelve true en caso de que el archivo exista y false en caso contrario
if os.path.exists(archivo_para_Eliminar):
    #si el archivo existe, procedera a eliminarlo
    os.remove(archivo_para_Eliminar)
    print(f"archivo '{archivo_para_Eliminar}' eliminado")
else:
    #Si el archivo no existe le indico al usuario que no existe el archivo
    print(f"El archivo {archivo_para_Eliminar} no existe")    

