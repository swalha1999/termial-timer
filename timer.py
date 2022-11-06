import pyfiglet
import time
import os
import shutil
import sys

def print_centered(text):
    #str.center( x ) is a method that returns a copy of the string centered in a string of length x
    
    centerd_text = [x.center(shutil.get_terminal_size().columns) for x in text.split("\n")]
    
    for line in centerd_text:
        print(line)

def timer():
    try:
        if sys.argv[1] == "fonts":
            print(*pyfiglet.FigletFont.getFonts(), sep = "\n")
            return
        get_time = int(sys.argv[1])
        font = 'standard'
        if len(sys.argv) > 2:
            font = sys.argv[2]
    
        while get_time:
            os.system('clear')
            mins, secs = 0 , 0
            mins, secs = divmod(get_time, 60)
            timer = '{:02d} : {:02d}'.format(mins, secs)
            assciArt = pyfiglet.figlet_format(timer, font=font, width= 1000)
            print_centered(assciArt) 
            time.sleep(1)
            get_time -= 1

        os.system('clear')

        print_centered(pyfiglet.figlet_format("T i m e 's    u p ! "))
    except:
        print("usage: timer.py <time in seconds> <font>")

    
    

timer()

