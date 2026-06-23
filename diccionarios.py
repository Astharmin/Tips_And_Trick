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

# Los diccionarios no se pueden generar con elementos mutables
lista = [1,2,3]
# diccionario_erroneo = {lista:'A'}
# print(diccionario_erroneo)

tupla = (1,2,3)
diccionario_correcto = {tupla:'A'}
print(diccionario_correcto)