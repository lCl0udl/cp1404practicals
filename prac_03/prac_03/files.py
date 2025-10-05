"""
CP1404/CP5632 - Practical
File reading/writing practice
"""

# ----------------------------------------
# 1. Ask the user for their name and write it to name.txt
# ----------------------------------------
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# ----------------------------------------
# 2. Read the name from file and print a greeting
# ----------------------------------------
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# ----------------------------------------
# 3. Read first two numbers from numbers.txt and print their sum
# ----------------------------------------
with open("numbers.txt", "r") as in_file:
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
    result = num1 + num2
    print(result)

# ----------------------------------------
# 4. Calculate and print the total for all numbers in numbers.txt
# ----------------------------------------
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
