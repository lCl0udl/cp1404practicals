
MIN_LENGTH = 8


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    while True:
        password = input("Enter password: ")
        if len(password) >= MIN_LENGTH:
            return password
        else:
            print(f"Password must be at least {MIN_LENGTH} characters long")


def print_asterisks(password):
    print('*' * len(password))


if __name__ == "__main__":
    main()