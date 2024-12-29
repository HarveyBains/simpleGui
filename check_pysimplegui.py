import PySimpleGUI as sg

layout = [[sg.Text("PySimpleGUI is working!")], [sg.Button("OK")]]

window = sg.Window("PySimpleGUI Test", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "OK":
        break

window.close()