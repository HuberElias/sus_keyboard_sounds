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
    mixer.Channel(channel).play(mixer.Sound("./sounds/sus-sound-effect-amogus-meme.mp3"))

def handle_a():
    global channel
    if channel < 7:
        channel += 1
    else:
        channel = 0
    mixer.Channel(channel).play(mixer.Sound("./sounds/aaaauuughhhh-meme-sound-effect.mp3"))

# hotkeys
keyboard.add_hotkey("s", handle_s)
keyboard.add_hotkey("a", handle_a)




# main
while True:
    pass
