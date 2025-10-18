
FILENAME = "wimbledon.csv"


def main():
    
    records = load_data(FILENAME)
    champion_to_wins, countries = process_data(records)
    display_results(champion_to_wins, countries)


def load_data(filename):

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header line
        records = [line.strip().split(",") for line in in_file]
    return records


def process_data(records):

    champion_to_wins = {}
    countries = set()

    for record in records:
        country = record[1]
        champion = record[2]

        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1

    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display champions with win counts and list of countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    print()
    sorted_countries = sorted(countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


if __name__ == "__main__":
    main()
