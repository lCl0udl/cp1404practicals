
def main():
    """Store emails and names in a dictionary."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ("", "y", "yes"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    # Display results
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a formatted name from an email address."""
    # Split before the @ symbol
    prefix = email.split("@")[0]
    # Replace '.' with spaces, then title case
    name_parts = prefix.replace('.', ' ').split()
    name = " ".join(name_parts).title()
    return name


if __name__ == "__main__":
    main()
