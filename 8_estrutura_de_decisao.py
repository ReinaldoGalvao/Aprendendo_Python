'''crie um programa onde pergunte os nomes dos participantes e eles escolhem um numero
se o numero do primeiro participante for maior imprima JOGADOR 1 WIN!
se o numero do primeiro participante for maior imprima JOGADOR 2 WIN!
se os numeros forem iguais imprima EMPATE!
'''
jogador1 = input('Fale o nome do primeiro jogador: ')
jogador2 = input('Fale o nome do segundo jogador:  ')

numeroJogador1 = int(input(f'{jogador1}, fale um numero: '))
numeroJogador2 = int(input(f'{jogador2}, fale um numero: '))

if numeroJogador1 > numeroJogador2: #SE O NUMERO DO JOGADOR1 FOR MAIOR ENTAO DE PRINT ('JOGADOR 1 WIN!')
    print('JOGADOR 1 WIN!')
    
elif numeroJogador1 < numeroJogador2: #SE O NUMERO DO JOGADOR2 FOR MAIOR ENTAO DE PRINT ('JOGADOR 2 WIN!')
    print('JOGADOR 2 WIN!')

else:
    print('EMPATE!') #COMO NENHUMA DAS OPÇOES ACIMA ATENDEU ENTAO DE print('EMPATE!') 