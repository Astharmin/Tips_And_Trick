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

