#Atributos de clases
#Definimos la clase coche
class Coche:
    ruedas=4 #atributo de clase: todas las instancias de coche tienen 4 ruedas
    def __init__(self, marca, modelo):
        self.marca=marca #atributo de instancia
        self.modelo=modelo #atributo de instancia

print(Coche.ruedas)
#crear instancias de la clase Coche

coche1= Coche("toyota","corolla")
coche2 = Coche("Honda", "civic")

#acceder al atributo de clase de las instancias
print(coche1.ruedas)
print(coche2.ruedas)