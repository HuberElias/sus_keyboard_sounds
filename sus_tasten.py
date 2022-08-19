# imports
import os
import sys
from pygame import mixer
import keyboard
mixer.init()

# variables
channel = 0
is_paused = False


# functions
def set_hotkeys():
    keyboard.add_hotkey("p", handle_pause)

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
        keyboard.add_hotkey("p", handle_pause)
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

# def handle_s():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/s.mp3"))
# 
# def handle_a():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/a.mp3"))
# 
# def handle_h():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/h.mp3"))
# 
# def handle_m():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/m.mp3"))
# 
# def handle_e():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/e.mp3"))
# 
# def handle_space():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/space.mp3"))
# 
# def handle_d():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/d.mp3"))
# 
# def handle_r():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/r.mp3"))
# 
# def handle_f():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/f.mp3"))
# 
# def handle_n():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/n.mp3"))
# 
# def handle_enter():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/enter.mp3"))
# 
# def handle_delete():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/delete.mp3"))
# 
# def handle_b():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/b.mp3"))
# 
# def handle_w():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/w.mp3"))
# 
# def handle_k():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/k.mp3"))
# 
# def handle_entf():
#     global channel
#     if channel < 7:
#         channel += 1
#     else:
#         channel = 0
#     mixer.Channel(channel).play(mixer.Sound("./sounds/entf.mp3"))


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
