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
    """Plant model representing name, water level, and sunlight."""

    def __init__(
            self,
            name: str,
            water_level: int,
            sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager():
    """Class to manage garden operations."""

    def __init__(self) -> None:
        self.plant_list = []
        self.water_in_tank = 5

    def add_plant_to_garden(self, plants: list[Plant]) -> None:
        """Add plant to specific garden."""
        for plant in plants:
            try:
                if not plant.name:
                    raise PlantError("Error adding plant: Plant "
                                     "name cannot be empty!")
                print(f"Added {plant.name} successfully")
                self.plant_list += [plant]
            except PlantError as e:
                print(e)

    def watering_plants(self) -> None:
        """Method to water the plants"""
        print("Opening watering system")
        try:
            for plant in self.plant_list:
                if self.water_in_tank <= 0:
                    raise WaterError("Caught GardenError: "
                                     "Not enough water in tank")

                self.water_in_tank -= 1
                plant.water_level += 1
                print(f"Watering {plant.name} - success")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Method to check the health of the plants"""
        for plant in self.plant_list:
            try:
                if plant.water_level > 10:
                    raise PlantError(f"Error checking {plant.name}: "
                                     f"Water level {plant.water_level} "
                                     "is too high (max 10)")
                if plant.sunlight_hours < 2:
                    raise PlantError(f"Error checking {plant.name}: "
                                     f"Sunlight {plant.sunlight_hours} "
                                     "is too low (min 2)")

                print(f"{plant.name}: healthy "
                      f"(water: {plant.water_level}, "
                      f"sun: {plant.sunlight_hours})")
            except PlantError as e:
                print(e)

    def error_recovery(self) -> None:
        """Simulate a crash and recovery scenario"""
        try:
            self.water_in_tank = 0
            if self.water_in_tank < 1:
                raise GardenError("Caught GardenError: "
                                  "Not enough water in tank")
        except GardenError as e:
            print(e)
            print("System recovered and continuing...")
            self.water_in_tank = 5


def ft_garden_management():
    """Function to test garden management system"""
    print("=== Garden Management System ===\n")

    tomato = Plant("tomato", 9, 3)
    lettuce = Plant("lettuce", 42, 42)
    empty = Plant("", 10, 10)

    print("Adding plants to garden...")
    manager = GardenManager()
    manager.add_plant_to_garden([tomato, lettuce, empty])

    print("\nWatering plants...")
    manager.watering_plants()

    print("\nChecking plant health...")
    manager.check_plant_health()

    print("\nTesting error recovery...")
    manager.error_recovery()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    ft_garden_management()
