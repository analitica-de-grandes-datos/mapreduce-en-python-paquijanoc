#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

# Lee los registros del archivo y emite los pares clave-valor
for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')
    
    # Emite la segunda columna como clave y la línea completa como valor
    if len(columns) >= 2:
        key = columns[1]
        value = line
        print(f'{key}\t{value}')