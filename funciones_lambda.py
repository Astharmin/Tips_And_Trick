# Ejemplo funcion normal
def sumar (a,b):
    return a + b

print(sumar(3,5))

# Ejemplo funcion lambda
sumar_lambda = lambda a,b: a + b
print(sumar_lambda(2,5))

# se puede usar en una linea de codigo
print((lambda a,b: a + b)(5,6))