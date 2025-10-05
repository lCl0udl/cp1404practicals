"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: set flag to True so the loop ends when valid input is given
    except ValueError:  # TODO: catch the specific exception for invalid int conversion
        print("Please enter a valid integer.")
print("Valid result is:", result)
