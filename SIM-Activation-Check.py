import pyautogui
import webbrowser
import time
from pyautogui import ImageNotFoundException

def urls_open (urls):
    for i in range(0,len(urls)):
        if i == 0:
            webbrowser.open(urls[i], autoraise=True) #Opens first URL in focus
            print("first url")
            time.sleep(2)
        else:
            webbrowser.open(urls[i]) 
            print("second url")

def unactivated_check():
    time.sleep(15)
    pyautogui.hotkey('ctrl', 'f') 
    pyautogui.write('UNACTIVATED')
    time.sleep(4.5)
    pyautogui.press('esc')
    pyautogui.press('left', presses=6, interval=0.25) 
    pyautogui.hotkey('ctrl', 'c') 
    pyautogui.hotkey('ctrl', 'tab') 
    time.sleep(1)
    pyautogui.click(1507,166) #Clicking WHMCS search bar
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(2)
    hideinactiveclients_location = pyautogui.locateOnScreen('imgs/hideinactiveclients.png', grayscale=True, confidence=0.7) #Uses screenshot to detect btn
    pyautogui.click(hideinactiveclients_location) #Turning 'Hide Inactive Clients' off
    time.sleep(1)
    cximg_location = pyautogui.locateOnScreen('imgs/cximg.png', grayscale=True, confidence=0.7) 
    pyautogui.click(cximg_location) #Clicking Cx name
    time.sleep(3)
    loginasclient_location = pyautogui.locateOnScreen('imgs/loginasclient.png', grayscale=True, confidence=0.7) 
    pyautogui.click(loginasclient_location) #Clicking 'Login as Client'
    time.sleep(2)
    wirelessplan_location = pyautogui.locateOnScreen('imgs/wirelessplan.png', grayscale=True, confidence=0.7) 
    pyautogui.click(wirelessplan_location) 
    time.sleep(6)

def activated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(1)
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'tab') #Go back to WirelessSIMLog
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)  
        pyautogui.write('ACTIVATED')

def unactivated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(1)
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'tab') #Go back to WirelessSIMLog
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)  
        pyautogui.write('UNACTIVATED')

def main():
    urls = ["https://shop.fongowireless.com/wirelessadmin/index.php", "https://docs.google.com/spreadsheets/d/1ZFn_k_oDB5vqmOTVyb2MnIMkWTzAm0KtXpg9jPPIYsM/edit#gid=0"]
    urls_open(urls)
    unactivated_check()
    try:
        activatedscreen_location = pyautogui.locateOnScreen('imgs/activatedscreen.png', grayscale=True, confidence=0.7)
        unactivatedscreen_location = pyautogui.locateOnScreen('imgs/unactivatedscreen.png', grayscale=True, confidence=0.7)

        if activatedscreen_location is not None: #ACTIVATED
            activated_confirmed()
            print("activated")

        elif unactivatedscreen_location is not None: #UNACTIVATED
            unactivated_confirmed()    
            print("unactivated")
            
        else:
            print("None were found")

    except ImageNotFoundException: #In case error crashes program
        pyautogui.alert('Error:ImageNotFoundException')

if __name__ == "__main__":
    main()