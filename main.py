import sys

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

edad = sys.argv[1]

print('Recibido:', int(edad))

if int(edad) >= 18:
  print("Mayor de edad")
else:
  print("Menor de edad")
