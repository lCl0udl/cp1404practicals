
FILENAME = "subject_data.txt"


def main():
    """Main function to load and display subject data."""
    subjects = load_subjects(FILENAME)
    display_subject_details(subjects)


def load_subjects(filename=FILENAME):
    """Read data from file and return as list of subject details."""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # Convert student count to integer
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """Display all subject details in formatted output."""
    for subject in subjects:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer:12} and has {student_count:3} students")


if __name__ == "__main__":
    main()