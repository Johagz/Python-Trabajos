# Ejemplo 1: función que usa *args
def sumar_numeros(*args):
    total= 0
    for numero in args:
        total+=numero
    return total

print("Ejemplo del uso de args")
print(f"suma de 1,2,3,4: {sumar_numeros(1,2,3,4)}")    

#Ejemplo 2: funcion que usa **kwargs

def mostrar_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}:{valor}")

print("Ejemplo 2: kwargs")
mostrar_detalles(nombre="Ana", Edad=30, Ciudad="Caracas")

#Ejemplo 3: Combinados
def mostrar_info_completa(*args, **kwargs):
    print("Argumentos no Nombrados:")
    for arg in args:
        print(args)
    print("Argumentos Nombrados:")
    for clave, valor in kwargs.items():
        print(f"{clave}:{valor}")
        
print("Ejemplo 3: Combinado")
mostrar_info_completa(1,2,3,Nombre="Ama",Edad=20, Ciudad="Caracas")