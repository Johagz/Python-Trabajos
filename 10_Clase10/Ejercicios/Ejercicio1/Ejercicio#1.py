#Sistema de gestion de estuduantes

class Estudiante:
    def __init__(self, nombre, edad, notas):
        #inicilaizamos las propiedades del objero
        self.nombre=nombre #propiedad nombre
        self.edad=edad #propiedad edad
        self.notas=notas# propiedad nota
    
    def promedio_notas(self):
        promedio= sum(self.notas) / len(self.notas)
        if promedio > 9:
            return "APROBADO"
        else: 
            return "REPROBADO"

class Curso:
    estudiantes = [Estudiante("Maria", 12,[12,10,20]), Estudiante("Juan",13,[4,6,5])]
    
    @classmethod
    def listaAprobados(cls):
        aprobados = []
        for estudiante in cls.estudiantes:
            if Estudiante.promedio_notas(estudiante) == "APROBADO":
                aprobados.append(estudiante)
        return aprobados

print(Curso.listaAprobados())