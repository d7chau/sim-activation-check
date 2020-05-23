import pyautogui
import webbrowser
import time

webbrowser.open("https://shop.fongowireless.com/wirelessadmin/index.php", autoraise=True) #Opens WHMCS in focus
webbrowser.open("https://docs.google.com/spreadsheets/d/1ZFn_k_oDB5vqmOTVyb2MnIMkWTzAm0KtXpg9jPPIYsM/edit#gid=0") #Opens WirelessSIMLOG in the next tab

# while True:
#     currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#     print("MouseX:" + str(currentMouseX) + "   MouseY:" + str(currentMouseY))

time.sleep(15)
pyautogui.hotkey('ctrl', 'f') 
pyautogui.typewrite(['u', 'n', 'a', 'c', 't', 'i', 'v', 'a', 't', 'e', 'd'])
time.sleep(4.5)
pyautogui.press('esc')
pyautogui.press('left', presses=6, interval=0.25) 
pyautogui.hotkey('ctrl', 'c') 
pyautogui.hotkey('ctrl', 'tab') 
time.sleep(1)
pyautogui.click(1507,166) #Clicking WHMCS search bar
pyautogui.hotkey('ctrl', 'v') 
time.sleep(2)
pyautogui.click(1432,315) #Turning 'Hide Inactive Clients' off
time.sleep(1)
pyautogui.click(1277,266) #Clicking Cx name
time.sleep(2)
pyautogui.click(326,766) #Clicking 'Login as Client'





