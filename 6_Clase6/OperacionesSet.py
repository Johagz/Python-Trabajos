#Crear conjuntos
conjunto1={1,2,3,4}
conjunto2={3,4,5,6}
conjunto3={7,8,9}

#Sub conjunro
es_subconjunto=conjunto1.issubset(conjunto2)
print("Es conjunto 1 un sub conjunto de conjunrto2", es_subconjunto)

#Superconjunto
es_superconjunto=conjunto2.issuperset(conjunto1)
print(f"Es conjunto 2 un superconjunto de conjunto 1 {es_superconjunto}")

#Disconjntos

son_disconjuntos=conjunto1.isdisjoint(conjunto3)
print(f"son conjunto 1 y conjunto 3 disconjunto {son_disconjuntos}")

#Simetria

simetria=conjunto1.symmetric_difference(conjunto2)
print(f"Diferencia simetrica entre conjunto1 y conjunto2 {simetria}")

#Union udate

conjunto1.update(conjunto2)
print(f"conjunto1 despues de la union con conjunto 2 {conjunto1}")


# Interseccion udate
conjunto1.intersection_update(conjunto2)
print(f"conjunto1 despues de la interseccion con conjunto 2 {conjunto1}")

#Difference udate

conjunto1.difference_update(conjunto3)
print(f"conjunto1 despues de la diferencia con conjunto 3 {conjunto1}")

#symetric difference udate

conjunto1.symmetric_difference_update(conjunto2)
print(f"conjunto1 despues de la diferencia simetrica con conjunto 3 {conjunto2}")
