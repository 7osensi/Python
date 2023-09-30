#           Author: Hussein Mohamed 
#           Description: Pyhton script to open the last email 

import pyautogui
import webbrowser
import time

webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 

time.sleep(8) # Give time for the page to load
      
pyautogui.moveTo(492, 298) 
time.sleep(2)
pyautogui.click()  

# To find the coordinates of the point you want 
# while True:
#   x, y =  pyautogui.position()
#   print(f"Mouse position : X = {x} and Y = {y}") 