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
