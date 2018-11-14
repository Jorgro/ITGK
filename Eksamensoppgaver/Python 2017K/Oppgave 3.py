#3a)
#show_display(content) liste av 6 elm, print ut til skjerm

def enter_line(prompt, length):
    switch = True

    while switch:
        user_input = str(input(prompt))
        if len(user_input) == length:
            switch = False
            break

        print(f"The text must be {length} characters long")

#3b)
def adjust_string(text, length):
    if len(text)>length:
        return text[:length]
    elif len(text)<length:
        return text.center(length)
    else:
        return text

print(adjust_string("This is a test on writing nicely and cooly!",30))
list = ['Hey', 'welcome', 'to', 'my', 'show', 'stupid']
empty = []
for i in list:
    empty.append(adjust_string(i, 30))

#3c)
def enter_line_smart(prompt, length):
    text = str(input(prompt))

    return adjust_string(text, length)

#3d)
def enter_show_text():
    empty = []
    for i in range(6):
        empty.append(enter_line_smart(f"Line {i+1}: ", 30))

    show_display(empty)

#3e)
def show_display(content):
 print()
 if len(content)==6 and len(content[0])==30:
     print("####################################")
     print("# #")
 for row in content:
     print('# '+row.upper()+" #")
     print("# #")
     print("####################################")
 else:
     print("Error: Wrong dimensions")
import time
def scroll_display(content, line):
    for i in range(len(content[line-1])):
        text = content[line-1][1:] + content[line-1][0]
        content[line-1] = text
        show_display(content)
        time.sleep(0.1)
#3f)
def display_from_file(filename):
    with open(filename, 'r') as file:
        text_list = file.readlines()

    for i in text_list:
        text_list[text_list.index(i)] = adjust_string(i.strip(), 30)

    for i in range(len(text_list)//6):
        try:
            show_display(text_list[i*6:6*(i+1)])
            time.sleep(10)
        except:
            show_display(text_list[i*6:])
            time.sleep(10)
