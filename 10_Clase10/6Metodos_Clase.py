#Metodos de Clase
#Definimos una Clase
class Conejo:
    cantidad_de_conejos=0 #atributo d eclase
    def __init__(self, color, nombre):
        self.color=color
        self.nombre=nombre
        Conejo.cantidad_de_conejos+=1#aumenta la cantidad total de conejos

# el metodo de clase para obtener el total de conejos 
@classmethod
def total_conejos(cls):
    return f"total de conejos: {cls.cantidad_de_conejos}"

#crear instancia 
conejo1=Conejo("blanco", "Tambor")
conejo2=Conejo("Gris", "Pochoclo")

#llamar el metodo de clase
print(Conejo.total_conejos())