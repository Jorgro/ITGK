import webbrowser, time, pyautogui 
kahoot_id = '8311259'

for i in range(20):
    webbrowser.open_new('https://www.kahoot.it')
    time.sleep(0.5)
    pyautogui.click(760, 443)
    pyautogui.doubleClick(760, 443)
    pyautogui.typewrite(kahoot_id)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.doubleClick(760, 500)
    pyautogui.typewrite('I AM BOT :) '+ str(i))
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(300, 600)
#1150 258 blå
#1150 600 grønn
#300 200 rød
#300 600 gul
