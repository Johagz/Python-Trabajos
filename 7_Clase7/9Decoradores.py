#Ejemplo de Decorador Básico
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la funcion")
        Resultado=func(*args, **kwargs)
        print("Despues de ejecutar la Funcion ")
        return Resultado
    return wrapper

#Usamos el decorador en una funcion
@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

#LLamamos la funcion decorada
print("****Decorador en una funcion****")
saludar("Ana")
    
    
#Ejemplo decorador con parametro

def repetir_veces(veces):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for in range(veces):
                func(*args, **kwargs)
            return wrapper
        return decorador
    
@repetir_veces(3)
def decir_hola():
    print("hola")
    
print("decorador con parametro")
decir_hola()
