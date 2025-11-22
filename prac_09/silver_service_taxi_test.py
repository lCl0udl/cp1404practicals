"""CP1404/CP5632 - Test SilverServiceTaxi"""

from silver_service_taxi import SilverServiceTaxi


def main():

    luxury_taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(luxury_taxi)
    # Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50

    # text 2：go 18km
    luxury_taxi.drive(18)
    print(luxury_taxi)

    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    actual_fare = taxi.get_fare()
    print(f"18km trip fare: ${actual_fare}")
    assert actual_fare == 48.8, f"Expected 48.8 but got {actual_fare}"

    print("All tests passed!")


main()