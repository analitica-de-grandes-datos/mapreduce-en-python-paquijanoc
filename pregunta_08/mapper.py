#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

# Leer los registros del archivo data.csv y emitir pares clave-valor
with open('data.csv', 'r') as csvfile:
    for line in csvfile:
        line = line.strip()
        columns = line.split('   ')

        if len(columns) >= 3:
            letter = columns[0]  # La primera columna es la letra
            value = float(columns[2])  # La tercera columna es el valor (convertido a float)
            print(f'{letter}\t{value}')