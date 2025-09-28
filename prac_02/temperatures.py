"""
CP1404/CP5632 - Practical
Program for temperature conversion with functions
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Main function to run temperature conversion program."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit()
        elif choice == "F":
            fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit():
    """Convert Celsius temperature to Fahrenheit."""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def fahrenheit_to_celsius():
    """Convert Fahrenheit temperature to Celsius."""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


if __name__ == "__main__":
    main()