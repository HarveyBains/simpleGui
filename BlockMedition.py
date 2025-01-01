"""
    Version 3.2
    DateTime:27/12/24 17:14
"""

import random
import pygame
import PySimpleGUI as sg

pygame.mixer.init()

def create_window(theme):
    sg.theme(theme)
    layout = [
        [sg.Text("Meditation Labels", font=("Helvetica", 14, "bold"))],
        [sg.Multiline("5.\nYour present beliefs govern the actualisation of events.\nCreativity and experience is being created by each and every individual.\nwhere flesh meets with matter and spirit.\nTherefore your present is the point of power",
            key="inp_csvData", size=(50, 8), font=("Helvetica", 10, "bold"), background_color="light grey", text_color="black"
            )],
        [sg.Text("", key="txt_Selected", font=("Helvetica", 10, "bold"))],
        [sg.Button("Start", key="btn_Start", size=(4, 2)), sg.Button("Theme Toggle", key="tgl_Theme")]
    ]
    return sg.Window("My Meditation Gui", layout, size=(600, 900))

def myFunction(inputStr: str):
    valuesList: list = inputStr.split(".")
    randomSel: int = random.randint(1, len(valuesList) - 1)
    return (f"{valuesList[randomSel].strip()}")

theme = "DarkBlue3"  # Default theme
window = create_window(theme)

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

        timerDelay = int(sendStr.split(".")[0])
        for seconds in range(timerDelay, 0, -1):
            window.read(timeout=1000)
        window["btn_Start"].update(disabled=False)

        # Play the sound effect
        pygame.mixer.Sound("339129__indigoray__beep-select.wav").play()
        pygame.time.wait(1000)  # Adjust based on sound duration


    if event == "tgl_Theme":
        # Change theme
        if theme == 'DarkBlue3':
            theme = 'DarkBlue'
        else:
            theme = 'DarkBlue3'
        window.close()
        window = create_window(theme)

       

    if event == sg.WINDOW_CLOSED or event == "OK":  # Close if "X" or "OK" clicked
        break

window.close()  # Close the window when done
