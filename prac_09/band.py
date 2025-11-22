
class Band:
    """Represent a band consisting of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their instrument."""
        return "\n".join(musician.play() for musician in self.musicians)

    def __str__(self):
        """Return a string representation of the band."""
        musicians_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"