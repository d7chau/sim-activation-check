import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

pyautogui.hotkey('ctrl', 'f') 
pyautogui.typewrite(['u', 'n', 'a', 'c', 't', 'i', 'v', 'a', 't', 'e', 'd'])
pyautogui.press('esc')

