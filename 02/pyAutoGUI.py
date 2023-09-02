import pyautogui

# print(pyautogui.size())
# print(pyautogui.displayMousePosition())

#####################################################
########  1. install clangd from extensions  ########
#####################################################

pyautogui.moveTo(100, 120)  # Explorer coordinates

pyautogui.click()          # Click the mouse

pyautogui.moveTo(98, 354)  # Extentions coordinates

pyautogui.click()          

# Make sure the search bar is empty
for i in range(25):
    pyautogui.press('backspace') 

pyautogui.write('clangd', interval=1.5) # Write clangd

# pyautogui.PAUSE = 1

pyautogui.moveTo(223, 227) 

pyautogui.click()        

pyautogui.moveTo(857, 291) # Install button coordinates

pyautogui.click() 