import PySimpleGUI as sg
from convert_function import convert

sg.theme('Black')
feet_label = sg.Text("Enter feet:")
inches_label = sg.Text("Enter inches:")
output = sg.Text('', key='output', text_color='white')

input_box1 = sg.InputText(key='feet')
input_box2 = sg.InputText(key='inches')

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

layout = [[feet_label, input_box1],
          [inches_label, input_box2],
          [convert_button, exit_button, output]]
window = sg.Window("Converter", layout=layout,)

while True:
    events, values = window.read()
    match events:
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
    try:
        meters = convert(values['feet'], values['inches'])
        window['output'].update(value=meters)

    except ValueError:
        sg.popup_ok("Please enter two values")
        continue

window.close()