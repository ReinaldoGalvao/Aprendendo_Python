'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
'''

while True:
    letra = input('Diga uma letra: ').lower()
    if letra.isdigit():
        print('Não pode ser um número. Digite apenas letras.')
        continue
    if len(letra) != 1:
        print('Só pode ter 1 letra.')
        continue
    if letra == ' ':
        print('Não pode ter espaços')
        continue
    if letra in 'aeiou':
        print('Vogal')
        break
    else:
        print('Consoante')
        break
