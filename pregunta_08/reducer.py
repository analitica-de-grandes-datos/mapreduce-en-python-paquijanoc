#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_letter = None
total_sum = 0
total_count = 0

# Leer los pares clave-valor del mapper y calcular la suma y el conteo por letra
for line in sys.stdin:
    line = line.strip()
    letter, value = line.split('\t', 1)
    value = float(value)

    if current_letter is None:
        current_letter = letter

    if letter == current_letter:
        total_sum += value
        total_count += 1
    else:
        # Calcular el promedio y emitir la letra anterior con la suma y el promedio
        if total_count > 0:
            average = total_sum / total_count
            print(f'{current_letter}\t{total_sum}\t{average}')

        # Actualizar la letra actual y los valores totales
        current_letter = letter
        total_sum = value
        total_count = 1

# Calcular el promedio y emitir la última letra encontrada con la suma y el promedio
if current_letter is not None:
    if total_count > 0:
        average = total_sum / total_count
        print(f'{current_letter}\t{total_sum}\t{average}')