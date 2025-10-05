
import random

# line 1: random.randint(5, 20)
# Returns a random integer between 5 and 20 (both inclusive)
print(random.randint(5, 20))
# Smallest possible number: 5
# Largest possible number: 20

# line 2: random.randrange(3, 10, 2)
# Returns a random number from range(start=3, stop=10, step=2)
# That means possible values: 3, 5, 7, 9
print(random.randrange(3, 10, 2))
# Smallest possible number: 3
# Largest possible number: 9
# Could line 2 have produced a 4? No, because step=2 skips even numbers (3,5,7,9 only)

# line 3: random.uniform(2.5, 5.5)
# Returns a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))
# Smallest possible number: 2.5
# Largest possible number: 5.5

# Finally, produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)
