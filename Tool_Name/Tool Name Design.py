from pystyle import *
import pyfiglet
import keyboard
import atexit
import os
import time as t

enter = str(input('enter your name: '))
name = pyfiglet.figlet_format(f'welcome {enter}')
t.sleep(2)
os.system('clear')
Write.Print(name,Colors.red_to_green,interval=0.01)
t.sleep(0.75)
os.system('clear')
t.sleep(0.75)
os.system('clear')
text = 'Designed by Lord S'
design = pyfiglet.figlet_format(text)
Write.Print(design,Colors.red_to_blue,interval=0.01)
#print(Box.Lines('BY: LORD S'))
# Under that shape, place your script 

