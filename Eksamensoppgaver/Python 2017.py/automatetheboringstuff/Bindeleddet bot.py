import datetime
import time
import pyautogui
import webbrowser


bindeleddetdato = datetime.datetime(2018, 10, 18, 12, 0, 0)
while datetime.datetime.now() < bindeleddetdato:
    time.sleep(1)
webbrowser.open_new('https://www.bindeleddet.no/events/2078')
pyautogui.click(662, 1054)
pyautogui.click(476, 611)
