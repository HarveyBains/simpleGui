"""
    Version 3.2
    DateTime:27/12/24 17:14
    Desc: Include Beeper
"""

import random
import pygame


PySimpleGUI_License = 'ekybJEMgagWvN0l5bineN1leVKHrlVwGZ9SYIj6JIFkhR5ltdumwVns7bM3tB0l9cDiJI7spIEktxNpWYf2aVcuqci2GVtJiRsCbIb67MvTHcSzxN2TLMhyPMqzOcB1nMayEwciVTGGllGj0ZBWd5szTZfU7RFlecRGExcv5elW91UlqbSnnR0WKZwXrJgz6aVWb9BuZIyjxoWx2LICVJnOKYAWR1mlcRsmMl5yCcp36QSiZOgixJ9IbYTXTJk22Z0XwkwiPLACYJ1O8Y0Wr1JlvTcGyFPz3dTCeIp6uIRkbJ0hAa9Wx5yzgIbikw0ifQD2g9mt7cdGYFSugeBSoI063IKizIlsRI5kgNs1xc33dRmvebkWJVkyeStUBQHidOWivIe1iMlT0Ee5mM2C8IEsZIKklRrhWdcGXVEJZca34Nj1MZVWqQciiOHizIdxYMRiL8Jy4NByx81yPMlD5IE0ZIuixwOiaR8GmFC0XZsUbVe4dcYGnlYy7ZXXQMeiOOaiCI8xlMji08lykNeyS8Oy3MLDYIZ1hIJiNwuixRmWX1FhdasWXxkBSZsGxRYypZMXsN9zoIvjeosiKSdGTFUyPdImFVq5wQlmLFnpzb0nYMdxhNQDAZLAUZT2m1Nh9a0Wjw4uBYh249WtoIhiDwLi9SGV3BpBbZDGJRSycZmX8NfznInj3oji2ORDzYFuVMzjZkguOMxTbkEyaLKjyEb2BMsyoJr9Q1bd9dd6516d63810b490dd340ab240764a0d3f8b28dd90f8e671b1995243ae117c525e82d67b728a1fd4423adc1866884df51f81552ea6eed4c7d27b25c3159105104e39f79a4530da6345c0d78f7e3fd3b1c2bfed28e24d711a64a1caff03f2ece6b7fb1b6ebe9ea25bbade96875514c1bc7eab6a4ddc90adc7e39af4c83ef4f3a5f7f38f6e94d61c4a9ee4bb47e31a05aac623c8149a223c6123d2b74eb2b6abd5be867e318c32297f936d21c68f1290f31a7b255b6bad0ec127839942986abe11c1bbda4b3b14d782f423bb2a7a65bf16279a08a76e797fce8bcba3b4360e0537521771c25c8bc15c3baf15658f54f89e4deccaebe6c2ce6ff8ccba77483077eb9106516e4d6ac44caf03eb8124022e7609a3340d02f2af8402d250a53d08e3fd93249d1ac52430e0e1f20667bae4408f8451c002c8252c297b427cdc19448370deca95cf4e6b7a2d4959d246c058fc265bdda6f3b34734ec17e54b51b7479fcbdfda3155baa073aae591b51c6476d44603705e086495475532d1b3c527290e225e6755d66c5e04186eb88403ffa591c9a1db0c82c85d0f5285b5f297e21d1ed9c906894b77df8f84f2fa77014c877aa8b488b36e313b97b32fd165d0ab1790d1c307c622dc9830c9a7ac2347f9f0c174c60e4f3981bbecc9a88561a08c4be7c967987a1913e9f1c209385df5c2eec188a2db7f4f68385f5acf73352286b7'

import PySimpleGUI as sg

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

        
        # Play the sound effect
        pygame.mixer.Sound("339129__indigoray__beep-select.wav").play()
        pygame.time.wait(1000)  # Adjust based on sound duration

    



        

    if event == sg.WINDOW_CLOSED or event == "OK":  # Close if "X" or "OK" clicked
        break

window.close()  # Close the window when done
