"""
    Version 2
    Time:14:00
"""
import PySimpleGUI as sg
import random

layout = [[sg.Text("Meditation Labels")],
          [sg.Input("60, Mind, Body, Breath", key="inp_csvData")],
          [sg.Text("", key="txt_Selected")],
          [
              sg.Button("Update", key="btn_Submit"),
              sg.Button("Go", key="btn_Next")
          ]]


def myFunction(inputStr: str):
    valuesList: list = inputStr.split(",")
    randomSel: int = random.randint(1, len(valuesList) - 1)
    return (f"{valuesList[randomSel]}")


window = sg.Window("My Meditation Gui", layout, size=(600, 700))

# Event loop: Keep the window open and responsive
while True:
    event, values = window.read(timeout=100)  # Read user interactions

    if event == "btn_Next":
        # Update the text field with new content
        sendStr: str = values["inp_csvData"]
        window["txt_Selected"].update(myFunction(sendStr))
        window["btn_Next"].update(disabled=True)

        for seconds in range(10, 0, -1):
            window.read(timeout=1000)
        window["btn_Next"].update(disabled=False)

    if event == "btn_Submit":
        # Update the text field with new content
        window["inp_csvData"].update(values["inp_csvData"])

    if event == sg.WINDOW_CLOSED or event == "OK":  # Close if "X" or "OK" clicked
        break

window.close()  # Close the window when done
