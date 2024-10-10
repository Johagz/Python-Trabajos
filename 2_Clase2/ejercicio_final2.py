#Escribe un programa que clasifique a una persona en una categoría 
# según su edad. Usa un condicional if tradicional con operadores 
# lógicos (and, or) para las siguientes categorías:
# ✓ "Niño" si la edad está entre 0 y 12 años.
# ✓ "Adolescente" si la edad está entre 13 y 19 años.
# ✓ "Adulto" si la edad está entre 20 y 64 años.
# ✓ "Adulto Mayor" si la edad es 65 o más

edad=int(input("Ingrese por favor su edad: "))

if edad>=0 and edad<=12:
    print(f"Usted es un niño ya que su edad es {edad} y entra en el rango de la niñes que esta definido entre 0 y 12 años")
elif edad>=13 and edad<=19:
    print(f"Usted es un adolescente ya que su edad es {edad} y entra en el rango de la Adolescencia que esta definido entre 13 y 19 años")
elif edad>=20 and edad<=64:
    print(f"Usted es un adulto ya que su edad es {edad} y entra en el rango de la edad adulta que esta definida entre 20 y 64 años")
elif edad==65 or edad>65: #Aqui podria poner sin el or la condición edad>=65
    print(f"Usted es un adulto mayor ya que su edad es {edad} y es igual o mayor a 65 años")
else:
    print("la edad que introdujo no es valida por ser menor a cero, verifique por favor") 
    
    