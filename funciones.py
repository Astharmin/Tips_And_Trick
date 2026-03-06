def mayusculas(texto):
    return texto.upper()

print(mayusculas('Hola\n'))

variable_fun = mayusculas
print(f'Variable funcion: {variable_fun}')
print(f'Funcion Mayuscula: {mayusculas}')

print(variable_fun('\nCualquier Texto'))

del mayusculas

print(variable_fun('Salu2...'))
# ya se elimino la referencia ----> print(mayusculas('se elimino'))

# Acceder por default al nombre de la funcion
print(f'Nombre por default: {variable_fun.__name__}')