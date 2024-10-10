#Ejercicio 7: Contar Ocurrencias de Elementos en un Diccionario Anidado 
#1. Crea un diccionario que contenga información sobre tres clubes deportivos, cada uno con una lista de jugadores. 
#o Cada jugador es un diccionario con las claves: nombre y edad. 
#2. Cuenta cuántos jugadores en total tienen cada uno de los clubes 

#Ejercicio 7: Contar Ocurrencias de Elementos en un Diccionario Anidado 

clubes={
    "Futbol":[{"Nombre":"Julian","Edad":19}, {"Nombre":"Jose","Edad":18}],
    "Baloncesto":[{"Nombre":"Magali","Edad":17}, {"Nombre":"Genesis","Edad":18}],
    "Esgrima":[{"Nombre":"Rosa","Edad":32},{"Nombre":"Marcos","Edad":39}]
}
club1=clubes["Futbol"]
cantidad_de_jugadores=len(club1)
print(f"El Club de Futbol tiene {cantidad_de_jugadores} Jugadores")
club2=clubes["Baloncesto"]
cantidad_de_jugadores2=len(club2)
print(f"El Club de Baloncesto tiene {cantidad_de_jugadores2} Jugadores")
club3=clubes["Esgrima"]
cantidad_de_jugadores3=len(club3)
print(f"El Club de Esgrima tiene {cantidad_de_jugadores3} Jugadores")