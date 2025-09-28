"""
CP1404/CP5632 - Practical
Program to determine score status with functions
"""


def main():
    """Main function to determine score status."""
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)


def determine_score_status(score):
    """Determine and return the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()