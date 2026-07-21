# this is simple python script to open notepad and write some text in it
# STEPS TO DO 
# 1- pip install pyautogui
# 2- import the module pyautogui
# 3- import time module
# 4- use s.press to press any key on your keyboard
# 5- use s.write to write any thing """"

""""""

import pyautogui as s
import time

s.press("win")
time.sleep(0.6)
s.write("notepad", interval=0.2)
s.press("enter")
time.sleep(1)
s.write("this is simple python script to open notepad", interval=0.2)
s.press("enter")
