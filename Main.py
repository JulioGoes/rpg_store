from Database.ConsultDatabase import consult_database
import PySimpleGUI as sg

teste = consult_database()
cabecalho = ("Name", "Type", "Seller")
sg.theme("Dark Red")

layout = [
    [sg.Table(teste, headings=cabecalho, justification="center")],
    [sg.Button('Proximo')]
]

window = sg.Window('RPG Store', layout, size=(500, 300))

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Proximo':
        pass

window.close()
