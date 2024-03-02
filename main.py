from configparser import ConfigParser
import os
import shutil
CONSOLE_WIDTH, CONSOLE_HEIGHT = shutil.get_terminal_size()

config = ConfigParser()
config.read("settings.ini")

def list_savefiles():
    pass

def start_new_game():
    pass

def start():
    welcome = "[Welcome to Depths"
    continue_message = "[C] - Continue Saved Game"
    new_game_message = "[N] - Start New Game"
    quit_message = "[Ctrl-C] - Quit"
    if config.getboolean("StartScreen", "ShowScriptVersion"):
        welcome += " v0.1.0"
    if config.getboolean("StartScreen", "ShowScriptCommit"):
        welcome += " (main, 2 Mar 2024)"
    welcome += "]"

    print(f'{welcome:=^{CONSOLE_WIDTH}}')

    print(f'{continue_message: ^{CONSOLE_WIDTH}}')
    print(f'{new_game_message: ^{CONSOLE_WIDTH}}')
    print(f'{quit_message: ^{CONSOLE_WIDTH}}')

    choice = input("> ").lower()
    while choice not in ('c', 'n'):
        if choice == "c":
            pass
        elif choice == "n":
            pass
        else:
            print(f"Invalid choice: {choice} - press enter to retry")
            print(f"[Error 1]")
            input("")

start()
