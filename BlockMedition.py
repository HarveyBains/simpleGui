"""
    Version 1.0
    DateTime:01/01/25 17:09
"""

import random
import pygame
import PySimpleGUI as sg

pygame.mixer.init()

myParagraph1:str = "Your present beliefs govern the actualisation of events.\nCreativity and experience is being created by each and every individual.\nYour present is where flesh meets with matter and spirit.\nTherefore your present is the point of power"
myParagraph2:str = "Your xxx govern the actualisation of events.\nCreativity xx experience is being created by each and every individual.\nYourxxxx present is where flesh meets with matter and spirit.\nxx your present is the point of xxxx"



def create_window(theme):
    sg.theme(theme)
    layout = [
        [sg.Text("Meditation Labels", font=("Helvetica", 14, "bold"))],
        [sg.Multiline(default_text=myParagraph1, key="inp_txtBlock", size=(50, 7), font=("Helvetica", 8, "bold"), background_color="light grey", text_color="black")],
        [sg.Text("", key="txt_Selected", font=("Helvetica", 6, "bold"))],
        [sg.Button("Start", key="btn_Start", size=(4, 2)), sg.Button("Theme Toggle", key="tgl_Theme"), sg.Input("20,1", key="inp_ParaNo", size=5, justification="center",font=("Helvetica", 8, "bold"), background_color="light grey")]
    ]
    return sg.Window("My Meditation Gui", layout, size=(1000, 600))

def myFunction(inputStr: str):
    valuesList: list = inputStr.split(".")
    randomSel: int = random.randint(0, len(valuesList) - 1)
    return (f"{valuesList[randomSel].strip()}")


def update_txtPara(txtNo: str) -> str:
    match txtNo:
        case "1": return myParagraph1
        case "2": return myParagraph2
        case _: return "Invalid paragraph number"
    


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
