def check_temperature(temp_str):
    """
    Converts input to int, validates range (0-40), and handles errors.
    Returns the integer if valid, otherwise returns None.
    """
    try:
        temp_int = int(temp_str)

        if temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
            return None
        elif temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
            return None
        return temp_int

    except:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    """
    Function that test temperatures value via
    check_temperature function
    """
    temperatures = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===")

    for temp_input in temperatures:
        print()
        print(f"Testing temperature: {temp_input}")
        result = check_temperature(temp_input)
        if result:
            print(f"Temperature {result}°C is perfect for plants!")
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()
