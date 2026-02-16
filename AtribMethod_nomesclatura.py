from Modulo import _fun_protegida, fun_publica


class MiClase:
    def __init__(self):
        self.var = 10
        self._var_protegida = 20

# <--- Prueba de la clase --->
if __name__ == "__main__":
    obj = MiClase()
    print(f'Valor de variable: {obj.var}')
    # no recomemdable acceder a variable protegidas
    print(f'Valor de variable protegida: {obj._var_protegida}')

    fun_publica()
    _fun_protegida()  