# De manera explicita retorna None
def fun1(valor):
    if valor:
        return valor
    else:
        return None

# De manere implicita se retorna None
def fun2(valor):
    if valor:
        return valor

def fun3(valor):
    print(valor)

if __name__=='__main__':
    print(fun1(0))
    print(fun2(0))
    fun3(10)