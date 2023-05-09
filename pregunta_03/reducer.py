#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Lee los pares clave-valor del mapper y realiza la reducción
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    
    # Emite el valor (línea completa) ordenado por la clave (segunda columna)
    print(value)