#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Inicializar el contador por letra
letter_counts = {}

# Leer los pares clave-valor del mapper y contar los registros por letra
for line in sys.stdin:
    line = line.strip()
    letter, count = line.split('\t', 1)

    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

# Emitir los resultados
for letter, count in letter_counts.items():
    print(f'{letter},{count}')