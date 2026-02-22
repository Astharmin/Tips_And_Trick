# Uso de underscore en iterables
for _ in range(3):
    print(f'Hola...{_}')

# Uso de underscore en Tuplas
valor = ('Juan','Carlos',35)
nom, _ , ed = valor
print(f'\nNombre: {nom}')
print(f'Edada: {ed}')
print(f'Apellido: {_}')

# Uso de variable en lista
_ = list()
_.append(1)
_.append(2)
_.append(3)
print(f'\nVariable temporal asignada  a lista: {_}')