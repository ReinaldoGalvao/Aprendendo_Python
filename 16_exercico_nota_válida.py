'''
Escreva um programa que receba notas de um aluno (0 - 10), caso
a nota digitada esteja fora desse intervalo peça para o professor digitar
novamente.
'''

while True:
    nota = int(input('Qual a nota do aluno: '))
    if nota >= 0 and nota <= 10:
        print(f'nota salva com sucesso {nota}.')
        break
    print('Nota invalida digite novamente: ')