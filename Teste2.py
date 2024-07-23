import pyautogui as pa
import time
import pyperclip
import keyboard
import os
import threading

procurar = "sim"

while procurar == "sim":
    try:
        img1 = pa.locateCenterOnScreen('click1.png')

        pa.click(img1.x, img1.y)
    except:
        time.sleep(1)
        print("não encontrei")