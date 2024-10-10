#Scope: Alcnce local y global en python
#declaramos una variable global
x=20

def funcion_local():
    x=10 # x es una variable local
    print(f"valor de x dentro de la funcion local : {x}")
funcion_local()

print(f"Valor de x fuera de la funcion: {x}")

def funcion_global():
    global x #para modificar la variable global
    x=30
    print(f"Valor de x dentro de la funcion global es: {x}")
    
funcion_global()
print(f"Valor de x fuera de la funcion: {x}")