#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_letter = None
numbers = []

# Leer los pares clave-valor del mapper y agrupar los números por letra
for line in sys.stdin:
    line = line.strip()
    letter, number = line.split('\t', 1)

    if current_letter is None:
        current_letter = letter

    if letter == current_letter:
        numbers.append(int(number))
    else:
        # Emitir la letra anterior junto con los números asociados en orden ascendente
        if len(numbers) > 0:
            numbers.sort()
            print(f'{current_letter}\t{",".join(str(num) for num in numbers)}')

        # Actualizar la letra actual y los números
        current_letter = letter
        numbers = [int(number)]

# Emitir la última letra encontrada junto con los números asociados en orden ascendente
if current_letter is not None:
    if len(numbers) > 0:
        numbers.sort()
        print(f'{current_letter}\t{",".join(str(num) for num in numbers)}')