import pyautogui
import time


def click_accept_button():

    accept_button_location = None

    print('Looking for button.')
    while accept_button_location is None:
        try:
            accept_button_location = pyautogui.locateOnScreen('accept.png', confidence=0.7)
            time.sleep(1)
            print('Image found')
        except pyautogui.ImageNotFoundException:
            print('ImageNotFoundException: image not found')
    print("Button found !")
    accept_button_center = pyautogui.center(accept_button_location)
    pyautogui.click(accept_button_center)

    print("Match accepted! Exiting ...")
    time.sleep(5)
    exit()


click_accept_button()