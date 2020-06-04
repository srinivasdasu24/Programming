"""
Screenshot and image recognition using python

sudo apt-get installs scrot  -- for linux

github.com/asweigart/sushigoroundbot

"""

import pyautogui

pyautogui.screenshot("saves to the file")  # to take the screen shot

pyautogui.locateOnScreen("image you want to recognize")   #for image recognition  ,gives positio and height and width of the image

pyautogui.locateCenterOnScreen("image ")

pyautogui.moveTo((x,y),duration=1)

pyautogui.click((x,y))   # accepts tuple or normal x,y
