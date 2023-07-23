'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
'''
while True:
    letra = input('Digite M para Masculino ou F para feminino: ').upper()
    if letra == 'F':
        print('Feminino')
        break
    elif letra == 'M':
        print('Masculino')
        break
    else:
        print('Inválido digite novamente.')
        continue