"""

Controlling keyboard using python

"""

import pyautogui

pyautogui.click(100,100) # setting the position of the mouse to write
pyautogui.typewrite("Hello world!", intervel=0.2)  # gives gap 0.2 seconds between every character typing

pyautogui.typewrite(['a','b','left','left','X','Y'], interval=1)  # prints each charatcer with interval of 1 sec and moves left 2 times
                                                                         by left word
                                                                         
                                                                         
pyautogui.KEYBOARD_KEYS()  # gives list of keyboard keys avilable 

pyautogui.press('f1')   # press the f1 key

pyautogui.hotkey('ctrl','o')  # to use short cuts
