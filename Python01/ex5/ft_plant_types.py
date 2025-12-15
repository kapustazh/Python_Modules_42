class Plant:
    """Plant model representing name, height (cm), and age (days)."""

    def __init__(self, *, name: str, height: int, age: int) -> None:
        """Initialize a Plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return a short description with class, height, and age."""
        class_name = self.__class__.__name__
        return f"{self.name}: ({class_name}) {self.height}cm, {self.age} days"

    def actions(self) -> list[str]:
        """Return a list of actions this plant can perform (default empty)."""
        return []


class Tree(Plant):
    """Tree model that extends Plant with a trunk diameter and shade."""

    def __init__(self,
                 *, name: str,
                 height: int,
                 age: int,
                 trunk_diameter: int) -> None:
        """Initialize a Tree, including trunk diameter."""
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> str:
        """Return extended info for a Tree, including trunk diameter."""
        base = super().get_info()
        return f"{base}, {self.trunk_diameter}cm diameter"

    def produce_shade(self) -> str:
        """Compute an approximation of shade provided and return a message."""
        area = self.trunk_diameter * 1.5
        return f"{self.name} provides {area:.0f} square meters of shade\n"

    def actions(self) -> list[str]:
        """Return a list of Tree actions, e.g. producing shade."""
        return [self.produce_shade()]


class Flower(Plant):
    """Flower model that extends Plant with color and bloom behavior."""

    def __init__(self,
                 *,
                 name: str,
                 height: int,
                 age: int,
                 color: str) -> None:
        """Initialize a Flower with a color on top of base plant attributes."""
        super().__init__(name=name, height=height, age=age)
        self.color = color

    def get_info(self) -> str:
        """Return extended info for a Flower, including color."""
        base = super().get_info()
        return f"{base}, {self.color} color"

    def bloom(self) -> str:
        """Simulate the flower blooming and return a display string."""
        return (f"{self.name} is blooming beatufilly!\n")

    def actions(self) -> list[str]:
        """Return a list of actions this Flower can perform (e.g. bloom)."""
        return [self.bloom()]


class Vegetable(Plant):
    """Vegetable model that extends Plant with harvest and nutrition data."""

    def __init__(self,
                 *,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutrition_value: str) -> None:
        """Initialize a Vegetable with harvest season and nutrition info."""
        super().__init__(name=name, height=height, age=age)
        self.harvest_season = harvest_season
        self.nutrition_value = nutrition_value

    def get_info(self) -> str:
        """Return info for Vegetable including harvest season and nutrition."""
        base = super().get_info()
        return (
            f"{base}, {self.harvest_season} harvest\n"
            f"{self.name} is rich in vitamin {self.nutrition_value}\n"
        )


def ft_plant_types():
    """Demo routine that showcases plant types and their actions.

    Creates several Plant subclasses (Flower, Tree, Vegetable) and prints
    their info and the actions they can perform (blooming, shade, etc.).
    """
    flowers = {
        ("Rose", 25, 30, "red"),
        ("Violet", 30, 20, "blue"),
        ("Sunflower", 70, 70, "yellow")
    }

    trees = {
        ("Oak", 2500, 6120, 100),
        ("Bobab", 700, 315, 40),
        ("Willow", 3300, 1242, 120)
    }

    vegetables = {
        ("Lemon", 80, 90, "summer", "C"),
        ("Carrot", 30, 120, "spring", "A"),
        ("Cabbage", 40, 100, "spring", "A")
    }

    list_of_flowers = [
        Flower(name=name, height=height, age=age, color=color)
        for name, height, age, color in flowers
    ]
    list_of_trees = [
        Tree(name=name, height=height, age=age, trunk_diameter=trunk_diameter)
        for name, height, age, trunk_diameter in trees
    ]
    list_of_vegetables = [
        Vegetable(
            name=name, height=height, age=age,
            harvest_season=harvest_season, nutrition_value=nutrition_value
        )
        for name, height, age, harvest_season, nutrition_value in vegetables
    ]
    list_of_plants = list_of_vegetables + list_of_flowers + list_of_trees
    print("=== Garden Plant Types ===")
    for plant in list_of_plants:
        print(plant.get_info())
        for action in plant.actions():
            print(action)


if __name__ == "__main__":
    ft_plant_types()
