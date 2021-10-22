import time
import os
# Hi
# DATE: 22-5-2021
# DESCRIPTION: A whatsapp spammer based on the user input
# Please view the IMPORTANT_BEFORE_YOU_TRY txt so that you understand how this tool works
# PS: UNDER ANY SITUATIONS, PLEASE DO NOT DO THIS IF YOU DO NOT HAVE THE PERMISSION OF THE VICTIM

try:
    import colorama
    from colorama import Fore

except ModuleNotFoundError:
    print("colorama module has not been found")
    print(Fore.RED +"YOU NEED TO DOWNLOAD THIS MODULE")
    install = str(input("The module will be downloaded automatically, press Y to continue "))

    if install.upper() == "Y":
        os.system('pip install colorama')        
    else:
        exit()

try:
    import webbrowser

except ModuleNotFoundError:
    print("webbrowser module has not been found")
    print(Fore.RED +"YOU NEED TO DOWNLOAD THIS MODULE")
    install = str(input("The module will be downloaded automatically, press Y to continue "))

    if install.upper() == "Y":
        os.system('pip install webbrowser')        
    else:
        exit()

try:
    import pyautogui

except ModuleNotFoundError:
    print("pyautogui module has not been found")
    print(Fore.RED +"YOU NEED TO DOWNLOAD THIS MODULE")
    install = str(input("The module will be downloaded automatically, press Y to continue "))

    if install.upper() == "Y":
        os.system('pip install pyautogui')        
    else:
        exit()

try:
    import pyfiglet

except ModuleNotFoundError:
    print("pyfiglet module has not been found")
    print(Fore.RED +"YOU NEED TO DOWNLOAD THIS MODULE") 
    install = str(input("The module will be downloaded automatically, press Y to continue "))

    if install.upper() == "Y":
        os.system('pip install pyfiglet')        
    else:
        exit()

colorama.init(autoreset=True)
display = pyfiglet.figlet_format("Whatsapp Spammer", font = "slant")
print(Fore.LIGHTGREEN_EX + display)
print(Fore.LIGHTRED_EX + "Coded by @Adnanize")
print()

print("1 - Start") 
print("2 - Help")

print()

prompt = str(input("Please choose either 1 or 2: "))

def main():
    num_of_message = int(input("Please enter the number of times you want your message to be spammed: "))
    message = str(input("Please enter your message: "))

    webbrowser._browsers['chrome'] = None
    webbrowser.open("https://web.whatsapp.com")
    print()
    print(Fore.RED,"This operation will take time, make sure you select your victim, hover to the text field and press on it and wait ")
    time.sleep(30)

    for i in range(num_of_message):
        pyautogui.write(message)
        pyautogui.press("enter")

if prompt == "1":
    main()

elif prompt == "2":
    print()
    print("If you have any doubts, please read the IMPORTANT_BEFORE_YOU_TRY.txt")
    input("press Enter to read the IMPORTANT_BEFORE_YOU_TRY.txt ")
    f = open("IMPORTANT_BEFORE_YOU_TRY.txt", "r")
    print(f.read())
    print()
