#Definimos distintas variables para usar en las comparaciones 

a=10
b=5
c=15
d=8

# Operador Logíco AND
resultado_and= (a > b) and (c > d)
print(f"resultado de (a > b) and (c > d) : {resultado_and}")

# Operador Logíco OR
resultado_or= (a < b) or (c > d)
print(f"resultado de (a < b) and (c > d) : {resultado_or}")

# Operador Logíco NOT
resultado_not= not (a < b) 
print(f"resultado not de (a < b): {resultado_not}") 

#Combinación
resultado_combinado=(a>b) and (not(c<d)) or (b<c)
print(f"Resultado Combinado: {resultado_combinado}")