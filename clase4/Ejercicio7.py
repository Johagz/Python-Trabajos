#Ejercicio 7: Calcular el Precio final con descuento
costo=int(input("Ingrese el valor Total de la compra: "))
if costo>200:
    descuento=0.15*costo
    costo_final=costo-descuento
    print(f"Felicidades Ganaste un descuento de {descuento}")
    print(f"El monto que debia cancelar era {costo} con el descuento ahora debe cancelar {costo_final}")
else:
    print("Para participar por un Descuento su compra debe ser mayor a 200")
