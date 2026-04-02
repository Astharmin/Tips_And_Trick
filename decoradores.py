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