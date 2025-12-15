class Plant:
    """Plant model representing name, height (cm), and age (days)."""

    def __init__(self, *, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():
    """Demo routine that builds a small registry and prints plant data.

    Creates a small list of Plant instances and prints the formatted
    registry for demonstration and validation of data composition.
    """
    rose = Plant(name="Rose", height=40, age=10)
    sunflower = Plant(name="Sunflower", height=70, age=42)
    violet = Plant(name="Violets", height=67, age=52)

    print("=== Garden Plant Registry ===")
    registry = (
        f"{rose.name}: {rose.height}cm, {rose.age} days old\n"
        f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old\n"
        f"{violet.name}: {violet.height}cm, {violet.age} days old"
    )
    print(registry)


if __name__ == "__main__":
    ft_garden_data()
