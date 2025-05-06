import pyautogui
import time

time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(0.3)
pyautogui.write('d')
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'v')

