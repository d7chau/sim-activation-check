import pyautogui
import webbrowser
import time
import pyperclip
from pyautogui import ImageNotFoundException

pyautogui.FAILSAFE = True #moving mouse to top left corner of screen aborts program

def urls_open(urls):
    for i in range(0,len(urls)):
        if i == 0:
            webbrowser.open(urls[i], autoraise=True) #Opens first URL in focus
            print("first url")
            time.sleep(2)
        else:
            webbrowser.open(urls[i]) 
            print("second url")

def email_exists():
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('left', presses=6, interval=0.25) 
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c') 
    time.sleep(1)
    clipboard_text = pyperclip.paste() #Finds what copied in the clipboard

    if clipboard_text != "" and clipboard_text != "\r\n": #\r\n is blank
        print("clipboard text detected")
        return True
    else:
        print("clipboard text not detected")
        return False

def account_search():
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
    time.sleep(8)

def activated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'tab') 
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)  
        pyautogui.write('ACTIVATED')

def unactivated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
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
    urls = ["https://shop.fongowireless.com/wirelessadmin/index.php", "https://docs.google.com/spreadsheets/d/1XzngtTaRWeXNDgMWxpupXd0rOtKg4sM17lynj0q5VZw/edit#gid=0"]
    urls_open(urls)
    time.sleep(15)
    pyautogui.hotkey('ctrl', 'f') 
    pyautogui.write('Below Requires FOLLOW UP')
    time.sleep(2)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('left')

    while True:
        try:
            if email_exists() == False: # If no email is detected, end program
                pyautogui.alert('Program Complete \n(no email detected)')
                break

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