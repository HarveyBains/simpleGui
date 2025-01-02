"""
    Version 1.0
    DateTime:01/01/25 17:09
"""

import random
import pygame
import PySimpleGUI as sg

pygame.mixer.init()

myParagraph1:str = "Experiences from life can contain both memories of joy and difficulty. Beliefs in the present tend to attract more-of-the-same experiences that are supportive from the past. Belief determines new experience by combining the present with the past to actualise new experience. Experience and mental creativity in varying levels is being produced by each and every individual. In the present moment is where Spirit choses a probabilistic outcome that coordinates flesh and matter. Therefore the present is the frontline, the seat and point of power, for wielding determinance and mental creativity to actualise new reality. So try to get the feeling of this present minded moment-by-moment quality. By becoming present is key for seeing first-hand how auto behaviours in the moment can influence experience if not quality checked. By seeking new sense data that is contrary - we can bring about a reappraisal process. Flush out the old presuppositions with yes-no statements. Use creativity in the thinking mind to yield more attractive beliefs that can cause a change of direction. So try to get the feeling of this present minded moment-by-moment quality"
myParagraph2:str = "xxx"

# Create a pop which takes text input

def create_window(theme):
    sg.theme(theme)
    layout = [
        [sg.Text("Enter Time (s), Paragraph No:", font=("Helvetica", 10)), sg.Input("27,1", key="inp_ParaNo", size=(10, 1), justification="center", font=("Helvetica", 10), background_color="light grey", text_color="black")],
        [sg.Multiline(default_text=myParagraph1, key="inp_txtBlock", size=(60, 6), font=("Helvetica", 8), background_color="light grey", text_color="black", pad=(0, 10))],
        [sg.Text("", key="txt_Selected", font=("Helvetica", 8), size=(50,2), background_color="light grey", text_color=("black"), pad=(0, 10) )],
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
