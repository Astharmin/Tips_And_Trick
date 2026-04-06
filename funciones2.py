def imprimir_vecor(x, y, z):
    return f'<{x}, {y}, {z}>'

# Desempaquetando iterables:
tupla_vec = (10, 3, 12)
lista_vec = [4,6,7]

# Desempaquetando Un diccionario
exp_generador = (x * x for x in range (3))
diccionario_vector = {'x':10, 'y':5, 'z':6}

if __name__ == '__main__':
    print(f'Desenpaquetando una Tupla: {imprimir_vecor(*tupla_vec)}')
    print(f'Desenpaquetando una Lista: {imprimir_vecor(*lista_vec)}')
    print(f'Desempaquetando un generador: {imprimir_vecor(*exp_generador)}')
    print(f'Desempaquetando un diccionario: {imprimir_vecor(**diccionario_vector)}')

