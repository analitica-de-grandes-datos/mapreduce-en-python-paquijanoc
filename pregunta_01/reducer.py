#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_word = None
count = 0

# Lee los pares clave-valor del mapper y realiza la reducción
for line in sys.stdin:
    line = line.strip()
    word, value = line.split('\t', 1)
    
    if current_word == word:
        count += int(value)
    else:
        if current_word:
            # Emite el resultado de la palabra anterior
            print(f'{current_word}\t{count}')
        current_word = word
        count = int(value)

# Emite el resultado de la última palabra
if current_word:
    print(f'{current_word}\t{count}')