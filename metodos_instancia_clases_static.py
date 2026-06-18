# Metodos de instancia, clase y static mas sus dierencias
class MiClase:
    def metodo_instancia(self):
        # Retornamos una tupla
        return 'metodo de instancia ejecutado...', self

    @classmethod
    def metodo_clase(cls):
        # Retprnamos una tupla
        return 'Metodo de clase ejecutado...', cls

    @staticmethod
    def metodo_estatico():
        return 'metodo estatico ejecutado...'

if __name__ == '__main__':

    # Caso 1: Ejecutamos el metodo de instancia implicita
    objeto = MiClase()
    print(f'Metodo iniciado: {objeto.metodo_instancia()}')

    # Caso 2: Ejecutamos el metodo de instancia explicita
    print(f'Metodo iniciado: {MiClase.metodo_instancia(objeto)}')

    # Caso 3: Ejecutamos el metodo de instancia desde la clase
    print(f'Metodo Iniciado: {MiClase.metodo_instancia(MiClase)}\n')

    # Caso 4: Ejecutamos el metodo de clase implicita
    print(f'Metodo Iniciado: {MiClase.metodo_clase()}')

    # Caso 5: Metodo de clase desde las instancias
    print(f'Metodo iniciado: {objeto.metodo_clase()}\n')

    # Caso 6: Ejecutamos el metodo estatico
    print(f'Metodo Iniciado: {MiClase.metodo_estatico()}')

    # Caso 7: Ejecutamos el metodo estatico desde la instancia
    print(f'Metodo iniciado: {objeto.metodo_estatico()}')