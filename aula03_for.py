''''
for i in range(7):
    print('Gol da Alemanha!')

print('Gol do Brasil')


tupla_alunos = ('ana', 'jose', 'joao', 'maria')

for i, aluno in enumerate(tupla_alunos):
    print(i, aluno)
'''

dict_alunos = {'joao':5, 'ana':9}
for aluno, nota in dict_alunos.items():
    print(f'O(a) aluno(a) {aluno} tirou a nota {nota} na prova')