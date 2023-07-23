'''
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps)
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 
'''
tamanho = int(input('Diga o tamanho do arquivo em MB: '))
velocidade = int(input('Diga qual a velocidade da sua internet em Mbps: '))

taxa_dow = velocidade * 0.119209
minuto_mbs = taxa_dow * 60
temp_dow = tamanho / minuto_mbs

print('O download ira demorar {:.2f} minutos'.format(temp_dow))