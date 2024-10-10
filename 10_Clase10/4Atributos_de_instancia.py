#Atributos de instancias
#Definimos la clase 
class Gato:
    def __init__(self, color, nombre):
        self.color=color
        self.nombre=nombre
#crear difenentes objetos, es decir, instancias de la clase gatos

gato1=Gato("NEGRO","TORAO") 
gato2=Gato("Amarillo","Malndro")

#acceder a los atributos de instancia 
print(gato1.color)
print(gato2.color)
