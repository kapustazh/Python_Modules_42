class GardenError(Exception):
    """A basic error for garden problems"""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception for problems with plants"""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception for problems with watering"""

    def __init__(self, message: str) -> None:
        super().__init__(message)


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        wilting = True
        if wilting:
            raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        water_in_jar = 80
        if water_in_jar < 100:
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        wilting = True
        if wilting:
            raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_in_jar = 80
        if water_in_jar < 100:
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
