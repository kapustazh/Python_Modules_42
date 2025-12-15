class Plant:
    """Plant model representing name, height (cm), and age (days)."""

    def __init__(self, *, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory():
    """Demo routine that creates Plant instances and displays factory output.

    Creates Plant objects from example specifications, prints each created
    plant details and a total count for demonstration and validation.
    """
    plants_specs = [
        ("Rose", 40, 10),
        ("Sunflower", 70, 42),
        ("Violet", 67, 52),
        ("Tulip", 20, 15),
        ("Carnation", 50, 1),
    ]

    plants = [
        Plant(name=name_, height=height_, age=age_)
        for name_, height_, age_ in plants_specs
    ]

    amount_of_plants: int = 0
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        amount_of_plants += 1
    print(f"\nTotal plants created: {amount_of_plants}")


if __name__ == "__main__":
    ft_plant_factory()
