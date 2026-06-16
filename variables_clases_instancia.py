# Dierencias entre variables de clases y de instancia
class Perro:
    num_patas = 4 # <- Variable de clase

    def __init__(self, nombre):
        self.nombre = nombre # <- Variable de instancia

# Si modificamos la variable de clase se actualiza en todos los objetos
Perro.num_patas = 5

# Se puede crear una variable de clase desde la misma
Perro.nombre = 'Clase perro'

# Creamos una variable que no este asignada a los objetos
Perro.num_orejas = 2

if __name__ == '__main__':
    pongoso = Perro('Pongoso')
    chichigua = Perro('Chihigua')

    # Cada objeto tiene su propio atributo de nombre
    print(f'Nombre del chucho: {pongoso.nombre}\n'
          f'Nombre del chucho: {chichigua.nombre}\n')

    # La variable de clase se puede acceder con la variable de clase o con los objetos
    print(f'cuantas patas tiene Pongoso?: {pongoso.num_patas}')
    print(f'cuantas patas tiene Chichigua?: {Perro.num_patas}')

    # No es posible acceder a la variable de instancia desde la clase
    # print(Perro.nombre)

    # Se puede modificar la variable de clase individualmente
    chichigua.num_patas = 6 # <- Aqui ocurre un detalle importante, se crea una variable de instancia temporal
    print(f'\ncuantas patas tiene Chichigua?: {chichigua.num_patas}')

    # Imprimimos el valor de la variable de instancia temporal y la variable de clase
    print(f'Variable de instancia creada: {chichigua.num_patas}'
          f'\nVariable de clase: {chichigua.__class__.num_patas}')

    # Accedemos a las variables de clases creadas al vuelo
    print(f'\n{Perro.nombre}\n{pongoso.nombre}')

    # Accedemos a una variable de clase que no esta en las objetos
    print(f'Cuantas orejas tiene el perro: {pongoso.num_orejas}')