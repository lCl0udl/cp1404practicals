

class ProgrammingLanguage:
    """Represent a programming language with some simple properties."""

    def __init__(self, name, typing, reflection, year):

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language uses dynamic typing.

        This method takes no parameters other than self and uses the object's
        stored data to answer the question.
        """
        return str(self.typing).strip().lower() == "dynamic"

    def __str__(self):

        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"