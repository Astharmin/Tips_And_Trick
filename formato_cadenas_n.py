print(' Formato de cadenas '.center(30,'='))
# Nuevo estilo de formato
nombre = 'Juan'
mi_cadena = 'hola, {}!'.format(nombre)
print(mi_cadena)

# convercion en hexadecimal
error = 500
cadena_hexa = 'Error en hexadecimal: {e1:x}'.format(e1=error)
print(cadena_hexa)

# convercion enteros a hexadecimal
entero = 50
cadena_f = 'Numero flotante: {entero:.2f}'.format(entero=entero)
print(cadena_f)

print(' Formato de cadenas con Interpolacion (f-string literal) '.center(70,'='))
# Interpolacion de cadenas
mi_cadena = f'Hola, {nombre}!'
print(mi_cadena)

# Interpolacion con convercion en hexadecimal
print(f'Error en hexadecimal: {error:x}')

# Interpolacion con convercion de entero a decimal
print(f'Numero Flotante: {entero:.2f}')

print(' Formato de cadenas con interpolacion y funciones '.center(70,'='))
# Ejemplos con llamados a funciones
a = 10
b = 3
print(f'Divicion: {a/b:.2f}')