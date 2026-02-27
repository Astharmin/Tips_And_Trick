# formato antiguo de cadenas
nombre = 'Juan'
mi_cadena = 'Hola, %s!' % nombre
print(mi_cadena)

# Convercion de enteros a hexadecimal
error = 500
cadena_hexa = 'Error en hexadecimal: %x' % error
print(cadena_hexa)

# varios valeres
cadena = 'Hola %s hay un error: %x' % (nombre, error)
print(cadena)

# Sustitucion de valores por diccionario
cadena = 'Hola %(nombre)s hay un error: %(error)x' % {'nombre':nombre,
                                                      'error':error}
print(cadena)