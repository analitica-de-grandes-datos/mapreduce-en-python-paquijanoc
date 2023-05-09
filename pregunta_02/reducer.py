#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

max_amounts = {}

# Lee los pares clave-valor del mapper y realiza la reducción
for line in sys.stdin:
    line = line.strip()
    purpose, amount = line.split('\t', 1)
    amount = int(amount)
    
    if purpose in max_amounts:
        max_amounts[purpose] = max(max_amounts[purpose], amount)
    else:
        max_amounts[purpose] = amount

# Emite los resultados
for purpose, max_amount in max_amounts.items():
    print(f'{purpose}\t{max_amount}')