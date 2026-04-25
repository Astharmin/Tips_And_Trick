# Definimos una clase para una excepcion personaliada

# Validacion no indica cual es el problema
def validar(nomb_cplt):
    if len(nomb_cplt) < 3:
        raise ValueError
    else:
        print('Validacion correcta...')

# Validacion personalizada
class NombreCorto(ValueError):
    pass

def validar_mejorada(nomb_cplt):
    if len(nomb_cplt) < 3:
        raise NombreCorto(nomb_cplt)
    else:
        print('Validacion correcta...')

if __name__ == '__main__':
    nomb_A = 'pe'
    # validar(nomb_A)

    nomb_B = 'Ka'
    validar_mejorada(nomb_B)