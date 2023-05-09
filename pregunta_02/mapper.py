#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import csv

# Lee los registros del archivo credit.csv y emite los pares clave-valor
with open('credit.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Omitir encabezado
    
    for row in reader:
        purpose = row[3]  # Obtiene el valor de la cuarta columna (purpose)
        amount = int(row[4])  # Obtiene el valor de la quinta columna (amount) como int
        
        # Emite el par clave-valor al reducer
        print(f'{purpose}\t{amount}')