def water_plants(*, plant_list: list) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is not None:
                print(f"Watering {plant}")
            else:
                plant = plant[::-1]
    except Exception:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plants = ["Tomato", "Cucumber", "Cabbage"]
    plants_with_error = ["Tomato", None, "Cabbage"]

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plant_list=plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(plant_list=plants_with_error)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
