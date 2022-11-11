from PIL import ImageGrab
import pyautogui
import pyautogui as pag
import pyperclip
import time
import webbrowser

webbrowser.open_new_tab("https://www.google.com/")
time.sleep(1)
pyautogui.press("shift")
pyperclip.copy("平泉町 観光")
pyautogui.hotkey("command", "v")
pyautogui.hotkey("\n")
time.sleep(1)
screenshot = ImageGrab.grab()
time.sleep(1)
screenshot.save("screenshot.png")
# pyautogui.hotkey("command", "shift", "3")
