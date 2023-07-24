'''
def boas_vidas(quantidade, nome='Linda'):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')
    
boas_vidas(6)

//////////////////////////////

def cliente1(nome):
    print(f'Olá {nome}')
    

def cliente2(nome):
    return f'Olá {nome}'
    


x= cliente1('Maria')
y = cliente2('Jose')
print(x)
print(y)
//////////////////////////////

'''

def soma(*numeros):
    resultado = 0
    for nun in numeros:
        resultado += nun 
    return resultado
    
x = soma(2, 3, 4, 7)
print(x)