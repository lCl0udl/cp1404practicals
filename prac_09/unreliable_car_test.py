
from unreliable_car import UnreliableCar


def main():
    bad_car = UnreliableCar("Bad Car", 100, 30.0)
    good_car = UnreliableCar("Reliable Car", 100, 90.0)

    print("Testing Bad Car (30% reliability) over 100 attempts:")
    successes_bad = 0
    for i in range(100):
        distance_driven = bad_car.drive(10)
        if distance_driven > 0:
            successes_bad += 1
    print(f"Bad Car succeeded {successes_bad}/100 times ≈ {successes_bad}%")

    print("\nTesting Reliable Car (90% reliability) over 100 attempts:")
    good_car = UnreliableCar("Reliable Car", 100, 90.0)
    successes_good = 0
    for i in range(100):
        distance_driven = good_car.drive(10)
        if distance_driven > 0:
            successes_good += 1
    print(f"Reliable Car succeeded {successes_good}/100 times ≈ {successes_good}%")

    print(f"\nFinal state of Bad Car: {bad_car}")


main()