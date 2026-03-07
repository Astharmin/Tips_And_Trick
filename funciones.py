def mayusculas(texto):
    return texto.upper()

print(mayusculas('Hola\n'))

# las funcion se pueden tratar como objeto
variable_fun = mayusculas
print(f'Variable funcion: {variable_fun}')
print(f'Funcion Mayuscula: {mayusculas}')

print(variable_fun('\nCualquier Texto'))

# Eliminar referencia de la funcion
# del mayusculas

print(variable_fun('Salu2...'))
# ya se elimino la referencia ----> print(mayusculas('se elimino'))

# Acceder por default al nombre de la funcion
print(f'Nombre por default: {variable_fun.__name__}')

# Funcion en estructuras de datos
lita_fun = [mayusculas, variable_fun, str.upper]
print(lita_fun)

for fun in lita_fun:
    print(fun, fun('Saludos desde funcion'))

# Acceder directamente a funciones almacenadas
print(lita_fun[1]('Saludos desde variable_fun'))