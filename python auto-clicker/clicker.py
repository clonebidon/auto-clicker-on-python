import keyboard
import mouse
import time

clicker = False

def toggle_auto_clicker():
    global clicker
    clicker = not clicker

keyboard.add_hotkey("`", toggle_auto_clicker)
while True:
    if clicker:
        mouse.click(button='left')
        time.sleep(0.5)
