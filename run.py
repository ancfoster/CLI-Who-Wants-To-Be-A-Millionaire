import gspread
from google.oauth2.service_account import Credentials
import time
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('who_wants_game')

#Global variables
question_number = 1
question_numbers_array = []
player_name = ''

def clear_output(seconds):
    """
    This function clears the terminal contents after a certain number of seconds.
    The arguement (seconds) determines how long until the terminal should be cleared.
    """
    current_time = time.time()
    while True:
        time.sleep(0.25) # sleep for 250 milliseconds
        if time.time() >= current_time + seconds:
            print("\033c") # Code snippet from StackOverflow user Alex Hawking https://stackoverflow.com/users/9868018/alex-hawking
            break


def main_menu():
    print("Welcome to CLI Who wants to be a Millionaire")
    clear_output(1.5)

    while True:
        print("Main Menu\n")
        print("Input: 'New' to start a new game\nInput 'How to' for game instructions")

        main_menu_input = input("Enter input: ")
        main_menu_input = main_menu_input.lower()
        
        if validate_main_menu_input(main_menu_input):
            break

    if main_menu_input == 'new':
        new_game()
    elif main_menu_input == 'how to':
        print('how to')

def validate_main_menu_input(input):
    """
    try:
    """
    if input == 'new':
        return True
    elif input == 'how to':
        return True
    else:
        print(f"Ivalid input, you entered {input}")
        return False

def new_game():
    """
    This function prepares the program for a new game. 
    Resets variables if player has already played during run time.
    """
    clear_output(0)
    print("Loading New Game . . .")
    clear_output(1)
    question_number = 1
    question_numbers_array = []
    load_level(1)

def load_level(level_number):
    if level_number < 6:
        sheet = 'easy'
    elif level_number < 11:
        sheet = 'medium'
    elif level_number < 16:
        sheet = 'hard'
    print(sheet)


main_menu()