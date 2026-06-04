# ABC - Abstract Base Class
# Al heredar de ABC se obtine una jerarquia mas robusta y codigo mas mantenible
from abc import ABCMeta, abstractmethod


# Ejemplo sin ABC
class ClaseBase1:
    def metodo_1(self):
        raise NotImplementedError

    def metodo_2(self):
        raise NotImplementedError

class ClaseConcreta1(ClaseBase1):
    def metodo_1(self):
        print('Metodo 1 implementado...')

    # El metodo 2 no se va a implementar
    # Esto ya es un problema porque no se reporta la falta de implementacion

class ClaseBase2(metaclass=ABCMeta):
    # No es necesario la implementacion al ser absatrcto
    @abstractmethod
    def metodo_1(self):
        pass

    @abstractmethod
    def metodo_2(self):
        pass

class ClaseConcreta2(ClaseBase2):
    def metodo_1(self):
        print('Metodo 1 implementado...')

    # Estamos obligados a implementar todos los metodos abstractos
    def metodo_2(self):
        print('Metodo 2 implementado...')

if __name__ == '__main__':
    # Problema: Se puede instanciar la Clase Base
    clase_base = ClaseBase1()
    # clase_base.metodo_1()

    # Funciona segun lo esperado
    clase_concreta = ClaseConcreta1()
    # clase_concreta.metodo_1()

    # El metodo 2 se llama del metodo heredado
    # clase_concreta.metodo_2()

    # Con el metodo ABC no se puede crear objetos con el mismo implementado
    # clase_base = ClaseBase2()

    # Resolucion del problema: instanciando la ClaseConcreta2
    clase_concreta = ClaseConcreta2()
    clase_concreta.metodo_1()
    clase_concreta.metodo_2()