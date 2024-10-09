#Gestion de asistentes a un evento
#Crear un programa que administre una lista de asistentes a eventos sin permitir duplicados y que realice operaciones entre dos listas

#Crear conjuntos de Invitados 

invitados_viernes = {"Ana", "Carlos","Pedro","luis","Clara"}

invitados = {"paula","manuel","miguel","Pedro","Ana"}

#Mostar a los invitados unicos que asisten el viernes
print(f"Invitados de viernes: {invitados_viernes}")

#Monstar a los Invitados de un sabado
print(f"Invitados de viernes: {invitados}")

#mostrar la union (asistieron al menos un dia)

asistentes=invitados_viernes|invitados
print("Asistentes generales de los dos dias",asistentes)


#Mostar la interseccion (quien asistio ambos dias)

asiste_dos_dias=invitados_viernes&invitados

print("Asistentes en los dos dias",asiste_dos_dias)


#Mostrar la diferencia 
solo_viernes= invitados_viernes-invitados
print("Asistentes solo el viernes",solo_viernes)


#Agregar un nuevo invitado 

invitados_viernes.add("Mauricio")
print(f"los invitaos del sabado agregando a un nuevo invitado {invitados_viernes}")

#Eliminar invitado que cancelo

invitados_viernes.remove("Carlos")
print(invitados_viernes)

#Eliminar con discard

invitados_viernes.discard("Mauricio")
print(invitados_viernes)

#Comprobar si Ana asistio (Comprobar si un invitado esta en la lista)
print(f"Ana asistio el viernes?: {"Ana" in invitados_viernes} ")


