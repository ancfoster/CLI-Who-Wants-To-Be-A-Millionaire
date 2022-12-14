from operator import add
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import time
import random
from pip import main


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('who_wants_game')

# Global variables
question_number = 1
question_numbers_array = []
player_name = ''
sheet = ''
question_row = []


def clear_output(seconds):
    """
    This function clears the terminal contents after a certain number of
    seconds the arguement (seconds) determines how long until the terminal
    should be cleared.
    """
    current_time = time.time()
    while True:
        # Using time.sleep() greatly reduces CPU performance
        # sleep for 250 milliseconds - snippet from StackOverflow user Antony
        # https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time
        time.sleep(0.25)
        if time.time() >= current_time + seconds:
            print("\033c")  # Code snippet from StackOverflow user Alex Hawking
            # https://stackoverflow.com/users/9868018/alex-hawking
            break


def main_menu():
    """
    This function displays the main menu when called. Contains a while loop
    that displays the menu until a valid input has been entered by the user.
    """
    print("Welcome to CLI Who wants to be a Millionaire")
    clear_output(1.5)
    while True:
        print(f'''Main Menu\n
Input: 'New' to start a new game
Input 'How to' for game instructions
Input 'Scores' to see scores\n''')
        main_menu_input = input("Enter input: ")
        main_menu_input = main_menu_input.lower()
        if validate_main_menu_input(main_menu_input):
            break
    if main_menu_input == 'new':
        set_user()
    elif main_menu_input == 'how to':
        how_to()
    elif main_menu_input == 'scores':
        scores()


def validate_main_menu_input(input):
    """
    This function validates the users input from the main menu
    """
    if input == 'new':
        return True
    elif input == 'how to':
        return True
    elif input == 'scores':
        return True
    else:
        clear_output(0)
        print(f'''Ivalid input, you entered {input}
Please try again.\n''')
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
    global milestone_amount
    milestone_amount = 0
    sheet = 'easy_questions'
    load_level()


def load_level():
    """
    This function loads the 'level' variables.
    There are three sheets in the worksheet file, one for easy questions,
    medium and hard. The difficulty of question picked depends on the
    players progress.
    """
    # Loads the required sheet and counts the number of questions in the sheet.
    global loaded_sheet
    loaded_sheet = SHEET.worksheet(sheet)
    column1 = loaded_sheet.col_values(1)
    number_of_questions_in_sheet = len(column1)
    global question_numbers_array
    question_numbers_array = []
    question_array_counter = 1
    # Creates an array of numbers based on the number of questions in the sheet
    while question_array_counter < number_of_questions_in_sheet:
        question_numbers_array.append(question_array_counter)
        question_array_counter += 1
    load_question()


def load_question():
    """
    This function randomly generates a number with the length of the question
    numbers array. This number corresponds to a row in a question sheet.
    A row contains a written question and four answers. The last answer is
    always the correct one.
    """
    print("Loading question . . .")
    # question ID represents the list index of each question number
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
        case 0:
            return '??0'
        case 1:
            return '??100'
        case 2:
            return '??200'
        case 3:
            return '??300'
        case 4:
            return '??500'
        case 5:
            return '??1,000'
        case 6:
            return '??2,000'
        case 7:
            return '??5,000'
        case 8:
            return '??10,000'
        case 9:
            return '??20,000'
        case 10:
            return '??50,000'
        case 11:
            return '??75,000'
        case 12:
            return '??150,000'
        case 13:
            return '??250,000'
        case 14:
            return '??500,000'
        case 15:
            return '??1,000,000'


def ask_question():
    """
    This function outputs the question to the terminal and how much money the
    question is worth. It also asks the user to input their answer and then
    checks it. The function also allows users to 'walk away' if they do not
    know the answer.
    """
    output_question()
    # Validates input
    while True:
        global user_answer
        user_answer = input("Which is the correct answer A, B, C or D?: \n")
        user_answer = user_answer.lower()
        if validate_answer(user_answer):
            break
    check_answer()


def output_question():
    """
    This function is responsible for printing the question to the terminal.
    It calculates how much money the player can walk away with and populates
    the possible answers between the letters A B C D. It also globally sets
    the correct answer variable which is used by other functions.
    """
    # This calculates the arguement for display_question_amount.
    # It is the current question number -1
    global walk_away_with_arg
    walk_away_with_arg = question_number - 1
    # Walk away with is the mounr of money the player can walk away with and is
    # based on the last correctly answered question.
    global walk_away_with
    walk_away_with = display_question_amount(walk_away_with_arg)
    question_money = display_question_amount(question_number)
    answers = assign_answers(question_row)
    global correct_answer
    correct_answer = answers[4]
    print(f'''Question {question_number} for {question_money}:
\n{question_row[0]}
\nA: {answers[0]}
\nB: {answers[1]}
\nC: {answers[2]}
\nD: {answers[3]}\n''')
    # Player cannot 'walk away' with less than ??1k, question number must be > 5
    if question_number > 5:
        print(f'''If you are unsure you may walk away with {walk_away_with}
by entering 'walk' instead of an answer.\n''')


def validate_answer(user_answer):
    """
    This function checks the player's inputted answer. If the input is valid
    True will be returned, if not False will be returned along with the
    incorrect user input.
    """
    match user_answer:
        case 'a':
            return True
        case 'b':
            return True
        case 'c':
            return True
        case 'd':
            return True
        case 'walk':
            return True
        case _:
            clear_output(0)
            print(f'Invalid input, you entered {user_answer}\n')
            output_question()
            return False


def check_answer():
    """
    This function checks the users answer and then determines
    what should happen next in the game. If the answer is correct
    the user can progress and what the user will be able to 'bank'
    if they have reached the next game mileston.
    If the user walked away the game will then output how much money
    the user has won.
    If the user answered the question incorectly the game will
    calculate if they won any money or how much.
    This function also calls the add_to_scores function and passes
    in a number between 0-15 as the arguement, this number corresponds
    to a prize amount.
    """
    if user_answer == correct_answer:
        print(f"\nCorrect Answer")
        # The milestone checks whether the correct answer means the user gets
        # to 'bank' a milestone amount
        milestone()
        clear_output(1)
        level_check()
    elif user_answer == 'walk':
        clear_output(0)
        print(f'''Thank you for playing {player_name},
you have walked away with {walk_away_with}.''')
        print('Saving your score . . .')
        # Calls function that saves player score. The arguement is the question
        # number of the last correctly answered question
        add_to_scores(walk_away_with_arg)
        print(f'Score successfully saved.\n')
        input("Press enter to return to the main menu")
        clear_output(0)
        main_menu()
    else:
        if question_number < 6:
            leave_with_incorrect_answer_amount = '??0'
        else:
            leave_with_incorrect_answer_amount = display_question_amount(milestone_amount)  # noqa
        print(f'''\nIncorrect. You answered {user_answer.capitalize()},
the correct answer was {correct_answer.capitalize()}.\n
You leave with {leave_with_incorrect_answer_amount}''')
        # Calls function that saves player score.
        # Arguement is question number of the last correctly answered question
        if question_number < 6:
            add_to_scores(0)
        else:
            add_to_scores(milestone_amount)
        print(f'\nSaving your score . . .')
        print(f'\nScore saved.')
        input('Press enter to return to the main menu')
        clear_output(0)
        main_menu()


def assign_answers(row_input):
    """
    To make the game more interesting if it is played multiple times the
    position of the different changes. This function determines the letter
    of the correct answer and then the letters of the incorrect answers.
    """
    correct_answer_position = random.randrange(1, 5)
    if correct_answer_position == 1:
        answers = [row_input[4], row_input[1], row_input[2], row_input[3], 'a']
    elif correct_answer_position == 2:
        answers = [row_input[1], row_input[4], row_input[2], row_input[3], 'b']
    elif correct_answer_position == 3:
        answers = [row_input[1], row_input[2], row_input[4], row_input[3], 'c']
    elif correct_answer_position == 4:
        answers = [row_input[1], row_input[2], row_input[3], row_input[4], 'd']
    return answers


def level_check():
    """
    This function is called when the user answers a question correctly.
    This function determines whether to load a sheet with harder questions.
    If not necessary the next question is simply loaded by calling
    load_question() This function also increments the question number.
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


def game_complete():
    """
    This function is called by the function level_check when
    the variable question_number is equal to 16. This means the
    player has commpleted the game and won ??1,000,000
    """
    print(f'''********************************
*                              *
* CONGRATULATIONS YOU HAVE WON *
*        ??1,000,000,000        *
*                              *
********************************''')
    print(f"\nSaving score . . .")
    add_to_scores(15)
    print(f"Score saved, thank you for playing\n")
    input("Press enter to return to the main menu")
    main_menu()


def how_to():
    clear_output(0)
    print(f"How to play CLI Who Wants to Be A Millionaire\n")
    print(f"_____________________________________________\n")
    print(f'''This game is a CLI interpretation of the UK quiz
game show of the same name.

The objective is to win ??1,000,000 by answer 15 multiple choice questions
correctly. These questions are from a variety of general knowledge topics.
The questions will get harder as the game progresses.
The questions are valued at progressively higher sums of money.\n''')
    input("Press Enter to continue reading . . .")
    clear_output(0)
    print('''
The questions answers are labelled A, B, C and D. To answer a question
simply input the corresponding letter into the terminal and press the
enter key. During the game there are two monetary milestones, ??1,000
and ??50,000. If you answer a question incorrectly, but passed a
milestone during the game that milestone will be your score.

Game developed by Alexander Foster.
''')
    while True:
        print('''Navigate back Main Menu by entering "menu"
or start a new game by entering "new"''')
        how_to_input = input("\nEnter input: ")
        how_to_input = how_to_input.lower()
        if validate_how_to_play(how_to_input):
            break
    clear_output(0)
    if how_to_input == 'menu':
        main_menu()
    elif how_to_input == 'new':
        set_user()


def validate_how_to_play(input):
    """
    This function validates the users input from the main menu
    """
    if input == 'new':
        return True
    elif input == 'menu':
        return True
    else:
        clear_output(0)
        print(f"Ivalid input, you entered {input}\n")
        return False


def set_user():
    """
    This function asks for and sets the player's name.
    The name is validated to be between 3 and 15 characters
    in length.
    """
    clear_output(0)
    print('''Please enter your player name,
which must be at least 3 characters long and no more than 15.\n''')
    while True:
        p_name = input("Input player name: \n")
        if validate_player_name(p_name):
            break
    global player_name
    player_name = p_name
    new_game()


def validate_player_name(name):
    """
    This function validated the length of the inputted player name.
    If the criteria have been met True is returned, if not false is returned.

    """
    name_len = len(name)
    if name_len > 2 and name_len < 16 and name.isalpha():
        return True
    else:
        clear_output(0)
        print(f'''Enter a valid player name.
This must be at least 3 but no more than 15 characters
in length and be made up of letters only.\n
You entered:
{name}\n''')


def add_to_scores(score_to_save):
    """
    This function writes the player name, game date & score (cash amount)
    to the sheet named 'scores' in the Google worksheet.
    """
    # Init empty list
    score_data = []
    # Returns a string containing the cash score amount
    score_save = display_question_amount(score_to_save)
    # Current date
    current_date = datetime.now()
    # Convert date into required format dd-mm-yyyy
    save_date = current_date.strftime("%d-%m-%Y")
    # Append the three values to list score_data
    score_data.append(player_name)
    score_data.append(save_date)
    score_data.append(score_save)
    SHEET.worksheet('scores').append_row(score_data)
    return


def milestone():
    """
    This function calculates if a game milestone
    has been reached and returns it when called.
    """
    global milestone_amount
    match question_number:
        case 5:
            milestone_amount = 5
            return
        case 10:
            milestone_amount = 10
            return
        case _:
            return


def scores():
    """
    This function retrieves the most recent scores from the sheet in the
    Google worksheet called 'scores'
    """
    clear_output(0)
    print('''Scores
________________________

Loading most recent scores . . .
''')
    scores_col = []
    scores_col = SHEET.worksheet('scores').col_values(1)

    number_of_scores = len(scores_col)
    # If there are less than 10 records only get the records that are available
    if number_of_scores < 10:
        score_records_to_get = number_of_scores
    else:
        # Default action is to get and print out the 10 most recent scores
        score_records_to_get = 10
    score_records_all = []
    record_count = score_records_to_get
    while record_count > 0:
        """ Prints scores newest to oldest by taking the number_of_scores and -1
        with each iteration """
        score_record = SHEET.worksheet('scores').row_values(number_of_scores)
        score_records_all.append(score_record)
        record_count -= 1
        number_of_scores -= 1
    clear_output(0)
    print('''Scores
________________________

''')
    for record in score_records_all:
        print(f'''Player {record[0]} played and won {record[2]} on {record[1]}
        ''')
    # This section of the function returns the user to the main menu
    input('Press enter to return to the main menu')
    clear_output(0)
    main_menu()


# This calls the main_menu function and starts the game when run.py is run.
main_menu()
