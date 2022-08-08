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
question_count = 1
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
    print("""Welcome to \nWho wants to be a Millionaire""")
    clear_output(5)
    print("Main Menu")
    print("Enter: 'New' to start a new game,/nor enter 'Scores' to see scores/nor 'How to Play' for game instructions")

def main():
    """
    Main function
    """
    main_menu()

main()