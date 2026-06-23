# Diccionarios - dicts
'''
Tambien conocidos como:
 ° Maps
 ° Hashmaps
 ° Lookup Tables
Etc, El consepto es el mismo: (llave-valor)
'''

# Ejemplo Clasico: directorio (llave=nombre, valor=telf)
directorio = {
    'Juan': 596701,
    'Alicia': 586803,
    'Carlos': 568374,
}
print(directorio)

# Recuperamos un elemento
print(f'\nNumero Recuperado: {directorio['Alicia']}\n')

# Podemos utilizar una expresion para crear un diccionario
valres = {x: x*x for x in range(5)}
print(f'Valores al cuadrado: {valres}\n')