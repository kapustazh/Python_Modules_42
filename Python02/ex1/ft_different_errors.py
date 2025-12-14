from fileinput import close


def garden_operations(*, error_name: str) -> None:
    """
    Function to execute operations on garden's states
    """
    plant_inventory = {10: "Sunflower"}
    if error_name == "ValueError":
        try:
            garden_age = int("abc")
            print(f"Garden is {garden_age} years old")
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")
    if error_name == "ZeroDivisionError":
        try:
            water_per_plant = 100 / 0
            print(f"Garden needs {water_per_plant} per each plant\n")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
    if error_name == "FileNotFoundError":
        try:
            open("missing.txt")
            close()
            print("Garden info was reviewed!\n")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    if error_name == "KeyError":
        try:
            plant_to_sell = plant_inventory[1]
            print(f"{plant_to_sell} is ready to be sold\n")
        except KeyError:
            print(f"Caught KeyError: 'missing\\_plant'\n")

    if error_name == "all":
        try:
            garden_name = int("Sunshine")
            water_per_plant = 100 / 0
            open("missing.txt")
            close()
        except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
            print("Caught an error, but program continues!\n")




def test_dynamic_inputs():
    """
    Test of different error types
    throughout the runtime of the program
    """
    print("=== Garden Error Types Demo ===")
    print("Testing ValueError...")
    garden_operations(error_name="ValueError")

    print("Testing ZeroDivisionError...")
    garden_operations(error_name="ZeroDivisionError")

    print("Testing FileNotFoundError...")
    garden_operations(error_name="FileNotFoundError")

    print("Testing KeyError...")
    garden_operations(error_name="KeyError")

    print("Testing multiple errors together...")
    garden_operations(error_name="all")

    print("All error types tested successfully!")

if __name__ == "__main__":
    test_dynamic_inputs()