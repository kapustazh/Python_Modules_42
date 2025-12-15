class Plant:
    """Plant model representing name, height (cm), and age (days)."""

    def __init__(self, *, name: str, height: int, age: int) -> None:
        """Initialize a plant"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, *, increment: int = 1) -> None:
        """Grow the plant by increment cm."""
        self.height += increment

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Flowering plant with color."""

    def __init__(self, *, name: str, height: int, age: int,
                 color: str) -> None:
        """Initialize flowering plant."""
        super().__init__(name=name, height=height, age=age)
        self.color = color

    def get_info(self) -> str:
        """Return formatted info."""
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming)")


class PrizeFlower(FloweringPlant):
    """Prize flower with points."""

    def __init__(self, *, name: str, height: int, age: int, color: str,
                 prize_points: int) -> None:
        """Initialize prize flower."""
        super().__init__(name=name, height=height, age=age, color=color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        """Return formatted info."""
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.prize_points}")


class GardenManager:
    """Manages multiple gardens with nested statistics helper."""

    def __init__(self) -> None:
        """Initialize manager."""
        self.total_gardens = 0
        self.all_gardens = {}

    class GardenStats:
        """Statistics helper for a garden (nested inside GardenManager)."""

        def __init__(self, *, name: str) -> None:
            """Initialize stats."""
            self.name = name
            self.plants = ()
            self.count_added = 0
            self.count_regular = 0
            self.count_flowering = 0
            self.count_prize = 0
            self.total_growth = 0

        def classify_plant(self, *, plant_type: str) -> None:
            """Classify and count plant by type."""
            if plant_type == "PrizeFlower":
                self.count_prize += 1
            elif plant_type == "FloweringPlant":
                self.count_flowering += 1
            elif plant_type == "Plant":
                self.count_regular += 1

        def compute_score(self) -> int:
            """Compute garden score from all plants."""
            score = 0
            for plant in self.plants:
                score += plant.height + plant.age
                if plant.__class__.__name__ == "PrizeFlower":
                    score += plant.prize_points
            return score

    @staticmethod
    def validate_height(height: int) -> bool:
        """Utility: validate plant height (class-level utility)."""
        return height > 0

    @classmethod
    def create_garden_network(cls, *, names: list[str] | None = None):
        """Create and return a manager with initial gardens (class method)."""
        if names is None:
            names = ["Alice", "Bob"]
        manager = cls()
        for name in names:
            manager.add_garden(name=name)
        return manager

    def add_garden(self, *, name: str) -> None:
        """Add a garden to the network."""
        if name not in self.all_gardens:
            self.all_gardens[name] = GardenManager.GardenStats(name=name)
            self.total_gardens += 1

    def add_plant_to_garden(self, *, garden_name: str, plant: Plant
                            ) -> None:
        """Add plant to specific garden."""
        if garden_name not in self.all_gardens:
            print(f"Error: Garden '{garden_name}' not found")
            return

        stats = self.all_gardens[garden_name]
        stats.plants = stats.plants + (plant,)
        stats.count_added += 1
        stats.classify_plant(plant_type=plant.__class__.__name__)
        print(f"Added {plant.name} to {garden_name}'s garden")

    def grow_plants(self, *, garden_name: str | None = None,
                    increment: int = 1) -> None:
        """Grow plants in specified garden(s)."""
        if garden_name and garden_name in self.all_gardens:
            gardens = [self.all_gardens[garden_name]]
        else:
            gardens = []
            for g_name in self.all_gardens:
                gardens = gardens + [self.all_gardens[g_name]]
        for stats in gardens:
            for plant in stats.plants:
                plant.grow(increment=increment)
                stats.total_growth += increment

    def get_garden_report(self, *, garden_name: str) -> str:
        """Display summary of the garden"""
        if garden_name not in self.all_gardens:
            return ""

        stats = self.all_gardens[garden_name]

        header = f"=== {garden_name}'s Garden Report ===\nPlants in garden:\n"

        plants_info = ""
        first = True
        for plant in stats.plants:
            if not first:
                plants_info += "\n"
            plants_info += f"- {plant.get_info()}"
            first = False

        height_ok = True
        for p in stats.plants:
            if not self.validate_height(p.height):
                height_ok = False
                break

        summary = (
            f"\nPlants added: {stats.count_added}, "
            f"Total growth: {stats.total_growth}cm\n"
            f"Plant types: {stats.count_regular} regular, "
            f"{stats.count_flowering} flowering, {stats.count_prize} "
            f"prize flowers\n"
            f"Height validation test: {height_ok}"
        )

        return header + plants_info + summary

    def display_network_summary(self) -> None:
        """Display summary of all gardens in network."""
        scores = ""
        first = True
        for name in self.all_gardens:
            stats = self.all_gardens[name]
            entry = f"{name}: {stats.compute_score()}"
            if first:
                scores = entry
                first = False
            else:
                scores += ", " + entry
        print(f"Garden scores - {scores}")
        print(f"Total gardens managed: {self.total_gardens}")


def ft_garden_analytics() -> None:
    """Main demo function showcasing garden management system."""
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network(names=["Alice", "Bob"])

    manager.add_plant_to_garden(
        garden_name="Alice",
        plant=Plant(name="Oak Tree", height=100, age=10),
    )
    manager.add_plant_to_garden(
        garden_name="Alice",
        plant=FloweringPlant(name="Rose", height=25, age=5, color="red"),
    )
    manager.add_plant_to_garden(
        garden_name="Alice",
        plant=PrizeFlower(name="Sunflower", height=50, age=15,
                          color="yellow", prize_points=10),
    )

    manager.add_plant_to_garden(
        garden_name="Bob",
        plant=Plant(name="Cactus", height=40, age=10),
    )
    manager.add_plant_to_garden(
        garden_name="Bob",
        plant=FloweringPlant(name="Tulip", height=20, age=20, color="pink"),
    )

    print()
    print("Alice is helping all plants grow...")
    manager.grow_plants(garden_name="Alice", increment=1)
    for plant in manager.all_gardens["Alice"].plants:
        print(f"{plant.name} grew 1cm")

    print()
    print(manager.get_garden_report(garden_name="Alice"))
    print()
    manager.display_network_summary()


if __name__ == "__main__":
    ft_garden_analytics()
