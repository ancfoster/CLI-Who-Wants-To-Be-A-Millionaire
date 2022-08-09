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
sheet = ''

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
    """
    This function displays the main menu when called. Contains a while loop that displays the menu
    until a valid input has been entered by the user.
    """
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
    """
    This function loads the 'level' variables.
    There are three sheets in the worksheet file, one for easy questions, medium and hard.
    The difficulty of question picked depends on the players progress.
    """
    if level_number < 6:
        sheet = 'easy_questions'
    elif level_number < 11:
        sheet = 'medium_questions'
    elif level_number < 16:
        sheet = 'hard_questions'
    # Loads the required sheet and counts the number of questions.
    loaded_sheet = SHEET.worksheet(sheet)
    column1 = loaded_sheet.col_values(1)
    number_of_questions_in_sheet = len(column1)
    question_array_counter = 1
    # Creates an array of numbers based on the number of questions in the sheet.
    while question_array_counter < number_of_questions_in_sheet:
        question_numbers_array.append(question_array_counter)
        question_array_counter += 1
    load_question()

def load_question():
    """
    This function randomly generates a number with the length of the question numbers array.
    This number corresponds to a row in a question sheet. 
    A row contains a written question and four answers. The last answer is always the correct one.
    """

main_menu()