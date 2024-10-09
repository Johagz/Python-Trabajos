#Crear un Diccionario
persona={
    "Nombre":"Emilia",
    "Edad":33,
    "ciudad":"Caba"
}

#Comprobar si una clave existe antes de acceder a su valor
clave="Edad"
if clave in persona:
    valor=persona[clave]
    print(f"El valor de {clave} es: {valor}") 
else:
    print(f"La clave {clave} no existe en el diccionario")

#Intentar acceder a un aclave que no existe

clave_inexistente= "pais"

if clave_inexistente in persona:
    valor=persona[clave_inexistente]
    print(f"El valor de {clave_inexistente} es: {valor}") 
else:
    print(f"La clave {clave_inexistente} no existe en el diccionario")
    
    
#otra forma de comprobar si una clave esta en el diccionario seria la siguiente
persona_5 = {
    "nombre": "Emilia",
    "edad": 33,
    "ciudad": "CABA"
}
print("nombre" in persona_5)

