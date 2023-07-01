import keyboard
import time
from pynput.keyboard import Controller
from keyboard import press

kb = Controller()
char = ' '
string = "Your Text goes here"
speed = 1  # higher is slower


def runner(ch, str1):
    for j in range(len(str1)):
        ch = str1[j]
        kb.press(ch)


while True:
    if keyboard.is_pressed('Ctrl') and keyboard.is_pressed('['):
        print("Combination is pressed.")
        time.sleep(1)
        while not keyboard.is_pressed('Shift'):
            time.sleep(speed)
            runner(char, string)
            press('enter')

