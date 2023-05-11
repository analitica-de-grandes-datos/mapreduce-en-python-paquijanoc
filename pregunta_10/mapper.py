#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

# Leer los registros del archivo data.csv y emitir pares clave-valor
with open('data.csv', 'r') as csvfile:
    for line in csvfile:
        line = line.strip()
        columns = line.split('\t')

        if len(columns) >= 2:
            letters = columns[1].split(',')  # La segunda columna son las letras separadas por ","
            number = columns[0]  # La primera columna es el número

            for letter in letters:
                print(f'{letter}\t{number}')