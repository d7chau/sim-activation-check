[![](https://github.com/d7chau/SIM-Activation-Check/blob/master/imgs/SIMActivationCheckLogo1.png)](https://github.com/d7chau/SIM-Activation-Check)

# Introduction to SIM Activation Check

Program used for checking the status of SIM cards (unactivated, activated, terminated) and updating the corresponding spreadsheet built using Python, specifically with the PyAutoGUI library.

## Getting Started

To run the program, right click on the `.exe` file and Run as Administrator (if a popup appears, click Run Anyways).

### Generating executable

Executables are available on the releases page, however you can also generate them via the following steps:

* `pip install pyinstaller`
* `pyinstaller -w -F SIM-Activation-Check.py`
* Check locally generated `dist` folder for executable

### Prerequisites

* Windows System
* Google Chrome
* Signed into your Google account (have access to WirelessSIMLog spreadsheet)
* Signed into WHMCS
* No Google Chrome windows or tabs should be open
* 1680x1050 resolution size (support for more resolution sizes can be implemented in the future)

## Features

Fail-Safe:
* Move mouse to top left corner of screen to abort and stop the program

## Built With

* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) - Handling keyboard and mouse events
* [OpenCV](https://opencv.org/) - Detecting accuracy (confidence level) of screenshots
* [PyInstaller](https://www.pyinstaller.org/) - Packages Python program into `.exe` format

## Future Implementations

Multiple Screen Resolution Support: 
* Take the same screenshots as the ones found in the imgs folder of this repository
* Add new screenshots to imgs folder
* Create new variables for each screenshot (newscreenshot_location = pyautogui.locateOnScreen('imgs/newscreenshot.png'))

## Versioning

Github was used for version control. For the versions available, see the [releases page on this repository](https://github.com/d7chau/SIM-Activation-Check/releases). 

## Authors

* **Dennis Chau** - *Entire program* - [SIM-Activation-Check](https://github.com/d7chau/SIM-Activation-Check)

