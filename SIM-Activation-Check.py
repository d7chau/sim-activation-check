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
            time.sleep(2)
        else:
            webbrowser.open(urls[i]) 

def email_exists():
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('left', presses=6, interval=0.25) 
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c') 
    time.sleep(1)
    clipboard_text = pyperclip.paste() #Finds what copied in the clipboard

    if clipboard_text != "" and clipboard_text != "\r\n": #\r\n is blank
        return True
    else:
        return False

def account_search():
    pyautogui.hotkey('ctrl', 'tab') 
    time.sleep(1)
    pyautogui.click(1507,166) #Clicking WHMCS search bar
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a') 
    time.sleep(1)
    pyautogui.press('del') 
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')    
    time.sleep(2)
    hideinactiveclients_location = pyautogui.locateOnScreen('imgs/hideinactiveclients.png', grayscale=True, confidence=0.99) 
    pyautogui.click(hideinactiveclients_location) #Turning 'Hide Inactive Clients' off
    time.sleep(1)
    cximg_location = pyautogui.locateOnScreen('imgs/cximg.png', grayscale=True, confidence=0.7) 
    time.sleep(2)

    if cximg_location is not None:
        pyautogui.click(cximg_location) #Clicking Cx name
        time.sleep(3)
        loginasclient_location = pyautogui.locateOnScreen('imgs/loginasclient.png', grayscale=True, confidence=0.7) 
        pyautogui.click(loginasclient_location) #Clicking 'Login as Client'
        time.sleep(2)
        wirelessplan_location = pyautogui.locateOnScreen('imgs/wirelessplan.png', grayscale=True, confidence=0.7) 
        pyautogui.click(wirelessplan_location) 
        time.sleep(8)
        return True

    else: #If account not found
        account_not_found()
        return False

def account_not_found():
        pyautogui.hotkey('ctrl', 'tab') 
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)  
        pyautogui.typewrite('N/A')        

def unactivated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'tab') 
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)
        pyautogui.typewrite('UNACTIVATED')

def activated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'tab') 
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)   
        pyautogui.typewrite('ACTIVATED') 

def terminated_confirmed():
        pyautogui.hotkey('alt', 'left')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'tab') 
        time.sleep(1)
        pyautogui.press('right', presses=6, interval=0.25)  
        pyautogui.typewrite('TERMINATED')

def main():
    urls = ["https://shop.fongowireless.com/wirelessadmin/index.php", "https://docs.google.com/spreadsheets/d/1GyzBpWz3BUVpsmVHvA2WpC9z_AGyh4FlFMFP1ynVzaI/edit#gid=0"]
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
            if email_exists() == False: #If no email is detected, end program
                pyautogui.alert('Program Complete \n(no email detected)')
                break

            if account_search() == True: #If account is found...
                activatedscreen_location = pyautogui.locateOnScreen('imgs/activatedscreen.png', grayscale=True, confidence=0.7)
                unactivatedscreen_location = pyautogui.locateOnScreen('imgs/unactivatedscreen.png', grayscale=True, confidence=0.7)

                if activatedscreen_location is not None: #ACTIVATED
                    activated_confirmed()

                elif unactivatedscreen_location is not None: #UNACTIVATED
                    unactivated_confirmed()    
                    
                else: #TERMINATED
                    terminated_confirmed() 
                
        except ImageNotFoundException: #In case error crashes program
            pyautogui.alert('Error:ImageNotFoundException')

if __name__ == "__main__":
    main()