# Definicion de una lista en una sola linea
lista_linea = ['Juan', 'Laura', 'Guadalupe']

# Formato consistente
lista_consis = [
    'Juan',
    'Laura',
    'Guadalupe',
]

# Formato con posibles errores
lista_error = [
    'Juan',
    'Laura',
    'Guadalupe'
    'Pedro'
]

print(f'''lista consistente: {lista_consis}
lista con error: {lista_error}
''')