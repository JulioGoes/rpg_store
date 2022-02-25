from Database.ConsultDatabase import consult_database
from Database.InsertDatabase import insert_database
from Database.DeleteFromDatabase import delete_from_database
import PySimpleGUI as sg

products = consult_database()
opa = '-'
header = ("Name", "Type", "Seller")
sg.theme("Dark")

layout = [
    [sg.Table(products, headings=header, justification="center",
              select_mode=None, key='-TABLE-', enable_events=True)],
    [sg.Text('Add Products', justification="center", size=(100, 1))],
    [sg.Text('Name: '), sg.Input(size=(20, 1), key='NAME', do_not_clear=False),
     sg.Text('Type: '), sg.Input(size=(20, 1), key='TYPE', do_not_clear=False),
     sg.Text('Seller: '), sg.Input(size=(20, 1), key='SELLER', do_not_clear=False)],
    [sg.Button('Add', key='-ADD-'), sg.Button('Delete', key='-DELETE-')]
]

window = sg.Window('RPG Store', layout, size=(700, 300))

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-ADD-':
        product_name = values['NAME']
        product_type = values['TYPE']
        product_seller = values['SELLER']
        insert_database(product_name.title(),
                        product_type.title(),
                        product_seller.title())
        products = consult_database()
        window.find_element('-TABLE-').Update(products)
    if event == '-DELETE-':
        select_row = values['-TABLE-'][0]
        select_row_name = products[select_row][0]
        delete_from_database((select_row_name))
        products = consult_database()
        window.find_element('-TABLE-').Update(products)


window.close()
