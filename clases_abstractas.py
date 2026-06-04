# ABC - Abstract Base Class

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

if __name__ == '__main__':
    # Problema: Se puede instanciar la Clase Base
    clase_base = ClaseBase1()
    # clase_base.metodo_1()

    # Funciona segun lo esperado
    clase_concreta = ClaseConcreta1()
    clase_concreta.metodo_1()

    # El metodo 2 se llama del metodo heredado
    clase_concreta.metodo_2()