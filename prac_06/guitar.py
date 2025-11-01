from datetime import date


class Guitar:
    """Represent a guitar with name, year and cost."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        # Use comma thousands separator and two decimal places
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the guitar's age in years based on the current year."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 years old or older."""
        return self.get_age() >= 50