import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui
import random

max=38
pyautogui.PAUSE = 0

print("Once started press 'q' to quit.")
sct = mss.mss()
dimensions = {
        'left': 1850,
        'top': 977,
        'width': 31,
        'height': 31
    }

img_catch = cv2.imread('catch.png')
img_cast = cv2.imread('cast.png')

fishing=False
action=""
count=0

while True:
    if fishing:
        img_target = cv2.imread('catch.png')
        action = "Catching"
    else:
        img_target = cv2.imread('cast.png')
        action = "Casting"

    scr = numpy.array(sct.grab(dimensions))

    # Cut off alpha
    scr_remove = scr[:,:,:3]
    result = cv2.matchTemplate(scr_remove, img_target, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(f"{action}. ({count+1} of {max}) Match%: {max_val}")
    src = scr.copy()
    if max_val > .85:
        fishing = not fishing
        randX = random.randint(0,21)
        randY = random.randint(0,21)
        pyautogui.click(x=1855+randX, y=982+randY)
        if not fishing:
            count+=1
            if count==max:
                print(f"End")
                break

    sleep_time = round(random.uniform(.05,.15), 4)
    sleep(sleep_time)
    if keyboard.is_pressed('q'):
        break