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
print(f'{diccionario_correcto}\n')

'''
Si queremos garantizar un orden de insercion, 
entonces usaremos la paqueteria de OrdedDict
'''

from collections import OrderedDict

dicc_ordenado = OrderedDict(uno=1,dos=2,tres=3)
print(f'Diccionario: {dicc_ordenado}')

# Agregamos un nuevo elemneto
dicc_ordenado['cuatro'] = 4
print(f'Diccionario: {dicc_ordenado}\n')

# Obtener las llaves
print(f'llaves del diccionario ordenado:\n'
      f'{dicc_ordenado.keys()}')

# Modiicamos el valor de las llaves
dicc_ordenado['uno'] = -1
print(f'\nDiccionario: {dicc_ordenado}\n')
'''
Como podemos observar en el ejemplo,
se mantiene el orden de las llaves.
'''

# Eliminamos una llave
dicc_ordenado.pop('tres')
print(f'Diccionario: {dicc_ordenado}\n')

# Volvemos a insertar el elemento eliminado
dicc_ordenado['tres']=3
print(f'Diccionario: {dicc_ordenado}\n')

# DefaultDict es una subclase de la clase dict
