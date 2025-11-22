
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel, price_per_km=0)
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the total fare including flagfall."""
        base_fare = super().get_fare()
        return round(base_fare + self.flagfall, 1)

    def __str__(self):
        """Return a string representation including price per km and flagfall."""
        return (f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}")
