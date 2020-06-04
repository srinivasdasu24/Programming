"""

Documentation :pyautogui.readthedocs.org
Installation : pip install pyautogui
This program explains how to control the mouse using python

If you want to stop the program move the mouse to the top left corner as mouse control we are giving to program to make it stop

Raises FAILSAFE error when it encounters issue


"""
import pyautogui

pyautogui.size()  # gives the screen size
width, height = pyautogui.size()

pyautogui.position() # gives the position of the mouse

pyautogui.moveTo(10,10) # moves mouse to this position

pyautogui.moveTo(10,10,duration=1.5)  # moves mouse to this position in 1.5 seconds

pyautogui.moveRel(200,0,duration=2) # moves mouse to the right by 200 pixels in 2 seconds
pyautogui.movRel(0,-100,duration=1) # moves mouse to the left by 100 pixels in 1 second

pyautogui.click(399,38)

pyautogui.doubleClick()
pyautogui.rightClick()

pyautogui.displayMousePosition() # works well on terminal but on python IDE

# drawing program using gui by dragging

import pyautogui

pyautogui.click()
distance =200
while distance > 0:
    print(ditance,0)
    pyautogui.dragRel(distance,0,duration=0.1)  #moveright
    distance = distance -25
    print(0,distance)
    pyautogui.dragRel(0,distance,duration=0.1)  # move down
    print(-distance,0)
    pyautogui.dragRel(-distance,0,duration=0.1)  # move left
    distance = distance -25
    print(0,-distance)
    pyautogui.dragRel(0,-distance,duration=0.1)   #move up

