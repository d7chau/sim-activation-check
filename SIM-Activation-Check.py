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

def account_search():
    time.sleep(15)
    pyautogui.hotkey('ctrl', 'f') 
    pyautogui.write('Below Requires FOLLOW UP')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(2)
    pyautogui.press('down')
    pyautogui.press('left', presses=7, interval=0.25)  
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c') 
    pyautogui.hotkey('ctrl', 'tab') 
    time.sleep(1)
    pyautogui.click(1507,166) #Clicking WHMCS search bar
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(2)
    hideinactiveclients_location = pyautogui.locateOnScreen('imgs/hideinactiveclients.png', grayscale=True, confidence=0.7) 
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
    time.sleep(5)

def activated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(1)
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'tab') 
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)  
        pyautogui.write('ACTIVATED')

def unactivated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(1)
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'tab') 
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)  
        pyautogui.write('UNACTIVATED')

def terminated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'tab') 
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)  
        pyautogui.write('TERMINATED')

def main():
    urls = ["https://shop.fongowireless.com/wirelessadmin/index.php", "https://docs.google.com/spreadsheets/d/1ZFn_k_oDB5vqmOTVyb2MnIMkWTzAm0KtXpg9jPPIYsM/edit#gid=0"]
    urls_open(urls)
    
    try:
        account_search()
        activatedscreen_location = pyautogui.locateOnScreen('imgs/activatedscreen.png', grayscale=True, confidence=0.7)
        unactivatedscreen_location = pyautogui.locateOnScreen('imgs/unactivatedscreen.png', grayscale=True, confidence=0.7)

        if activatedscreen_location is not None: #ACTIVATED
            activated_confirmed()
            print("activated")

        elif unactivatedscreen_location is not None: #UNACTIVATED
            unactivated_confirmed()    
            print("unactivated")
            
        else: #TERMINATED
            terminated_confirmed()

    except ImageNotFoundException: #In case error crashes program
        pyautogui.alert('Error:ImageNotFoundException')

if __name__ == "__main__":
    main()

    