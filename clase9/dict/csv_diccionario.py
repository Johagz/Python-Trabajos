import csv

with open('archivo2.csv', 'r') as archivo:
    reader= csv.reader(archivo)
    for fila in reader:
        print(fila)
        