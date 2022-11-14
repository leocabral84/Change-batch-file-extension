import PySimpleGUI as sg


layout = [
    [sg.Text("1º DIGITE A EXTENSÃO ATUAL NO PRIMEIRO CAMPO\n2º DIGITE A EXTENSÃO DE SAÍDA NO SEGUNDO CAMPO")],
    [sg.Text("Extensão existente - Exemplo: .jpg")],
    [sg.InputText(key="exte_inicial")],
    [sg.Text("Nova extensão - Exemplo: .png")],
    [sg.InputText(key="exte_final")],
    [sg.Button("Gerar Bat"), sg.Button("Cancelar")],
    [sg.Text("", key="texto_informacao")],
]

janela = sg.Window("Renomear Extensão by LeoCabral", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break



    elif evento == "Gerar Bat":
        exte_inicial = valores["exte_inicial"]
        exte_final = valores["exte_final"]

        janela['texto_informacao'].update(f'Arquivo Gerado com sucesso\n\n'
                                          f'IMPORTANTE: Após gerar o arquivo\n'
                                          f'"Renomear_arquivos.bat" copie e cole,\n'
                                          f'na pasta onde deseja fazer as alterações\n'
                                          f'de extensão.\n\n'
                                          f'EXECUTE o arquivo "Renomear_arquivos.bat"\n'
                                          f'com dois cliques, dentro pasta onde irá fazer\nas alterações.\n')



        #ESTE SCRIPT FAZ ALTERAÇÃO NO CÓDIGO BAT DO PROGRAMA

        extensao_existente = exte_inicial
        extensao_alterar = exte_final

        with open('Renomear_arquivos.bat','w') as renomear:
           renomear.write(f'ren *{extensao_existente} *{extensao_alterar}')


janela.close()






