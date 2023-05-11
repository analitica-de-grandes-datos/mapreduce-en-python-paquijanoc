#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

# Leer los registros del archivo data.csv y emitir pares clave-valor
with open('data.csv', 'r') as csvfile:
    for line in csvfile:
    # Eliminamos los posibles espacios en blanco al principio y al final de la linea
      line = line.strip()

    # Separamos la linea en sus distintas columnas, utilizando '   ' como delimitador
      columns = line.split('   ')

    # Si la linea no tiene 3 columnas, la ignoramos (no tiene fecha)
      if len(columns) != 3:
          continue

    # Obtenemos el mes de la fecha, que está en la segunda columna
      month = columns[1].split('-')[1]

    # Emitimos la pareja (mes, 1)
      print(f"{month}\t1")