import sys

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

edad = sys.argv[1]

print('Recibido:', int(edad))

if int(edad) >= 18:
  print("Es mayor de edad")
else:
  print("Es menor de edad")
