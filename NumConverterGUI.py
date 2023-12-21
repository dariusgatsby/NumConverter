import PySimpleGUI as sg
from convert_function import convert

feet_label = sg.Text("Enter feet:")
inches_label = sg.Text("Enter inches:")
output = sg.Text('', key='output', text_color='black')

input_box1 = sg.InputText(key='feet')
input_box2 = sg.InputText(key='inches')

convert_button = sg.Button("Convert")

layout = [[feet_label, input_box1],
          [inches_label, input_box2],
          [convert_button, output]]
window = sg.Window("Converter", layout=layout)

while True:
    events, values = window.read()

    meters = convert(values['feet'], values['inches'])
    window['output'].update(value=meters)

window.close()