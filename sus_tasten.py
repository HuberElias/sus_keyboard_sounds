# imports
from pygame import mixer
import keyboard
mixer.init()

# variables
channel = 0

# functions
def handle_s():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/s.mp3"))

def handle_a():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/a.mp3"))

def handle_h():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/h.mp3"))

def handle_m():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/m.mp3"))

def handle_e():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/e.mp3"))

def handle_space():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/space.mp3"))

def handle_d():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/d.mp3"))

def handle_r():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/r.mp3"))

def handle_f():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/f.mp3"))

def handle_n():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/n.mp3"))

def handle_enter():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/enter.mp3"))

def handle_delete():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/delete.mp3"))


# hotkeys
keyboard.add_hotkey("s", handle_s)
keyboard.add_hotkey("a", handle_a)
keyboard.add_hotkey("h", handle_h)
keyboard.add_hotkey("m", handle_m)
keyboard.add_hotkey("e", handle_e)
keyboard.add_hotkey("space", handle_space)
keyboard.add_hotkey("d", handle_d)
keyboard.add_hotkey("r", handle_r)
keyboard.add_hotkey("f", handle_f)
keyboard.add_hotkey("n", handle_n)
keyboard.add_hotkey("enter", handle_enter)
keyboard.add_hotkey("backspace", handle_delete)
#sos = keyboard._listener



# main
while True:
    #sos.listen()
    pass
