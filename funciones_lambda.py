# Ejemplo funcion normal
def sumar (a,b):
    return a + b

print(sumar(3,5))

# Ejemplo funcion lambda
sumar_lambda = lambda a,b: a + b
print(sumar_lambda(2,5))

# se puede usar en una linea de codigo
print((lambda a,b: a + b)(5,6))

# Se puede usar lambda si es una funcion concreta
lista_tuplas = [(1,'b'),(4,'z'),(7,'a'),(3,'c')]
# lista_tuplas_ord = sorted(lista_tuplas, key=lambda x: x[1], reverse=True)
lista_tuplas_ord = sorted(lista_tuplas, key=lambda x: x[0], reverse=True)
print(lista_tuplas_ord)

print(list(range(-3,4)))
for valor in range(-3,4):
    print(valor, valor*valor)

# Aplicamos en una funcion lambda
lista_ordenada = sorted(range(-3,4), key=lambda valor: valor*valor)
print(lista_ordenada)