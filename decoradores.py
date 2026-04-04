# Ejemplos comunes con decoradores: loggin, seguridad, caching

def deco_env(funcion):
    print('Estamos dentro de la funcion decoradora')
    return funcion

def saludar():
    return 'Saludos desde mi funcion...'

# Llamamos manualmente al decorador (no es comun en python)
funcion_retornada = deco_env(saludar)
print(funcion_retornada)

# La forma correcta
@deco_env
def saludar_fun():
    return 'Saludos desde funcion a decorar'

print(saludar_fun())

# Decorador que convierte el texto a mayusculas
def mayus(fun):
    def envol():
        # Mandamos a llamar la funcion original (Closure)
        resultado_orig = fun()
        resutado_modi = resultado_orig.upper()
        return resutado_modi
    return envol

@mayus
def saludar_minus():
    return 'hola...'

print(saludar_minus())

#<-------------->
# Decoradores Multiples

def negritas(fun):
    def fun_envol():
        return '<strong>' + fun() + '</strong>'
    return fun_envol

def enfatizar(fun):
    def fun_envol():
        return '<em>' + fun() + '</em>'
    return fun_envol

@negritas
@enfatizar
def saludar_html():
    return 'Hola con HTML'

print(saludar_html())

#<---------->
# Decoradores con argumento

def decorador_arg(fun):
    def fun_envol(*args, **kwargs):
        print('Se esta ejecutando Decorador')

        list_arg = []
        for indice, val_tupla in enumerate(args):
            list_arg.append(args[indice].upper())

        # Propagamos los parametros a la funcion principal
        # return fun(*args, **kwargs)

        # Propagamos los valores modificados
        return fun(*list_arg, **kwargs)
    return fun_envol

@decorador_arg
def funcion_saludar(titulo, nombre):
    print(f'{titulo}. {nombre}')

funcion_saludar('Ingeniera', 'Maria Quiroz')