class Padre:
    def __init__(self):
        self.__variable_dunder__ = 15
        self.__variable_privada = 10

if __name__ == '__main__':
    op = Padre()
    print(dir(op))
    print(f'Prueba de variable dunder: {op.__variable_dunder__}')
    print(f'Prueba de variable Name Mangling: {op._Padre__variable_privada}')