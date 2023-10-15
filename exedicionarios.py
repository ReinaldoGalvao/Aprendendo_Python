pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}

nomep = input('Diga o nome: ')
idadep = input('Diga a idade: ')
sexop = input('Diga o sexo: '.upper())

if sexop == 'F':
    pessoas['sexo'] = sexop
    pessoas['idade'] = idadep
    pessoas['nome'] = nomep

print(pessoas)