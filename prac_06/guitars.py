
def main():
    guitars = []

    print("My guitars!")

    while True:
        name = input("Name: ").strip()
        if not name:
            break
        try:
            year = int(input("Year: ").strip())
        except ValueError:
            print("Invalid year — setting to 0")
            year = 0
        try:
            cost = float(input("Cost: ").strip())
        except ValueError:
            print("Invalid cost — setting to 0.0")
            cost = 0.0

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

    # If you want to test quickly without typing input, uncomment the lines below:
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars were entered.")


if __name__ == '__main__':
    main()