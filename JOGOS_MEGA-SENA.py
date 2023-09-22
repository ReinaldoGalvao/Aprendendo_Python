from random import randint
import PySimpleGUI as sg

def gerar_jogos(quant):
    lista_jogos = []
    for _ in range(quant):
        lista = []
        cont = 0
        while cont < 6:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                cont += 1
        lista.sort()
        lista_jogos.append(lista)
    return lista_jogos

layout = [
    [sg.Text("  JOGA NA MEGA-SENA  ")],
    [sg.Text("Quantos jogos quer fazer: ", size=(20,1))],  # Adição do argumento size
    [sg.InputText(key="quant_jogos", size=(20,1))],  # Adição do argumento size
    [sg.Button("OK"), sg.Button("CANCELAR")],
    [sg.Text("Resultados aqui", key="resultados", size=(27,10))],  # Adição do argumento size
]

janela = sg.Window("    JOGA NA MEGA-SENA    ", layout, resizable=True, default_element_size=(27, 1))  # Adição do argumento default_element_size

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'CANCELAR':
        break
    if evento == "OK":
        quant_jogos = int(valores["quant_jogos"])
        lista_jogos = gerar_jogos(quant_jogos)
        resultados_texto = ''
        for i, l in enumerate(lista_jogos):
            resultados_texto += f'JOGO {i+1}: {l}\n'
        janela['resultados'].update(resultados_texto)

janela.close()
