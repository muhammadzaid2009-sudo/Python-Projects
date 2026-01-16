import win32com.client
import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("---Welcome to RoboSpeeker---")

    robo = input("Enter What You Want RoboSpeeker to Say: ")
    speaker.speak(robo)

