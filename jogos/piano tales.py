import keyboard
import pyautogui
import win32api
import win32con
from time import sleep


def click(a, b):
    win32api.SetCursorPos((a, b))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


pyautogui.click(763, 468, duration=1)

while not keyboard.is_pressed('1'):
    if pyautogui.pixelMatchesColor(655, 386, (0, 0, 0)):
        click(655, 386)
    if pyautogui.pixelMatchesColor(728, 379, (0, 0, 0)):
        click(728, 379)
    if pyautogui.pixelMatchesColor(809, 380, (0, 0, 0)):
        click(809, 380)
    if pyautogui.pixelMatchesColor(900, 378, (0, 0, 0)):
        click(900, 378)
