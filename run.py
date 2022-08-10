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
question_row = []

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
    This function validates the users input from the main menu
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
    global question_number
    question_number = 1
    global sheet
    sheet = 'easy_questions'
    load_level()


def load_level():
    """
    This function loads the 'level' variables.
    There are three sheets in the worksheet file, one for easy questions, medium and hard.
    The difficulty of question picked depends on the players progress.
    """  
    # Loads the required sheet and counts the number of questions in the sheet.
    global loaded_sheet
    loaded_sheet = SHEET.worksheet(sheet)
    column1 = loaded_sheet.col_values(1)
    number_of_questions_in_sheet = len(column1)
    global question_numbers_array
    question_numbers_array = []
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
    print("Loading question . . .")
    #question ID represents the list index of each question number
    global question_numbers_array
    question_id = random.randrange(1, len(question_numbers_array))
    global question_row
    question_row = loaded_sheet.row_values(question_numbers_array[question_id])
    question_numbers_array.pop(question_id)
    clear_output(0.4)
    ask_question()
    
def display_question_amount(q_number):
    """
    This function takes the current question number as an arguement
    and returns the money associated with the question as a string.
    """
    match q_number:
        case 1:
            return '£100'
        case 2:
            return '£200'
        case 3:
            return '£300'
        case 4:
            return '£500'
        case 5:
            return '£1,000'
        case 6:
            return '£2,000'
        case 7:
            return '£5,000'
        case 8:
            return '£10,000'
        case 9:
            return '£20,000'
        case 10:
            return '£50,000'
        case 11:
            return '£75,000'
        case 12:
            return '£150,000'
        case 13:
            return '£250,000'
        case 14:
            return '£500,000'
        case 15:
            return '£1,000,000'

def ask_question():
    """
    This function outputs the question to the terminal and how much money the question is worth.
    It also asks the user to input their answer and then checks it.
    """
    question_money = display_question_amount(question_number)
    print(f"Question {question_number} for {question_money}:\n")
    print(f"{question_row[0]}\n")
    answers = assign_answers(question_row)
    correct_answer = answers[4]
    print(f"A: {answers[0]}\n")
    print(f"B: {answers[1]}\n")
    print(f"C: {answers[2]}\n")
    print(f"D: {answers[3]}\n")

    user_answer = input("Which is the correct answer A, B, C or D? :")
    user_answer = user_answer.capitalize()

    if user_answer == correct_answer:
        print(f"\nCorrect Answer")
        clear_output(1)
        level_check()
    else:
        print(f"\nIncorrect. You answered {user_answer},\nthe correct answer was {correct_answer}")
        clear_output(2)
        main_menu()

def assign_answers(row_input):
    """
    To make the game more interesting if it is played multiple times the position
    of the different changes. This function determines the letetr of the correct answer
    and then the letters of the incorrect answers.
    """
    correct_answer_position = random.randrange(1, 5)
    if correct_answer_position == 1:
        answers = [row_input[4], row_input[1], row_input[2], row_input[3], 'A']
    elif correct_answer_position == 2:
        answers = [row_input[1], row_input[4], row_input[2], row_input[3], 'B']
    elif correct_answer_position == 3:
        answers = [row_input[1], row_input[2], row_input[4], row_input[3], 'C']
    elif correct_answer_position == 4:
        answers = [row_input[1], row_input[2], row_input[3], row_input[4], 'D']
    return answers

def level_check():
    """
    This function is called when the user answers a question correctly. 
    This function determines whether to load a sheet with harder questions.
    If not necessary the next question is simply loaded by calling load_question()
    This function also increments the question number. 
    """
    global question_number
    question_number += 1
    if question_number == 16:
        game_complete()
    global sheet
    if question_number == 6:
        sheet = 'medium_questions'
        load_level()
    elif question_number == 11:
        sheet = 'hard_questions'
        load_level()
    else:
        load_question()

def game_won():
    """
    This function is called by the function level_check when 
    the variable question_number is equal to 16. This means the 
    player has commpleted the game and won £1,000,000
    """
    print(f"********************************\n*                              *\n* CONGRATULATIONS YOU HAVE WON *\n*       £1,000,000,000         *\n*                              *\n********************************\n")
    clear_output(2)
    main_menu()


#This calls the main_menu function and starts the game when run.py is run.
main_menu()