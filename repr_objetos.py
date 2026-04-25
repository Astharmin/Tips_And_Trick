# __str__ sirve para que la informacio sea legible para el Usuario
# __repr__ sirve para que la informacion no sea ambigua

class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

# Por default solo muestra el nombre de la clase y el ID
audi_a3 = Auto('Audi', 'A3', 'Azul')
print(f'Carro: {audi_a3}')

class AutoStr:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return (f'str: Marca: {self.marca}, '
                f'Modelo: {self.modelo}, '
                f'Color: {self.color}')

    def __repr__(self):
        return (f'repr: Marca: {self.marca}, '
                f'Modelo: {self.modelo}, '
                f'Color: {self.color}')

audi_a1 = AutoStr('Audi', 'A1', 'Negro')
# Hay varias formas de imprimir un Objeto
print(audi_a1)
print(audi_a1.__str__())
print(str(audi_a1))
print('{}'.format(audi_a1))
print(f'{audi_a1}')

# Es mas recomendable usar __repr__ en lugar __str__
print([audi_a1])
print(f'{audi_a1!r}')

# Podemos escojer que metodo usar
print(str(audi_a1))
print(repr(audi_a1))
