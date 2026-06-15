# NamedTuple es una extencion del tipo Tupla, es una buena alternativa para escribir clases
from collections import namedtuple

Persona1 = namedtuple('Persona1', 'Nombre Apellido Edad')

# Creamos una instancia de la clase (se agrega un constructor por default)
persona1 = Persona1('Jose', 'Martinez', 25)
print(persona1)

# Se puede crear una clase con los atributos de una lista
Persona2 = namedtuple('Persona2', ['Nombre', 'Apellido', 'Edad'])
per2 = Persona2('Juan', 'Gomez', 30)
print(per2)

# Podemos acceder a los atributos de manera individual por nombres
print(f'\nNombre: {per2.Nombre}\n'
      f'Apellido: {per2.Apellido}\n'
      f'Edad: {per2.Edad}')

# Tambien se puede acceder por indice
print(f'\nNombre: {persona1[0]}\n'
      f'Apellido: {persona1[1]}\n'
      f'Edad: {persona1[2]}')

# Podemos convertir los valores a una tupla literal
print(f'\n{tuple(persona1)}')

# Se pueden empaquetar los elementos de nuestra tupla
nombre, apellido, edad = per2
print(f'\nValores de la tupla persona2:\n{nombre}, {apellido}, {edad}\n')

# Asi mismo tambine se pueden desempaquetar pasandolos como argumentos
print(*per2)
print()

# NameTuple son inmutables al igual que las tuplas
# per2.Edad = 23 <----- esto es ilegal

# Subclases de NamedTuples
class Persona3(Persona2):
      # Agregamos un nuevo metodo a la clase Hija
      def conver_mayus(self):
            return f'Nombre Completo: {self.Nombre.upper()} {self.Apellido.upper()}'

per3 = Persona3('Maria', 'Laura', 35)
print(per3)
print(per3.conver_mayus())

# Otra forma de hacer Extend de la clase (Recomendada)
Persona4 = namedtuple('Persona4', Persona2._fields + ('email',))

# Se crea un objeto respectivo con el nuevo atributo
per4 = Persona4('Maria', 'Quintero', 35, 'Mquintero@mail.com')
print(f'\n{per4}\n')

# Metodos de ayuda (Build-in)
print(per4._fields)

# Metodo de convercion a diccionario
dicc_per4 = per4._asdict()
print(dicc_per4)