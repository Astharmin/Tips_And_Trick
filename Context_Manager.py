from contextlib import contextmanager

# Forma de abrir y cerrar un archivo usando try y finally
# archivo = open('Txt/prueba.txt','w')
# try:
#     archivo.write('Hola desde python')
# finally:
#     archivo.close()

# Forma de abrir y cerrar un archivo usando with (Context Manager)
with open('Txt/prueba.txt','w') as archivo:
    archivo.write('Hola desde python\n')

# Manejo de Archivos de Context Manager en Clases

#<--- 1era Forma --->
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        self.archivo = open(self.nombre, 'w')
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()

#<--- 2da Forma usando decoradores --->
@contextmanager
def manejo_archivos(nombre):
    try:
        archivo = open(nombre, 'w',
                       encoding='utf-8')
        yield archivo
    finally:
        archivo.close()

#<--- 3era Forma usando tabuladores --->
class Identador():
    def __init__(self):
        self.nivel = 0

    def __enter__(self):
        self.nivel += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1

    def imprimir(self, mensaje):
        print(' ' * self.nivel + mensaje)

#<--- 4ta Forma usando contextlib --->
class Identador2():
    def __init__(self):
        self.nivel = 0

    @contextmanager
    def identar(self):
        try:
            self.nivel += 1
            yield self
        finally:
            self.nivel -= 1

    def imprimir(self, mensaje):
        print(' ' * self.nivel + mensaje)

if __name__ == '__main__':
    # Usando la 1era Forma
    with ManejoArchivos('Txt/prueba1.txt') as archivo:
        archivo.write('Hola desde la clase ManejoArchivos\n')
        archivo.write('Usando el Context Manager\n')

    # Usando la 2da Forma
    with manejo_archivos('Txt/prueba2.txt') as archivo:
        archivo.write('Hola desde la función "manejo_archivos"\n')
        archivo.write('Usando el Context Manager con @decoradores\n')

    # Usando la 3era Forma
    with Identador() as identador:
        identador.imprimir('Nivel 1:')
        with identador:
            identador.imprimir('Nivel 2:')
            with identador:
                identador.imprimir('Nivel 3:')
        identador.imprimir('De vuelta al Nivel 1')

    # Usando la 4ta Forma
    print()
    identador2 = Identador2()
    with identador2.identar() as id2:
        id2.imprimir('Nivel 1:')
        with id2.identar() as id3:
            id3.imprimir('Nivel 2:')
            with id3.identar() as id4:
                id4.imprimir('Nivel 3:')
        id2.imprimir('De vuelta al Nivel 1')