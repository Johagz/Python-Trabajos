#Ejemplo 1: Operacion Básica
def suma(a,b):
    return a+b

def restar(a,b):
    return a-b

#Funcion que recibe otra funcion como Callback
def operar(a,b,funcion_callback):
    resultado= funcion_callback(a,b)
    print(f"Resultado de la operacion: {resultado}")

#Uso de la Funcion operar con diferentes callback
print("****Ejemplo de Callbck simple****")
operar(5,3, suma)
operar(5,3, restar)


#Uso de una lambda como callback
operar(5,3, lambda a,b: a*b)
operar(5,3, lambda a,b: a/b)