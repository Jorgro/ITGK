import pyautogui, time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

width, height = pyautogui.size()

# for i in range(10):
#       pyautogui.moveTo(100, 100)
#       pyautogui.moveTo(200, 100)
#       pyautogui.moveTo(200, 200)
#       pyautogui.moveTo(100, 200)


# while True:
#     pyautogui.click(453, 413)

def commentAfterDelay():
    pyautogui.click(5, 59)
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line')
    # time.sleep(2)
    pyautogui.dragRel(8, 0)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(200, 60)
    pyautogui.press('return')
    pyautogui.hotkey('ctrl', 'v')
commentAfterDelay()
