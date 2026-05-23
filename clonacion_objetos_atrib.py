import copy

# Definimos un punto en plano 2D
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Punto ({self.x!r}, {self.y!r})'

    def __eq__(self, otro):
        return (isinstance(otro, Punto) and self.x == otro.x
                                        and self.y == otro.y)


if __name__ == '__main__':
    punto_a = Punto(1, 2)
    punto_b = copy.copy(punto_a)

    # Copia poco profunda
    print(f'Copia poco profunda (shallow)\n')
    print(f'Punto a: {punto_a}')
    print(f'Punto b: {punto_b}')

    # Comprobamos las diferencias de copias
    print(f'\nSon objetos con el mismo contenido?: '
          f'{punto_a == punto_b}')
    print(f'Son objetos con la misma referencia?: '
          f'{punto_a is punto_b}: ')