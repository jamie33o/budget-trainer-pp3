import sys  # System-specific parameters and functions
import time  # provides functions for handling time-related tasks
import os



def slow_print_effect(text, delay=0.04):
    """
    slow Typing effect for print statements
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)


def input_validator(expected_type, input_text):
    """checks if input valid depending on expected type if its 
    string or int and returns the input if there is no error"""
    input_value = ""
    if expected_type == "letter":
        while True:
                input_value = input(f"\n {input_text}\n")
                if input_value.upper() in ["Y", "N"]:
                       clear_terminal()
                       break  # Exit the loop if the input is a valid string
                else: 
                    slow_print_effect("Wrong input! Please enter text.")
    elif expected_type == "number":
        while True:
                try:
                    input_value = int(input(f"\n{input_text}\n"))
                    break  # Exit the loop if the input is a valid integer
                except ValueError:
                    slow_print_effect("Wrong input! Please enter a whole number.")
    elif expected_type == "username": 
        while True:
            input_value = input(f"""\n Please enter username,
            \n if you have used this website before please use the same username...
            \nIt must be 5 to 10 characters long\n""")
            if len(input_value) in range(5,11):
                    clear_terminal()
                    break  # Exit the loop if the input is a valid string
            else: 
                slow_print_effect("Wrong input! Please enter text.")
    return input_value


def clear_terminal():
    """
    function to clear terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear') 