[![](https://github.com/d7chau/SIM-Activation-Check/blob/master/imgs/SIMActivationCheckLogo.png)](https://github.com/d7chau/SIM-Activation-Check)

# Introduction to SIM Activation Check

Program used for checking if SIM cards are unactivated, activated, or terminated built using Python, specifically the PyAutoGUI library.

## Getting Started

To run the program, right click on the .exe file and Run as Administrator (if a popup appears, click Run Anyways).

### Prerequisites

-Windows System
-Google Chrome
-Signed into your Google account (have access to WirelessSIMLog spreadsheet)
-Signed into WHMCS
-No windows or tabs should be open
-1680x1050 resolution size (support for more resolution sizes can be implemented in the future)

## Built With

* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) - Handling keyboard and mouse events
* [OpenCV](https://opencv.org/) - Detecting accuracy (confidence level) of screenshots
* [PyInstaller](https://www.pyinstaller.org/) - Running Python files without Python needing to be downloaded

## Future Implementations

Screen Resolution: 
-Take the same screenshots as the ones found in the imgs folder of this repository
-Add new screenshots to imgs folder
-Create new variables for each screenshot (newscreenshot_location = pyautogui.locateOnScreen('imgs/newscreenshot.png'))

## Versioning

Github was used for version control. For the versions available, see the [commits on this repository](https://github.com/d7chau/SIM-Activation-Check/commits/master). 

## Authors

* **Dennis Chau** - *Entire program* - [SIM-Activation-Check](https://github.com/d7chau/SIM-Activation-Check)

