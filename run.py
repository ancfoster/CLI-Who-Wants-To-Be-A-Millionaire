import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.jpipson')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('who_wants_game')

#Global variables
question_count = 1
question_numbers_array = []
player_name = ''

def clear_output():
    print("\033c")
    # Code snippet from StackOverflow user Alex Hawking https://stackoverflow.com/users/9868018/alex-hawking

def main_menu():
    print("HEllo")
  

def main():
    """
    Main function
    """
    main_menu()