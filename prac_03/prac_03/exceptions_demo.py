"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# ✅ Q1: ValueError occurs when the user enters something that is NOT an integer
# (e.g. a letter, word, or symbol like "abc" or "#").
# ✅ Q2: ZeroDivisionError occurs when the user enters 0 as the denominator.
# ✅ Q3: To avoid ZeroDivisionError, we can add input validation to ensure
#       the denominator is not 0 before performing the division.

finished = False
while not finished:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator (not zero): "))
        if denominator == 0:
            print("Denominator cannot be zero. Please try again.")
            continue
        fraction = numerator / denominator
        print(f"The result is {fraction}")
        finished = True
    except ValueError:
        print("Numerator and denominator must be valid integers!")

print("Finished.")
