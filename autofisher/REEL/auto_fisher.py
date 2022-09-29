from pyautogui import *
from numpy import random
from time import sleep
from pynput.keyboard import Key, Controller
import pyautogui
import time
import keyboard
import random
import win32api, win32con

keyboard = Controller()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

baitAmount = 5

def shop_work():
    pyautogui.click(x=855, y=450)#sell for gold
    time.sleep(.1)
    pyautogui.click(x=891, y=450)#sell for mobcoins
    #buy bait
    pyautogui.click(x=1035, y=450)
    time.sleep(.1)
    pyautogui.click(x=963, y=450)
    time.sleep(.1)
    pyautogui.click(x=1034, y=450)
    time.sleep(.1)
    pyautogui.click(x=817, y=450)
    time.sleep(.1)
    pyautogui.click(x=817, y=451)
    time.sleep(.3)
    hit_key('e')
    time.sleep(.5)
    hit_key('e')
    time.sleep(.5)
    hit_key('e')
    time.sleep(.1)
    print("***Replenished Bait!***")
    keyboard.press('a')
    time.sleep(1)
    keyboard.release('a')
    time.sleep(.1)
    pyautogui.dragRel(110, 0, duration = 1)
    time.sleep(.1)
    pyautogui.dragRel(40, 0, duration = 1)
    time.sleep(.1)
    pyautogui.dragRel(10, 50, duration = .5)
    type_this("#goto 973 26 -69")
    time.sleep(20)
    pyautogui.click(button='right')
    
def type_this(x):
    keyboard.press('t')
    time.sleep(2)
    text = x
    pyautogui.PAUSE = 0.02
    charList = [i for i in text]
    for char in charList:
        pyautogui.typewrite(char)
    time.sleep(2)
    hit_key(Key.enter)
    
def hit_key(x):
    keyboard.press(x)
    time.sleep(.1)
    keyboard.release(x)

def afk_check():
    keyboard.press('a')
    time.sleep(.5)
    keyboard.release('a')
    time.sleep(.2)
    keyboard.press('d')
    time.sleep(.5)
    keyboard.release('d')

def reel():
    time.sleep(.3)
    pyautogui.click(button='right')
    time.sleep(.5)
    pyautogui.click(button='right')
    time.sleep(3)

def auto_shop():
    #move camera towards lakemaster
    pyautogui.dragRel(-110, 0, duration = 1)
    type_this("#goto 932 30 -141")
    time.sleep(10)
    pyautogui.dragRel(-40, 0, duration = 1)
    time.sleep(3)
    pyautogui.dragRel(-10, -50, duration = .5)
    time.sleep(4)
    pyautogui.click()#click
    time.sleep(.1)
    shop_work()#sell/buy everything
    #repos mouse

print("Initializing")
time.sleep(4)
print("Starting now")
time.sleep(1.5)

#always looking to reel
start = time.time()
while 1:
    if pyautogui.locateOnScreen('image.png', confidence=0.4) != None:
        curr = time.time()
        elapsed = (curr - start)-1.5
        print("REELING")
        reel()
        baitAmount = baitAmount - 1
        print("--------------------\n","Elapsed time for catch: ", elapsed,"\n--------------------")
        start = curr
        time.sleep(1.5)

    else:
        print("Waiting for fish...")
        time.sleep(1)
            
