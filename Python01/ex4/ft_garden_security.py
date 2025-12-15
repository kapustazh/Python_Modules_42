def value_validation(*, value: int) -> bool:
    """Return True for positive integers (value > 0)."""
    return value > 0


class SecurePlant:
    """Guarded Plant model that validates and encapsulates attributes."""

    def __init__(self, *, name: str, height: int, age: int) -> None:
        """Create a secure plant, validating numeric attributes.

        Attributes are validated and set; invalid values default to 0.
        """
        self.name = name
        if value_validation(value=height):
            self.__height = height
        else:
            print(f"Invalid initial height for {name}: {height} -> set to 0\n")
            self.__height = 0
        if value_validation(value=age):
            self.__age = age
        else:
            print(f"Invalid initial age for {name}: {height} -> set to 0\n")
            self.__age = 0
        """Gets the height of the plant in cm
        """

    def get_height(self) -> int:
        """Return the plant height in centimeters (cm)."""
        return self.__height

    def get_age(self) -> int:
        """Return the plant age in days."""
        return self.__age

    def set_height(self, *, new_height: int) -> None:
        """Validate and set a new height value for the plant."""
        if value_validation(value=new_height):
            self._height = new_height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(
                "\nInvalid operation attempted: "
                f"height {new_height}cm [REJECTED]\n"
                "Security: Invalid height rejected\n"
            )

    def set_age(self, *, new_age: int) -> None:
        """Validate and set a new age value for the plant."""
        if value_validation(value=new_age):
            self.__age = new_age
            if new_age == 1:
                print(f"Age updated: {self.__age} day [OK]")
            else:
                print(f"Age updated: {self.__age} days [OK]")
        else:
            print(
                f"Invalid operation attempted: age {new_age} days [REJECTED]\n"
                "Security: Invalid age rejected\n"
            )


def ft_garden_security():
    """Demo routine that creates SecurePlant instances and shows accessors.

    Creates a list of SecurePlant objects, updates their height and age, and
    prints the resulting state for demonstration and validation.
    """
    plants_specs = [
        ("Rose", 1, 1),
        # ("Sunflower", 70, 42),
        # ("Violet", 67, 52),
        # ("Tulip", 20, 15),
        # ("Carnation", 50, 1),
    ]

    plants = [
        SecurePlant(name=name_, height=height_, age=age_)
        for name_, height_, age_ in plants_specs
    ]
    # Set's the properties of the plants and prints their states
    print("=== Garden Security System ===")
    for plant in plants:
        if plant:
            print(f"Plant created: {plant.name}")
            plant.set_height(new_height=3)
            plant.set_age(new_age=2)
            name = plant.name
            height = plant.get_height()
            age = plant.get_age()
            print(f"\nCurrent plant: {name}, ({height}cm, {age} days)\n")


if __name__ == "__main__":
    ft_garden_security()
