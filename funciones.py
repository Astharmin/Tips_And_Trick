def mayusculas(texto):
    return texto.upper()

print(mayusculas('Hola\n'))

# las funcion se pueden tratar como objeto
variable_fun = mayusculas
print(f'Variable funcion: {variable_fun}')
print(f'Funcion Mayuscula: {mayusculas}')

print(variable_fun('\nCualquier Texto'))

# Eliminar referencia de la funcion
# del mayusculas

print(variable_fun('Salu2...'))
# ya se elimino la referencia ----> print(mayusculas('se elimino'))

# Acceder por default al nombre de la funcion
print(f'Nombre por default: {variable_fun.__name__}')

# Funcion en estructuras de datos
lita_fun = [mayusculas, variable_fun, str.upper]
print(lita_fun)

for fun in lita_fun:
    print(fun, fun('Saludos desde funcion'))

# Acceder directamente a funciones almacenadas
print(lita_fun[1]('Saludos desde variable_fun'))

# Higher-order Funtions
def saludo(argumento_funcion):
    referencia_funcion = argumento_funcion('Hola desde mi funcion')
    print(referencia_funcion)

# Llamamos a la funcion
saludo(mayusculas)

# Nueva Implementacion de la funcion como argumento
def minusculas (texto):
    return texto.lower()

saludo(minusculas)

# Ejemplo explicito de Higher-order Funtions
print(list(map(mayusculas,['Texto 1','Texto 2','Texto 3'])))
print(list(map(minusculas,['Texto 1','Texto 2','Texto 3'])))

# Funciones anidadas
def mostrar(text):
    def convertir_minusculas(t):
        return t.lower()
    return convertir_minusculas(text)

print(mostrar('Desde funcion anidada...'))

# No se puede acceder:

# convertir_minusculas('Texto 1')
# mostrar.convertir_minusculas('Texto 1')

# Accedemos a la funcion anidada retornandola
def hablar(volumen):
    def minusculas(text):
        return text.lower()
    def mayusculas(text):
        return text.upper()

    if volumen > 0.5:
        return mayusculas
    else:
        return minusculas

# Forma de usar funcion anidada
print(hablar(0.6)('hablar fuerte...'))
print(hablar(0.2)('hablar suave...'))

variable_min = hablar(0.4)
print(variable_min('Hablo Suave...'))

# Closure
def hablar(text, vol):
    def min():
        return text.lower()
    def mayus():
        return text.upper()

    if vol > 0.5:
        return mayus()
    else:
        return min()

print(hablar('hablar fuerte...', 0.8))
print(hablar('Hablar bajo...', 0.4))

# Con Closure se pueden pre conigurar una funcion
def mostrar(titulo):
    def saludar(mensaje):
        return f'{titulo}. {mensaje}'
    return saludar

var_mostar = mostrar('Ingeniero')
var_mostar2 = mostrar('licenciado')

print(var_mostar('Armando Paredes'))
print(var_mostar2('Roberto Angulo'))

# Funcion callable
print(f'Mostrar si se puede llamar esta funcion: {callable(mostrar)}')
print(f'Se puede llamar esta funcion: {callable(hablar)}')
print(f'Se puede llamar este objeto: {callable(var_mostar)}')

print(f'objeto str se puede llamar: {callable('cualquier texto')}')

class Mostrar:
    def __init__(self, titulo):
        self.titulo = titulo

    def __call__(self, mensaje):
        return self.titulo + '. ' + mensaje

mostar_doc = Mostrar('Doctora')
print(mostar_doc('Rosa Meltroso'))

print(f'Se puede llamar este objeto: {callable(mostar_doc)}')