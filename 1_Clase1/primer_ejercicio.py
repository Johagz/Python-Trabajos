# 1. Declaración de variables y constantes 
edad = 25                #variable int
nombre = "Ana"           #variable str
esta_estudiando = True  #variable booleana

#Declaración de Constantes 
PI = 3.14                #variable float
PAIS = "Argentina"       #variable str

# 2. Leer valores por teclado
edad = int(input("Introduce tu edad: "))                                               #Leer un número entero
nombre = input("Introduce tu nombre: ")                                                 #Leer una cadena de caracteres 
esta_estudiando = input("¿Estas estudiando? (si/no): ").lower()=="si"                   #Leer y convertir a booleano

# 3. Tipo de Datos 
Cantidad_de_libros = 10              #número (int)
titulo_libro = "El principito"       #Cadena de texto (string)  
es_interesante = True                #Booleano

# Convertir tipos de Datos 
edad_str = str(edad)                                  #convierte número en cadena de texto
Cantidad_de_libros_float = float(Cantidad_de_libros)  #Convierte entero a número de punto flotante

# 4. Imprimer Resultados en la consola
print("Nombre:", nombre)
print("Edad: ", edad)
print("¿Estas estudiando?: ", esta_estudiando)
print("Contaste PI: ", PI)
print("Constante Pais: ", PAIS)
print("Cantidad de Libros: ", Cantidad_de_libros)
print("Titulo del libro: ", titulo_libro)
print("¿Es interesante?: ", es_interesante)
print("Edad (Como cadena de texto): ", edad_str)
print("Cantidad de libros (como float): ", Cantidad_de_libros_float)