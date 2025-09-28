"""
CP1404/CP5632 - Practical
Menu-driven program to work with scores
"""

from score import determine_score_status


def main():
    """Main function for the score menu program."""
    score = get_valid_score()
    choice = display_menu()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_status(score)
            print(f"Result: {result}")
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        choice = display_menu()
    print("Farewell!")


def display_menu():
    """Display menu and get user choice."""
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    choice = input(">>> ").upper()
    return choice


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


if __name__ == "__main__":
    main()
