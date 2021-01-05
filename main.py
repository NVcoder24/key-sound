try:
    from threading import Thread
    from playsound import playsound
    from pynput.keyboard import Listener
    from pynput import keyboard
    from random import choice
    from ctypes import windll
    import os
except ImportError as e:
    print(f"libraries error: {e}\ninstall this library to continue")
    input("press enter to exit...")
    exit()

def show_tip():
    windll.user32.MessageBoxW(0, "If you want to exit: press shift + \\\n* key sound by NVcoder24", "Key sound Pro Tips!", 0)

current = set()

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='\\')},
    {keyboard.Key.shift, keyboard.KeyCode(char='|')}
]

def on_press(key):
    Thread(target=a).start()
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            exit()

def a():
    playsound(f'key{choice(range(1,6))}.mp3')

def run():
    try:
        with Listener(on_press=on_press) as listener:
            listener.join()
    except UnicodeDecodeError as e:
         print(f"error: {e}")

if __name__ == "__main__":
    Thread(target=show_tip).start()
    Thread(target=run).start()
