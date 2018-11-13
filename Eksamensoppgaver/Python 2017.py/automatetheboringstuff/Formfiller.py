import pyautogui, time
nameField = (600, 315)
submitButton = (708, 820)
submitButtonColor = (76, 142, 251)
submitAnotherLink = (826, 228)
pyautogui.PAUSE = 0.5

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the
            'break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public
            'trust. Uphold the law.'}
           ]
try:
    for person in formData:
        print('>>> 5 second pause to interrupt script (press CTRL-C) <<<')
        time.sleep(5)
        while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1],
       submitButtonColor):
           time.sleep(0.5)



except KeyboardInterrupt:
    print('\nDone')
