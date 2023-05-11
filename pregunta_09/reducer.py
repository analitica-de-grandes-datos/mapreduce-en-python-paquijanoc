#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Mantener una lista ordenada de los 5 registros con los valores más pequeños
top_values = []

# Leer los pares clave-valor del mapper y actualizar la lista de los 5 registros más pequeños
for line in sys.stdin:
    line = line.strip()
    value, record = line.split('\t', 1)
    value = float(value)

    if len(top_values) < 6:
        top_values.append((value, record))
        top_values.sort()
    elif value < top_values[-1][0]:
        top_values.pop()
        top_values.append((value, record))
        top_values.sort()

# Emitir los 5 registros con los valores más pequeños en orden ascendente
for value, record in top_values:
    print(record)