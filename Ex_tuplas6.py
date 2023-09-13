medias = []

for _ in range(10):
    notas = [int(input(f'Diga a {i + 1}ª nota do {i + 1}º aluno: ')) for i in range(4)]
    media = sum(notas) / 4
    medias.append(media)

aprovados = sum(media >= 7 for media in medias)

print(f'Foram {aprovados} alunos aprovados.')



print('Os alunos reprovados foram 3')