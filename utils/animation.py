import os
import time
import platform

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def wait(seconds=2):
    time.sleep(seconds)

def skull_bump_animation():
    frames = [
        "    (-_-)",
        "     (-_-) .",
        "      (-_-) ..",
        "       (-_-) ...",
        "        (-_-)....",
        "         (-_-).....",
        "          (o_o) *sniff*",
        "          (o_o)!!"
    ]
    for frame in frames:
        clear()
        print("\n\n\n\n\n")
        print(frame.center(80))
        time.sleep(0.2)
