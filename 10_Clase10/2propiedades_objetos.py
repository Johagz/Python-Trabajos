#Propiedades de objetos 
# Definimos la clase persona

class Persona:
    def __init__(self, nombre, edad):
        #inicilaizamos las propiedades del objero
        self.nombre=nombre #propiedad nombre
        self.edad=edad #propiedad edad
    
#crear un objeto de la clase peesona

persona1=Persona("ANA", 30)
persona2=Persona("Maria", 20)
#ACCEDER A LAS PROPIEDADES DEL OBJETO
print(persona1.nombre)
print(persona1.edad)
print("-"*40)
print(persona2.nombre)
print(persona2.edad)