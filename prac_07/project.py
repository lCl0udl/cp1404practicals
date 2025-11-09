from datetime import datetime

class Project:
    """Represent a project with details like name, start date, priority, cost, and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Allow sorting by priority, then start date."""
        if self.priority == other.priority:
            return self.start_date < other.start_date
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is 100% complete."""
        return self.completion_percentage == 100
