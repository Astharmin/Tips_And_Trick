class Padre:
    def __init__(self):
        self.var_publica = 1
        self._var_protegida = 2
        self.__var_privada = 3

if __name__ == "__main__":
    padre = Padre()
    print(dir(padre))

    print(f'Variable pública: {padre.var_publica}')
    print(f'Variable protegida: {padre._var_protegida}')

    # print(f'Variable privada: {padre.__var_privada}')
    print(f'Variable privada: {padre._Padre__var_privada}')