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


class Plant():
    """Plant model representing name, height (cm), and age (days)."""

    def __init__(self,
                 *, name: str,
                 water_level: int,
                 sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager():

    def __init__(self) -> None:
        self.plant_list = []
        self.water_in_tank = 5

    def add_plant_to_garden(self, *, plants: list[str]) -> None:
        """Add plant to specific garden."""
        try:
            for plant in plants:
                if not plant.name:
                    raise PlantError("Error: Plant name cannot be empty!\n")
                else:
                    print(f"Added {plant.name} successfully")
                    self.plant_list.append(plant)
        except PlantError as e:
            print(e)

    def watering_plants(self) -> None:
        """Method to water the plants

        Args:
            plants (list[str]): _description_
        """
        try:
            for plant in self.plant_list:
                if self.water_in_tank < 2:
                    raise GardenError(
                        "Caught GardenError: Not enough water in tank")
                else:
                    self.water_in_tank -= 1
                    plant.water_level += 1
                    print(f"Watering {plant.name} - success")
        except GardenError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self) -> None:
        """Method to check the health of the plants"""
        try:
            for plant in self.plant_list:
                if plant.water_level > 10:
                    raise PlantError(
                        f"Error checking {plant.name}: Water Level "
                        f"{plant.water_level}"
                        " is too high (max 10)\n")
                elif plant.sunlight_hours < 2:
                    raise PlantError(
                        f"Error Sunlight hours {plant.sunlight_hours}"
                        " is to low (min 2)\n")
                else:
                    print(
                        f"{plant.name}: "
                        f"healthy (water: {plant.water_level}, "
                        f"sun: {plant.sunlight_hours})")
        except PlantError as e:
            self.garden_error_flag = True
            print(e)

    def error_recovery(self) -> None:
        "I have no idea what ths function does"
        if self.water_in_tank < 2:
            print("Caught GardenError: Not enough water in tank")
            print("System recovered and continuing...\n")
            self.water_in_tank = 100


def ft_garden_management():
    print("=== Garden Management System ===\n")

    plants_specs = [
        ("tomato", 9, 3),
        ("cabbage", 42, 42),
        ("", 67, 11),
    ]

    plants = [
        Plant(name=name, water_level=water_level,
              sunlight_hours=sunlight_hours)
        for name, water_level, sunlight_hours, in plants_specs
    ]

    print("Adding plants to garden...")
    manager = GardenManager()
    manager.add_plant_to_garden(plants=plants)

    print("Watering plants...")
    print("Opening watering system")
    manager.watering_plants()

    print("Checking plant health...")
    manager.check_plant_health()

    print("Testing error recovery...")
    manager.error_recovery()
    print("Garden management system test complete!")


if __name__ == "__main__":
    ft_garden_management()
