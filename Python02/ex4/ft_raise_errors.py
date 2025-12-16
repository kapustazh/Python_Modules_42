def check_plant_health(plant_name, water_level, sunlight_hours) -> None:
    """Function to check plant health based on given parameters"""
    try:
        if not plant_name:
            raise ValueError("Error: Plant name cannot be empty!\n")
        elif water_level > 10:
            raise ValueError(
                f"Error: Water Level {water_level} is too high (max 10)\n")
        elif sunlight_hours < 2:
            raise ValueError(
                f"Error Sunlight hours {sunlight_hours} is to low (min 2)\n")
        else:
            print(f"Plant '{plant_name}' is healthy!\n")
    except ValueError as e:
        print(e)


def test_plant_checks():
    """Function to test plant health checks"""
    print("=== Garden Plant Health Checker ===")

    print("Testing good values...")
    check_plant_health(plant_name="tomato", water_level=10, sunlight_hours=5)

    print("Testing empty plant name...")
    check_plant_health(plant_name="", water_level=10, sunlight_hours=5)

    print("Testing bad water level...")
    check_plant_health(plant_name="wheat", water_level=15, sunlight_hours=5)

    print("Testing bad sunlight hours...")
    check_plant_health(plant_name="wheat", water_level=10, sunlight_hours=0)


if __name__ == "__main__":
    test_plant_checks()

# Authorized: try, except, raise, ValueError, print()
