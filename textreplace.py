# for this to work, you need xdotool. You can't get it on Windows.
# for mac, just 'brew install xdotool'. For linux, just sudo {package-manager} install xdotool.
# for Ubuntu/Debian/Linux mint the package manager is apt-get, for Fedora it's yum, etc.
import os
import keyboard
# stores all the keys we've hit
BUFFER = ""
# stores the special character we use for commands to text replace.
special_char = ''
# called whenever a key is typed. Appends key to buffer, 
# removes anything from the buffer except stuff that begins
# with the special character.
def callback(e):
    global BUFFER
    global special_char
    if e.name == "backspace":
        BUFFER = BUFFER[:-1]
    else:
        BUFFER += e.name
        while BUFFER != "" and BUFFER[0] != special_char:
            BUFFER = BUFFER[1:]

# parse our text replacement dictionary. We assume that the special character for commands is
# the first character on the first line, and that the remaining lines are 'key{SPACE}value' pairs.
d = {}
first = True
largestKey = 0
with open("config") as f:
    for line in f:
        if first:
            special_char = line[0]
            first = False
        else:
            (key, val) = line.split()
            if len(key) > largestKey:
                largestKey = len(key)
            d[key] = val
        
# whenever a command is detected, delete the command's text using backspace 
# and replace it with the appropriate text that we got from our dictionary.
keyboard.on_release(callback)
while True:
    cur = BUFFER
    if cur[1:] in d:
        for _ in cur:
            os.system("xdotool key BackSpace")    
        os.system("xdotool type \""+ d[cur[1:]] +"\" ")
        BUFFER = ""
    elif len(BUFFER[1:]) > largestKey + 1:
        BUFFER = ""