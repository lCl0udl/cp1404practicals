"""
guitar_test.py

Simple, manual tests for Guitar.get_age() and Guitar.is_vintage().

Estimate: 10 minutes
Actual: 10 minutes
Start: 2025-11-01 18:39 (SGT)
End: 2025-11-01 18:49 (SGT)
"""

from datetime import date
from prac_06.guitar import Guitar


def test_guitars():
    current_year = date.today().year

    g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    g2 = Guitar("Another Guitar", 2013, 1000.00)

    expected_age_g1 = current_year - 1922
    expected_age_g2 = current_year - 2013

    print(f"{g1.name} get_age() - Expected {expected_age_g1}. Got {g1.get_age()}")
    print(f"{g2.name} get_age() - Expected {expected_age_g2}. Got {g2.get_age()}")

    print(f"{g1.name} is_vintage() - Expected {expected_age_g1 >= 50}. Got {g1.is_vintage()}")
    print(f"{g2.name} is_vintage() - Expected {expected_age_g2 >= 50}. Got {g2.is_vintage()}")


if __name__ == '__main__':
    test_guitars()