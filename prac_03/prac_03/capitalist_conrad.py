"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.

The price starts off at $10.00, and at the end of every day there is:
- a 50% chance it increases by 0 to 17.5%
- a 50% chance it decreases by 0 to 5%

The simulation ends if the price rises above $100 or falls below $1.
The price is displayed to the nearest cent and written to an output file.
"""

import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "capitalist_conrad_output.txt"

# Initial setup
out_file = open(FILENAME, 'w')
price = INITIAL_PRICE
number_of_days = 0

print(f"Starting price: ${price:,.2f}")
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulation loop
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1

    # Randomly decide if the price goes up or down
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Apply the change
    price *= (1 + price_change)

    # Print results to screen and file
    print(f"On day {number_of_days} price is: ${price:,.2f}")
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()
