#Usar Assert

print("-"*20, "Edad", "-"*20)
Edad=int(input("Ingrese su edad:"))
assert Edad>= 18, "Usted es menor de 19 años"
print(f"Usted es mayor y su edad es:{Edad}")