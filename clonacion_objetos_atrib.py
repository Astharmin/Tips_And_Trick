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

# Clase Rectangulo usando dos puntos de referencia (Sup Izquierdo e Inf Derecho)
class Rectangulo:
    def __init__(self, sup_izq, inf_der):
        self.sup_izq = sup_izq
        self.inf_der = inf_der

    def __repr__(self):
        return (f'Rectangulo({self.sup_izq!r}, '
                           f'{self.inf_der!r})')

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

    # Definimos objetos con nuestra Clase
    rect_a = Rectangulo(Punto(0,1),
                        Punto(3,6))
    # Copia poco Profunda (Shallow)
    rect_b = copy.copy(rect_a)
    print(f'\nCopia Supericial del Rectangulo\n')
    print(f'Rectangulo A: {rect_a}')
    print(f'Rectangulo B: {rect_b}')

    # La copia Supericial afecta al otro Rectangulo
    rect_a.inf_der.y = 4
    print(f'\nEl cambio afecta al otro rectangulo por shallow copy\n')
    print(f'Rectangulo A: {rect_a}')
    print(f'Rectangulo B: {rect_b}')

    # Creacion de copia Profunda (Deep copy)
    rect_c = copy.deepcopy(rect_a)

    # Modificamos el valor en un punto sin afectar al otro
    rect_c.sup_izq.x = 2
    rect_a.sup_izq.y = 3
    print(f'\nEste cambio no afecta al otro rectangulo por copia profunda (Deep Copy)\n')
    print(f'Rectangulo A: {rect_a}')
    print(f'Rectangulo C: {rect_c}')