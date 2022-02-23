from Database.ConsultDatabase import consult_database
import PySimpleGUI as sg

teste = consult_database()

layout = [
    [sg.Text(teste[0])]
]

window = sg.Window('RPG Store', layout, size=(400, 400))

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
