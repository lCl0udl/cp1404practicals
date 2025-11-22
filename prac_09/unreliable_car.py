
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Represent an unreliable car that may fail to drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability  # 0 to 100 float

    def drive(self, distance):
        """Drive the car only if a random number is below reliability percentage."""
        random_number = random.uniform(0, 100)
        if random_number >= self.reliability:

            distance = 0

        distance_driven = super().drive(distance)
        return distance_driven

    def __str__(self):
        """Return string representation including reliability."""
        return f"{super().__str__()}, reliability={self.reliability:.1f}%"
