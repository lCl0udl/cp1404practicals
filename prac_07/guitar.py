
class Guitar:
    """Represent a guitar with name, year, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year

    def get_age(self, current_year):
        """Return the age of the guitar."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Determine if the guitar is vintage (50 years or older)."""
        return self.get_age(current_year) >= 50
