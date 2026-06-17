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

