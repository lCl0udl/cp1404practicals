from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    in_file = open('languages.csv', 'r')
    # Consume header
    in_file.readline()

    for line in in_file:
        parts = line.strip().split(',')
        # Reflection and PointerArithmetic are stored as strings (Yes/No)
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        languages.append(language)

    in_file.close()

    for language in languages:
        print(language)


if __name__ == "__main__":
    main()
