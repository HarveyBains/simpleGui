"""
    Version 1.0
    DateTime:01/01/25 17:09
"""

import random
import pygame
import PySimpleGUI as sg

pygame.mixer.init()

myParagraph1:str = "Historical experiences contains memories of both joy and pain. The beliefs of the present will attract supportive past memories. Beliefs weave the future using a combination of the past and incoming sense data to actualise events. Creativity and experience is being created by all individuals. The present moment is where Spirit meets flesh and matter. Therefore the present is the seat of power. Being present in the moment is key, for seeing how current behaviors are being induced. Looking for new sense data that is contrary can help the breakout. Induce what the existing beliefs are. See how new positive beliefs can be included to lead into a new direction."
myParagraph2:str = "xxx"

# Create a pop which takes text input


def create_window(theme):
    sg.theme(theme)
    layout = [
        [sg.Text("Enter Time (s), Paragraph No:", font=("Helvetica", 10)), sg.Input("20,1", key="inp_ParaNo", size=(10, 1), justification="center", font=("Helvetica", 10), background_color="light grey", text_color="black")],
        [sg.Multiline(default_text=myParagraph1, key="inp_txtBlock", size=(60, 6), font=("Helvetica", 8), background_color="light grey", text_color="black", pad=(0, 10))],
        [sg.Text("", key="txt_Selected", font=("Helvetica", 8), size=(59, 1), background_color="light grey", text_color=("black"), pad=(0, 10) )],
        [sg.Button("Go", key="btn_Start", size=(13, 1), font=("Helvetica", 14) ),sg.Button("Theme Toggle", key="tgl_Theme", size=(14, 1), font=("Helvetica", 13))]
    ]
    return sg.Window("My Meditation Gui", layout, size=(1000, 500))

def myFunction(inputStr: str):
    valuesList: list = inputStr.split(".")
    randomSel: int = random.randint(0, len(valuesList) - 1)
    return (f"{valuesList[randomSel].strip()}")


def update_txtPara(txtNo: str) -> str:
    match txtNo:
        case "1": return myParagraph1
        case "2": return myParagraph2
        case "3": return values["inp_txtBlock"]
    


theme = "DarkBlue3"  # Default theme
window = create_window(theme)


# Event loop: Keep the window open and responsive
while True:
    event, values = window.read(timeout=100)  # Read user interactions
    if event == "btn_Start":

        # update the txtParagraph input field
        txtParaNo:str = values["inp_ParaNo"].split(",")[1]
        window["inp_txtBlock"].update(update_txtPara(txtParaNo))

      
        # Update the text field with new content
        sendStr: str = values["inp_txtBlock"]
        window["txt_Selected"].update(myFunction(sendStr))
        window["btn_Start"].update(disabled=True)


        # Run the delay timer
        timerDelay:int = int(values["inp_ParaNo"].split(",")[0])
        for seconds in range(timerDelay, 0, -1):
            window.read(timeout=1000)
        window["btn_Start"].update(disabled=False)

        # Play the sound effect
        pygame.mixer.Sound("339129__indigoray__beep-select.wav").play()
        pygame.time.wait(1000)  # Adjust based on sound duration


    if event == "tgl_Theme":
        # Change theme
        if theme == 'DarkBlue3': theme = 'DarkBlue'
        else: theme = 'DarkBlue3'
        
        window.close()
        window = create_window(theme)

       

    if event == sg.WINDOW_CLOSED or event == "OK":  # Close if "X" or "OK" clicked
        break

window.close()  # Close the window when done
