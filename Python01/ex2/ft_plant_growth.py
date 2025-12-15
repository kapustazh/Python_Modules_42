class Plant():
    """Plant model representing name, height (cm), and age (days)."""

    def __init__(self, *, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, *, height: int = 1):
        """Method to grow the plant which change the height of the Plan"""
        self.height += height

    def age_plant(self, *, age: int = 1):
        """Method to age the plant which change the age of the Plant"""
        self.age += age

    def get_info(self):
        """Method print info(name, height and age) of the plant"""
        print(f"{self.name}: {self.height}cm, {self.age} days old\n")


def ft_plant_growth():
    """Demo routine that simulates daily plant growth and aging.

    Builds a list of Plant instances, simulates daily growth and aging, and
    prints updates and summary growth totals to show simulated changes.
    """
    plants_specs = [
        ("Rose", 40, 10),
        ("Sunflower", 70, 42),
        ("Violet", 67, 52),
    ]

    plants = [
        Plant(name=name_, height=height_, age=age_)
        for name_, height_, age_ in plants_specs
    ]

    start_heights = {plant.name: plant.height for plant in plants}

    current_day: int = 1
    while current_day < 8:
        print(f"=== Day {current_day} ===")
        for plant in plants:
            plant.grow()
            plant.age_plant()
            plant.get_info()
        current_day += 1

    for plant in plants:
        growth = plant.height - start_heights[plant.name]
        print(f"Weekly growth of {plant.name}: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
