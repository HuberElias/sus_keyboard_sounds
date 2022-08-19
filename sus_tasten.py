# imports
import os
import sys
from pygame import mixer
import keyboard
mixer.init()

# variables
channel = 0
is_paused = False
pause_button = "pause"


# functions
def set_hotkeys():
    keyboard.add_hotkey(pause_button, handle_pause)

    keyboard.add_hotkey("s", lambda: handle_press("s"))
    keyboard.add_hotkey("a", lambda: handle_press("a"))
    keyboard.add_hotkey("h", lambda: handle_press("h"))
    keyboard.add_hotkey("m", lambda: handle_press("m"))
    keyboard.add_hotkey("e", lambda: handle_press("e"))
    keyboard.add_hotkey("space", lambda: handle_press("space"))
    keyboard.add_hotkey("d", lambda: handle_press("d"))
    keyboard.add_hotkey("r", lambda: handle_press("r"))
    keyboard.add_hotkey("f", lambda: handle_press("f"))
    keyboard.add_hotkey("n", lambda: handle_press("n"))
    keyboard.add_hotkey("enter", lambda: handle_press("enter"))
    keyboard.add_hotkey("backspace", lambda: handle_press("delete"))
    keyboard.add_hotkey("b", lambda: handle_press("b"))
    keyboard.add_hotkey("w", lambda: handle_press("w"))
    keyboard.add_hotkey("k", lambda: handle_press("k"))
    keyboard.add_hotkey("delete", lambda: handle_press("entf"))


def handle_pause():
    global channel
    global is_paused

    if not(is_paused):
        keyboard.unhook_all_hotkeys()
        keyboard.add_hotkey(pause_button, handle_pause)
        is_paused = not(is_paused)
    else:
        keyboard.unhook_all_hotkeys()
        set_hotkeys()
        is_paused = not(is_paused)

    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/pause.mp3"))


def handle_press(args):
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/"+args+".mp3"))


# main
os.system("CLS")
print("Soundboard is now activated...")
mixer.Channel(7).play(mixer.Sound("./sounds/phub.mp3"))
set_hotkeys()

while True:
    try:
        pass
    except KeyboardInterrupt:
        sys.exit()
