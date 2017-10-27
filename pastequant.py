# This version pastes quantities

import pyautogui
import pyperclip
import csv
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

pyautogui.PAUSE = .5
pyautogui.FAILSAFE = True

with open('items.csv','rb') as f:
    reader = csv.reader(f)
    item_list = list(reader)

pyautogui.click(pyautogui.position())
pyautogui.click(pyautogui.position())

for item in item_list:
    print "Item:",item[0],"Quant:",item[1]
    #pyperclip.copy('-' + item[1])
    pyperclip.copy(item[1])
    pyautogui.press('0')
    pyautogui.keyDown('ctrlleft'); pyautogui.press('a'); pyautogui.keyUp('ctrlleft')
    pyautogui.keyDown('ctrlleft'); pyautogui.press('v'); pyautogui.keyUp('ctrlleft')
    #pyautogui.press('enter')
    pyautogui.press('down')
    
