#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_state = None
count = 0

# Lee los pares clave-valor del mapper y realiza la reducción
for line in sys.stdin:
    line = line.strip()
    state, value = line.split('\t', 1)
    
    if current_state == state:
        count += int(value)
    else:
        if current_state:
            # Emite el resultado del estado anterior
            print(f'{current_state}\t{count}')
        current_state = state
        count = int(value)

# Emite el resultado del último estado
if current_state:
    print(f'{current_state}\t{count}')