#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Inicializar el contador de meses
month_counts = {}

# Leer los pares clave-valor del mapper y contar los meses
for line in sys.stdin:
    line = line.strip()
    month, count = line.split('\t')

    if month in month_counts:
        month_counts[month] += int(count)
    else:
        month_counts[month] = int(count)

# Emitir los resultados
for month, count in month_counts.items():
    print(f'{month}\t{count}')