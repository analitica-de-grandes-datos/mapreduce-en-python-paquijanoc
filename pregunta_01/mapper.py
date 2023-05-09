#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import csv

# Lee los registros del archivo credit.csv y emite los pares clave-valor
with open('credit.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        credit_history = row[2]  # Obtiene el valor de la tercera columna (credit_history)
        print(f'{credit_history}\t1')