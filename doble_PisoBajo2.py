class Padre:
    def __init__(self):
        self.variable_publica = 1
        self._variable_protegida = 2
        self.__variable_privada = 3

    def get_variable_privada(self):
        return self.__variable_privada

    def __metodo_privado(self):
        print('Accediendo metodo privado en clase Padre')

class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.variable_publica = 'Sobre Escrita 1'
        self._variable_protegida = 'Sobre Escrita 2'
        self.__variable_privada = 'Sobre Escrita 3'

    def __metodo_privado(self):
        print('Accediendo metodo privado en clase Hija')

if __name__ == '__main__':
    # Imprimir todos los atributos de la clase
    padre = Padre()
    print(dir(padre))

    # Accedemos a los atributos de la clase
    print(f'Variable publica: {padre.variable_publica}')
    print(f'Variable protegida: {padre._variable_protegida}')
    # print(f'Variable privada manda error: {padre.__variable_privada}')
    print(f'Variable privada usando name mangling: {padre._Padre__variable_privada}')

    # Name mangling es transparente para el programador
    print(f'Acceso por medio del metodo get: {padre.get_variable_privada()}')

    # Prueba de la clase Hija
    hijo = Hijo()
    print(f'Acceso publico desde clase Hijo: {hijo.variable_publica}')
    print(f'Acceso protegida desde clase Hijo: {hijo._variable_protegida}')
    print(f'Accseso privado desde hijo con Name mangling :{hijo._Hijo__variable_privada}')
    print(f'Accseso privado desde padre con Name mangling :{hijo._Padre__variable_privada}')
    
    # Prueba de acceso a metodos privados
    padre._Padre__metodo_privado()
    hijo._Hijo__metodo_privado()
    hijo._Padre__metodo_privado()