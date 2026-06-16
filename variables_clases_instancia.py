# Dierencias entre variables de clases y de instancia
class Perro:
    num_patas = 4 # <- Variable de clase

    def __init__(self, nombre):
        self.nombre = nombre # <- Variable de instancia

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
