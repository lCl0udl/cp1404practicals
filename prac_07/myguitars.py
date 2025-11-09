
from guitar import Guitar

def main():
    """Read guitars from file, allow adding new ones, then save back."""
    guitars = load_guitars("guitars.csv")

    print("These are the guitars we have:")
    display_guitars(guitars)

    print("\nNow let's add some new guitars!")
    guitars = add_new_guitars(guitars)

    # Sort the list by year (thanks to __lt__)
    guitars.sort()

    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)

    # Save the updated list to file
    save_guitars("guitars.csv", guitars)
    print("\nYour guitars have been saved to guitars.csv")


def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display all guitars neatly."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def add_new_guitars(guitars):
    """Ask the user for new guitars and add them to the list."""
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(filename, guitars):
    """Write all guitars to the CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
