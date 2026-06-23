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

from collections import OrderedDict, defaultdict, ChainMap
from types import MappingProxyType

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
dicc_default = defaultdict(lambda : 'Valor Erroneo')
dicc_default['a'] = 1
dicc_default['b'] = 2
dicc_default['c'] = 3

print(f'Diccionario: {dicc_default.items()}')

# Imprimimos un elemento no existente
print(f'Diccionario: {dicc_default['d']}\n')

# Podemos crear valores como una lista
dicc_default_list = defaultdict(list)
dicc_default_list['Nombres'].append('Juan')
dicc_default_list['Nombres'].append('Karla')
dicc_default_list['Nombres'].append('Pedro')

print(f'Diccionario: {dicc_default_list}\n')

# Observamos que se pueden seguir usando las funciones asociados a diccionarios
print(dicc_default_list.items())
print(dicc_default_list.keys())
print(dicc_default_list.values())

# Buscar en multiples diccionario
dicc = {'uno': 1, 'dos': 2, 'tres': 3}
dicc2 = {'cuatro': 4, 'cinco': 5, 'seis': 6}

# Procedemos a combinar ambos diccionarios
comb_dic = ChainMap(dicc, dicc2)
print(f'\nDiccionario combinado: {comb_dic}')

# Buscamos en todos los diccionarios
print(f'\nElemento encontrado: {comb_dic['cinco']}\n')

# Error keyerror
# print(comb_dic['siete'])

# obtencion de diccionarios de solo lectura (read-only)
dicc_modificable = {'uno': 1, 'dos': 2, 'tres': 3}
dicc_solo_lectura = MappingProxyType(dicc_modificable)

print(f'Diccionario de solo lectura:\n'
      f'{dicc_solo_lectura}')
print(f'Elemento del diccionario: {dicc_solo_lectura['dos']}')

'''
Si queremos modiicar el diccionario de solo lectura
arrojara un error de TypeError.
'''
# dicc_solo_lectura['uno'] = -1

'''
Si modificamos el diccionario mutable
afecta al de solo lectura.
'''
dicc_modificable['dos'] = 22
print(f'Valores modificados: {dicc_modificable,dicc_solo_lectura}')