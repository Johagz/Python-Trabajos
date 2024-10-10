#Definir una funcion: parametros, con nombres y predeterminados
def presentar_persona(nombre, edad, ciudad="desconocida", profesion="desconocida"):
    print(f"nombre: {nombre}")
    print(f"edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"profesion: {profesion}")
    
#Ejemplo de llamada a la funcion 
#Usando argumentos posicionales

print(presentar_persona("ana",36))

#Ejemplo con argumentos posicionales y con nombres
print(presentar_persona("Luis",39,ciudad="caracas", profesion="ing"))

#Usando todos los argumentos con nombre 
print("Ejemplo de todos los argumentos con nombres")
print(presentar_persona(nombre="Marta",edad=38,ciudad="caracas", profesion="ing"))