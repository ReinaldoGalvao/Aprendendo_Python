'''
Exercício Python 56:
Desenvolva um programa que leia o
time, quantidade de torcedores de cada estado e a media de torcedores dos 4 times.
No final do programa, mostre: 
a quantida de torcedores de cada estado, 
qual o time de cada estado com mais torcida.
'''

time = ''
time_rj = ''
time_sp = ''
total_torcidas = 0
torcidas_rj = 0
torcidas_sp = 0
soma_torcidas_rj = 0
soma_torcidas_sp = 0
soma_torcidas = 0
numero_torcida_rj = 0
numero_torcida_sp = 0
nome_maior_rj = ''
nome_menor_sp = ''
numero_menor_rj = 0
numero_menor_sp = 0
nome_maior_torcida = ''


def contem_apenas_letras(texto):
    return texto.isalpha()

def contem_apenas_numeros(texto):
    return texto.isnumeric()

def times_def(texto):
    return texto in ['FLAMENGO', 'VASCO', 'PALMEIRAS', 'SANTOS']

times_escolhidos = []

for i in range(1, 5):
    time = input('Diga o nome do {0}° TIME: '.format(i)).upper()
    while not contem_apenas_letras(time) or not times_def(time):
        print("Nome de time inválido. Tente novamente.")
        time = input('Diga o nome do {0}° TIME: '.format(i)).upper()
    if time == 'FLAMENGO' or time == 'VASCO':
        time_rj = time
        torcidas_rj += 1
    else:
        time_sp = time
        torcidas_sp += 1

    qts_torcidas_str = input('Diga quantidade de  torcedores do {0}: '.format(time))
    while not contem_apenas_numeros(qts_torcidas_str):
        print('Inválida. Digite apenas numeros, sem letras ou caracteres especiais.')
        qts_torcidas_str = input('Diga quantidade de  torcedores do {0}: '.format(time))
    if time == 'FLAMENGO' or time == 'VASCO':
        total_torcidas = int(qts_torcidas_str)
        soma_torcidas += total_torcidas
        soma_torcidas_rj += total_torcidas
        
        if i == 1:
            numero_menor_rj = total_torcidas
            nome_maior_rj = time_rj
            
        if nome_maior_rj == '':
            nome_maior_rj = time_rj
            
        if total_torcidas > numero_menor_rj:
            numero_torcida_rj = total_torcidas
            nome_maior_rj = time_rj
    else:
        total_torcidas = int(qts_torcidas_str)
        soma_torcidas += total_torcidas
        soma_torcidas_sp += total_torcidas
        
        if nome_menor_sp == '':
            nome_menor_sp = time_sp
            
        if i == 1:
            numero_menor_sp = total_torcidas
            nome_menor_sp = time_sp
            
        if total_torcidas < numero_menor_sp:
            numero_torcida_sp = total_torcidas
            nome_menor_sp = time_sp
media = soma_torcidas / 4
media_estado_rj = soma_torcidas_rj / 2
media_estado_sp = soma_torcidas_sp / 2

print('============================================================') 
print('============================================================') 
print('============================================================') 
print('Temos {} times do estado do Rio de Janeiro.'.format(torcidas_rj))
print('O estado do Rio de Janeiro tem {} torcedores.'.format(soma_torcidas_rj))
print('A média de torcidas no estados do Rio de janeiro é {}'.format(media_estado_rj))
print('O maior time do estado do Rio de Janeiro é o {}.'.format(nome_maior_rj))
print('============================================================') 
print('============================================================') 
print('Temos {} times do estado do São Paulo.'.format(torcidas_sp))
print('O estado de São Paulo tem {} torcedores'.format(soma_torcidas_sp))
print('A média de torcidas no estados do São Paulo é {}'.format(media_estado_sp))
print('O menor time do estado de São Paulo é o {}.'.format(nome_menor_sp))
print('============================================================') 
print('============================================================') 
print('A soma de todas as torcidas é {}'.format(soma_torcidas))
print('A média de torcidas por times é {}'.format(media))

