"""
    Version 3.2
    DateTime:27/12/24 17:14
    Desc: Include Beeper
"""
import PySimpleGUI as sg
import random
import pygame

pygame.mixer.init()

layout = [[sg.Text("Meditation Labels")],
          [sg.Input("2, Mind, Body, Breath", key="inp_csvData")],
          [sg.Text("", key="txt_Selected")],
          [sg.Button("Start", key="btn_Start")]
         ]


def myFunction(inputStr: str):
    valuesList: list = inputStr.split(",")
    randomSel: int = random.randint(1, len(valuesList) - 1)
    return (f"{valuesList[randomSel]}")


window = sg.Window("My Meditation Gui", layout, size=(600, 700))




# Event loop: Keep the window open and responsive
while True:
    event, values = window.read(timeout=100)  # Read user interactions

    if event == "btn_Start":
        # Apply new user content
        window["inp_csvData"].update(values["inp_csvData"])
        
        # Update the text field with new content
        sendStr: str = values["inp_csvData"]
        window["txt_Selected"].update(myFunction(sendStr))
        window["btn_Start"].update(disabled=True)

        
        timerDelay = int(sendStr.split(",")[0])
        for seconds in range(timerDelay, 0, -1):
            window.read(timeout=1000)
        window["btn_Start"].update(disabled=False)

        # Initialize the pygame mixer

        sound = pygame.mixer.Sound("339129__indigoray__beep-select.wav")
        sound.play()
        pygame.time.wait(1000)  # Adjust based on sound duration

    



        

    if event == sg.WINDOW_CLOSED or event == "OK":  # Close if "X" or "OK" clicked
        break

window.close()  # Close the window when done
