# Uso de operador is  en Poo

# Ejemplo en lista
lista_a = [1, 2, 3]
lista_b = lista_a

'''Ambas listas apuntan a la misma referencia
 Por lo tanto is regresa un True'''

print(f'\nlista a y b tienen el mismo contenido?:'
      f' {lista_a == lista_b}')
print(f'lista a y b son el mismo objeto?:'
      f' {lista_a is lista_b}')

# Creamos un nuevo objeto
lista_c = list(lista_a)

''' Al comparar el contemnido si da un valor verdadero
pero al apuntar un objeto en mrmoria si retorna False'''

print(f'\nlista a y c tienen el mismo contenido?:'
      f' {lista_a == lista_c}')
print(f'lista a y c son el mismo objeto?:'
      f' {lista_a is lista_c}')