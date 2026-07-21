import pyautogui as s
import time
s.press("win")
time.sleep(1)
s.write("whatsapp", interval=0.2)
s.press("enter")
time.sleep(0.2)
s.hotkey("ctrl" ,"f")
time.sleep(1)
s.write("zaid 2", interval=0.2)
s.press("enter")
s.write("hello bro how are you", interval=0.2)
s.press("enter")
