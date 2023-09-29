import pyautogui
import webbrowser
import time

webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 

pyautogui.locateOnScreen('calc7key.png')

print(pyautogui.displayMousePosition())

# pyautogui.moveTo(70, 215)  # Firefox coordinates

# pyautogui.click()          # Click the mouse