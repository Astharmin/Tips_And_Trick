# Clonacion o copia de objetos

# Ejemplo de Copina Superficial

lista_a = [[1, 2], [3, 4], [5, 6]]
lista_b = list(lista_a)

print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

# Comprobacion de que los objetos son distintos (a nivel superficial)
# Cambiar a nivel superior no afecta a la otra lista

lista_a.append([7,8])
print('\nSon distintos objetos (Solo a nivel superior)')

print(f'\nNueva Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

# Comprobamos que los objetos internos tienen la misma referencia
lista_a[0][1] = 'A'
print('\nLa copia solo fue superficial, solo se copia en referencia')

print(f'\nLista a: {lista_a}')
print(f'Lista b: {lista_b}')
