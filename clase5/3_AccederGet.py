#Crear un Diccionario
persona= {"nombre": "Veronica", "Edad": 25, "Ciudad":"Buenos Aires"}

#Usar el Metodo .get() para acceder a los diccionarios

nombre=persona.get("nombre")
Edad=persona.get("Edad")
ciudad=persona.get("Ciudad")

#Imprimir
print("Nombre:", nombre)
print("Edad: ", Edad)
print("Ciudad", ciudad)

#Intentar acceder a una clave que no existe usando .get()
pais=persona.get("pais")
print("Pais", pais)

#Usar get con un valor  predeterminado si la clave no existe 

pais_predeterminado=persona.get("pais")
print("Pais (con valores predeterminados): ", pais_predeterminado)



