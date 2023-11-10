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

# def soma(*numeros):
#     resultado = 0
#     for nun in numeros:
#         resultado += nun 
#     return resultado

def somar(lista): #criei essa função para somar a lista numero
    return sum(lista) #aqui retorna a soma da lista

# x = soma(2, 3, 4, 7)
# print(x)


def calcular_media(lista):
    if len(lista) == 0:
        return "A lista esta vazia, não é possivel calcular a média."
    
    soma = sum(lista)
    
    media = soma / len(lista)
    
    return media

numeros = (int(input('Diga um numero: ')),
            int(input('Diga outro numero: ')),
            int(input('Diga mais um numero: ')),
            int(input('Fale um numero: ')),
            int(input('Diga mais uma vez numero: ')),
            int(input('Diga mais uma vez numero: ')),
            int(input('Diga mais uma vez numero: ')),
            int(input('Diga um numero novamente: ')),)
print(numeros)
x = somar(numeros)

mediax = calcular_media(numeros)



print(x)
print(mediax)