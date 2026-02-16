# Ejemplo de asercion 1:
def div (a,b):
    assert b!= 0, 'Divicion entre 0'
    print(f'Resultado: {a/b}')

# Ejemplo de asercion 2:
def promedio (nota):
    assert len(nota) !=0, 'Lista vacia'
    print(f'Promedio total: {sum(nota)/len(nota)}')

# Ejemplo de asercion 3:
def descuentos (produtos, descuento):
    precio_descuento = produtos['Precio'] * (1.0 - descuento)
    print(f'Precio con descuento: {precio_descuento:0.2f}')
    assert 0 <= precio_descuento <= produtos['Precio'],\
        f'Descuento invalido: {precio_descuento:0.2f}'
    print('Descuento Valido...')

if __name__ == '__main__':
# <--- Ejemplo 1 --->
    #div(15,2)

# <--- Ejemplo 2 --->
#     lista2 = []
#     lista = [5,7,9,10]
#     promedio(lista)

# <--- Ejemplo 3 --->
    productos = {'nombre':'Camisa', 'Precio':150}
    descuentos(productos, 0.1)